from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={
            'min_length': 'Password must be at least 8 characters long.'
        }
    )
    phone_number = serializers.CharField(
        max_length=20,
        required=False,
        allow_null=True,
        error_messages={
            'max_length': 'Phone number cannot be longer than 20 characters.'
        }
    )
    
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at', 'password']
        extra_kwargs = {
            'created_at': {'read_only': True},
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        return value

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField(max_length=1000)
    
    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']
        read_only_fields = ['message_id', 'sender', 'sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']
        read_only_fields = ['conversation_id', 'created_at']

