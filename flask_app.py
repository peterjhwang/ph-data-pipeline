from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.INFO)
application = Flask(__name__)

@application.route('/test')
def get_test():
    return jsonify({'message': 'service is working'})
    
from controllers import stats_controllers