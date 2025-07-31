from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_message_notification(sender, instance, created, **kwargs):
    """
    Creates a notification for the receiver when a new message is sent.
    """
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )
        print(f"Notification created for {instance.receiver}")

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """
    Logs previous content before a message is edited.
    """
    if instance.pk:  # Only for existing messages (not new ones)
        original = Message.objects.get(pk=instance.pk)
        if original.content != instance.content:  # Only log if content changed
            MessageHistory.objects.create(
                message=instance,
                old_content=original.content,
                edited_by=instance.sender
            )
            instance.edited = True
            instance.last_edited = timezone.now()

