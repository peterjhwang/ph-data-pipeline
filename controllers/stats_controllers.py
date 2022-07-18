from flask import jsonify
from flask_app import application
from services.stats.stats_api_service import stats_api_refresh 

@application.route('/stats_api')
def refresh_stats_api():
    application.logger.info('/stats_api')
    try:
        stats_api_refresh()
        return jsonify({'message': 'Stats data successfully refreshed'})
    except Exception as e:
        return jsonify({'Error message': str(e)})