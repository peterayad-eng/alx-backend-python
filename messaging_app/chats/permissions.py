from rest_framework import permissions
from .models import Conversation

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only owners to view their own messages/conversations.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to authenticated users who are participants in the conversation.
    """

    def has_permission(self, request, view):
        # Require user to be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # obj here should be a Message or Conversation instance
        conversation = getattr(obj, 'conversation', None)
        if conversation:
            return request.user in conversation.participants.all()
        elif isinstance(obj, Conversation):
            return request.user in obj.participants.all()
        return False

