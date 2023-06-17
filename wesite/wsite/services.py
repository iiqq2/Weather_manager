from datetime import datetime, timedelta
from wsite.tasks import send_email_task
from wsite.models import City
from wsite.weather import *



def create_city(new_city):
    try:
        city = City.objects.get(name=new_city)
    except City.DoesNotExist:
        city = City()
        city.name = new_city
        city.weather_data = get_weather(new_city)
        city.save()


def schedule_email(time, email, city):
    recipients_mail = email
    current_time = datetime.utcnow()
    hours, minutes, seconds = time.split(':')
    delta = timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
    scheduled_time = current_time + delta
    send_email_task.apply_async(args=[recipients_mail, city], eta=scheduled_time, retry=False)