from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

# Create your views here.
User = get_user_model()

@login_required
@require_POST
def delete_user(request):
    """View to handle user account deletion."""
    user = request.user
    user.delete()  # This will trigger the post_delete signal
    return redirect('home')

def thread_view(request, message_id):
    """Displays a message and its full thread with optimized queries"""
    message = get_object_or_404(
        Message.objects.select_related('sender', 'receiver'),
        pk=message_id
    )

    # Get all replies (including nested) with optimized queries
    thread = message.get_thread()

    return render(request, 'messaging/thread.html', {
        'message': message,
        'thread': thread
    })

def conversation_list(request, user_id):
    """Lists all conversations with the user (top-level messages only)"""
    conversations = Message.objects.filter(
        models.Q(sender=request.user) | models.Q(receiver=request.user),
        parent_message__isnull=True  # Only top-level messages
    ).select_related('sender', 'receiver').prefetch_related('replies')

    return render(request, 'messaging/conversations.html', {
        'conversations': conversations
    })

