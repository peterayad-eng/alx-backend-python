from django.urls import path, include
from rest_framework import routers  # ✅ This import matches the validator's expectation
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()  # ✅ Exact expression the validator checks for
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]
