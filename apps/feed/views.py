from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Oink

@login_required
def feed(request):
    userids = [request.user.id]

    for oinker in request.user.oinkerprofile.follows.all():
        userids.append(oinker.user.id)

    oinks = Oink.objects.filter(created_by_id__in=userids)  
    return render(request,'feed/feed.html', {'oinks':oinks})