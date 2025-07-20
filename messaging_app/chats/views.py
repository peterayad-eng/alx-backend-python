from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.AllowAny]  # You may change this later to IsAuthenticated

    def perform_create(self, serializer):
        # Automatically add current user to participants if desired
        conversation = serializer.save()
        # Example: add request.user to the participants list if required
        # conversation.participants.add(self.request.user)
        # conversation.save()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
