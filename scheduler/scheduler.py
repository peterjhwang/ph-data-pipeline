from apscheduler.schedulers.background import BackgroundScheduler
from services.stats.stats_api_service import stats_api_refresh
from utils.aws.sns import send_message
import pytz

nz_data_scheduler = BackgroundScheduler(timezone = pytz.timezone('Pacific/Auckland'))
nz_data_scheduler.add_job(func=stats_api_refresh, 
    trigger='cron', 
    minute='5',
    hour='1',
    day='*/2',
    month='*',
    week='*',
    id='data_refresh')
nz_data_scheduler.start()