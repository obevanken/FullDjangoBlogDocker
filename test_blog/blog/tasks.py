import logging
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from test_blog.celery import app


@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        link = 'http://3a664438.ngrok.io'
        send_mail(
            "Поддтверждение аккаунта",
            "Здравствуйте " + user.username + " для подтверждения аккакунта переходите по ссылке " + link + "/verify/" + str(user.verification_uuid) + "/",
            "От Андрея",
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user'%s'" % user_id)


@app.task
def create_message(user_id, room_name, message):
        from .models import Message, User, Room
        user = User.objects.get(pk=user_id)
        room = Room.objects.filter(title=room_name).first()
        result = Message.objects.create(text=message, user=user, room=room)
        result.save()
