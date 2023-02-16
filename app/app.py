from flask import Flask, request, jsonify
import logging, os, calendar, time, json
from gevent.pywsgi import WSGIServer
import db

logging.basicConfig(filename="/data/srv.log", level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(levelname)s:%(message)s')
logging.info('\n##\n\tversion.groundseg.app running\n##\n')

authkey = os.getenv('AUTHKEY')

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_conf():
    content = db.get_value('content','content','content')
    content = json.loads(content)
    return content

@app.route("/modify/groundseg/<version>/<software>/<key>/<value>", methods=["PUT"])
def upd_conf(version,software,key,value):
    logging.info(f'Updating {version} {software}: {key}={value}')
    db.upd_value(version,software,key,value)
    db.generate_content()
    return 'ok'

@app.before_request
def before_request():
    if request.path.startswith('/modify'):
        headers = request.headers
        auth = headers.get("X-Api-Key")
        fwd_ip = headers.get("X-Forwarded-For")
        logging.warning(f'Failed auth request from {fwd_ip}')
        if auth != authkey:
            return jsonify({"error": "Failed auth"}), 403

if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 8090), app)
    http_server.serve_forever()