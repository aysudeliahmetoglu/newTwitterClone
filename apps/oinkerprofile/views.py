from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def oinkerprofile(request,username):
    user = get_object_or_404(User,username=username)

    context = {
        'user':user
    }

    return render(request,'oinkerprofile/oinkerprofile.html',context)

@login_required
def follow_oinker(request,username):
    user = get_object_or_404(User,username=username)

    request.user.oinkerprofile.follows.add(user.oinkerprofile)

    return redirect('oinkerprofile', username=username)


@login_required
def unfollow_oinker(request,username):
    user = get_object_or_404(User,username=username)

    request.user.oinkerprofile.follows.remove(user.oinkerprofile)

    return redirect('oinkerprofile', username=username)


def followers(request,username):
    user = get_object_or_404(User,username=username)

    return render(request,'oinkerprofile/followers.html',{'user':user})


def follows(request,username):
    user = get_object_or_404(User,username=username)

    return render(request,'oinkerprofile/follows.html',{'user':user})


