from apscheduler.schedulers.background import BackgroundScheduler
from controllers.stats_controllers import refresh_stats_api
import pytz

nz_data_scheduler = BackgroundScheduler(timezone = pytz.timezone('Pacific/Auckland'))
nz_data_scheduler.add_job(func=refresh_stats_api, 
    trigger='cron', 
    minute='5',
    hour='1',
    day='*/2',
    month='*',
    week='*',
    id='data_reload')
nz_data_scheduler.start()