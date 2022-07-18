from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.INFO)
application = Flask(__name__)

from controllers import test_controllers, stats_controllers
from scheduler import scheduler

@application.route('/test')
def get_test():
    return jsonify({'message': 'service is working'})
    
