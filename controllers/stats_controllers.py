from flask import jsonify
from flask_app import application
from utils.aws.sns import send_message
from services.stats.stats_api_service import stats_api_refresh 

@application.route('/stats_api')
def refresh_stats_api():
    application.logger.info('/stats_api')
    try:
        stats_api_refresh()
        send_message("INFO", 'Cache file successfully refreshed.\n\nph-data-pipeline')
        return jsonify({'message': 'Stats data successfully refreshed'})
    except Exception as e:
        send_message("ERROR", str(e) + '\n\nh-data-pipeline')
        return jsonify({'Error message': str(e)})