from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UnreadMessagesManager(models.Manager):
    """Custom manager for unread messages"""
    def for_user(self, user):
        return self.filter(
            receiver=user,
            read=False
        ).select_related('sender').only(
            'id', 'content', 'timestamp', 'sender__username'
        )

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    last_edited = models.DateTimeField(null=True, blank=True)
    read = models.BooleanField(default=False)
    parent_message = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )

    # Managers
    objects = models.Manager()  # Default manager
    unread = UnreadMessagesManager()  # Custom manager

    class Meta:
        ordering = ['-timestamp']  # Newest messages first

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}'

    def get_thread(self):
        """Recursively fetches all replies in a thread"""
        thread = []
        for reply in self.replies.all().select_related('sender', 'receiver'):
            thread.append(reply)
            thread.extend(reply.get_thread())
        return thread

    def mark_as_read(self):
        """Helper method to mark message as read"""
        self.read = True
        self.save(update_fields=['read'])

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user}'

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-edited_at']  # Show newest edits first

    def __str__(self):
        return f"Edit of {self.message} at {self.edited_at}"

