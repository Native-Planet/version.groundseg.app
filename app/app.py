from flask import Flask, request, jsonify
import logging, os, calendar, time
from gevent.pywsgi import WSGIServer

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(levelname)s:%(message)s')
logging.info('\n##\version.groundseg.app running\n##\n')

app = Flask(__name__)

@app.route("/", methods=["GET"])
def upload():
    return 'ok'

if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 8090), app)
    http_server.serve_forever()