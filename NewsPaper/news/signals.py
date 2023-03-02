from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .tasks import send_notifications

from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':

        categories = instance.postCategory.all()
        subscribers: list[str] = []
        for category in categories:
            print(f'{categories = }')
            subscribers += category.subscribers.all()


        for user in subscribers:

            print(f'{user.email = }')

        subscribers = [s.email for s in subscribers]

        send_notifications.delay(instance.preview(), instance.pk, instance.title, subscribers)
