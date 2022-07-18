from flask_app import application
from flask import request, jsonify
from utils.aws.sns import send_message

@application.route('/send_email', methods=['POST'])
def send_email():
    try:
        req = request.get_json()
        typ, message = req['type'], req['message']
        response = send_message(typ, message)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return jsonify({'message': 'successfully sent'})
        else:
            return jsonify({'error': response})
    except Exception as e:
        return jsonify({'error': str(e)}) 