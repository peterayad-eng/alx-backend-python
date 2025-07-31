from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Message, Notification, MessageHistory

User = get_user_model()

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

@receiver(post_delete, sender=User)
def delete_related_user_data(sender, instance, **kwargs):
    """
    Deletes related messages, notifications, and histories after a user account is deleted.
    """
    # Delete messages sent or received by the user
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete notifications for this user
    Notification.objects.filter(user=instance).delete()

    # Delete message histories for messages sent by this user
    MessageHistory.objects.filter(message__sender=instance).delete()

    print(f"[Signal] Cleaned up all related data for deleted user {instance.username}")

