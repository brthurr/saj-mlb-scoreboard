from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date
import statsapi
import json

#scheduler = BackgroundScheduler(daemon=True)

def fetch_schedule():
    # Fetch today's schedule
    schedule = statsapi.schedule(date=date.today())
    
    # Save schedule into a json file
    with open('schedule.json', 'w') as f:
        json.dump(schedule, f)

    print("Schedule fetched successfully!")

# Fetch the schedule every day at 00:01
#scheduler.add_job(fetch_schedule, 'cron', day_of_week='mon-sun', hour=0, minute=1)
#scheduler.start()

# Keep the script running.
#while True:
#    pass

fetch_schedule()

