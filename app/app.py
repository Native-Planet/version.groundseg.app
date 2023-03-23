from flask import Flask, request, jsonify
import logging, os, calendar, time, json
from gevent.pywsgi import WSGIServer
import db

logging.basicConfig(filename="/data/srv.log", level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(levelname)s:%(message)s')
logging.info('\n##\n\tversion.groundseg.app running\n##\n')

authkey = os.getenv('AUTHKEY')

app = Flask(__name__)

# return cached version object
@app.route("/", methods=["GET"])
def get_conf():
    content = db.get_value('content','content','content')
    content = json.loads(content)
    return content

# route for modifying values in the version object
@app.route("/modify/groundseg/<channel>/<software>/<key>/<value>", methods=["PUT"])
def upd_conf(channel,software,key,value):
    if value == 'payload':
        # if we want to submit a string that wont work with url
        content = request.get_json()
        value = content.get('value')
    logging.info(f'Updating {channel} {software}: {key}={value}')
    db.upd_value(channel,software,key,value)
    db.generate_content()
    return 'ok'

# check for header auth
@app.before_request
def before_request():
    if request.path.startswith('/modify'):
        headers = request.headers
        auth = headers.get("X-Api-Key")
        fwd_ip = headers.get("X-Forwarded-For")
        if auth != authkey:
            logging.warning(f'Failed auth request from {fwd_ip}')
            return jsonify({"error": "Failed auth"}), 403

if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 8090), app)
    http_server.serve_forever()