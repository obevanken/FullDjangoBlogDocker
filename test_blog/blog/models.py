from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_verification_email
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth.models import AbstractUser
from .managers import LikeDislikeManager
from ckeditor_uploader.fields import RichTextUploadingField
import uuid


class User(AbstractUser):
    avatar = models.ImageField(verbose_name='Аватар', upload_to='img/',
                               null=True, blank=True)
    about = models.TextField(verbose_name='О себе', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_verification_email.delay(instance.id)


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Post(models.Model):
    title = models.CharField(null=False, verbose_name='Заголовок',
                             max_length=64)
    text = RichTextUploadingField(verbose_name="Текст", null=True)
    views = models.IntegerField(verbose_name='Просмотры', default=0)
    user = models.ForeignKey(User, related_name='Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='img/', null=True, blank=True)
    votes = GenericRelation(LikeDislike, related_query_name='articles')

    def __str__(self):
        return self.title
