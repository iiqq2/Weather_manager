from celery import shared_task
from django.core.mail import send_mail
from wesite.settings import EMAIL_HOST_USER
from wsite.weather import update_weather
from wsite.models import City


@shared_task
def send_email_task(recipient_mail, city):
    update_weather(city)
    city = City.objects.get(name=city)
    message = f'Здравствуйте вот данные о погоде {city.weather_data}'
    recipient_list = [recipient_mail]
    subject = f"qq Вот данные о погоде в городе {city.name}"
    from_email = EMAIL_HOST_USER
    send_mail(subject, message, from_email, recipient_list)