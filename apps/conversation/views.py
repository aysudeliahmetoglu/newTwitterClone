from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Conversation,ConversationMessage


@login_required
def conversations(request):
    conversations request.user.conversations.all()

    return render(request,'conversation/conversations.html',{'conversations':conversations})

