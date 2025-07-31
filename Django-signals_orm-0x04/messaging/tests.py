from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message, Notification

# Create your tests here.
User = get_user_model()

class SignalTests(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='testpass123')
        self.receiver = User.objects.create_user(username='receiver', password='testpass123')

    def test_notification_created_on_message_save(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Hello, this is a test message!"
        )

        # Check if a notification was created
        notification = Notification.objects.filter(user=self.receiver, message=message).first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.message.content, message.content)

