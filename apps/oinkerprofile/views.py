from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import OinkerprofileForm

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
def edit_profile(request):
    if request.method == 'POST':
        form = OinkerprofileForm(request.POST, request.FILES,instance=request.user.oinkerprofile)

        if form.is_valid():
            form.save()

            return redirect('oinkerprofile',username=request.user.username)
    else:
        form = OinkerprofileForm(instance=request.user.oinkerprofile)
    
    context = {
        'user':request.user,
        'form':form
    }

    return render(request,'oinkerprofile/edit_profile.html',context)




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


