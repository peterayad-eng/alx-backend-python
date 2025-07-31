from django.shortcuts import render
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

