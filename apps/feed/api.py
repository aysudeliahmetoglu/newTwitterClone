import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.notification.utilities import create_notification


from .models import Oink,Like
@login_required
def api_add_oink(request):
    data = json.loads(request.body)
    body = data ['body']

    oink = Oink.objects.create(body=body , created_by=request.user)

    return JsonResponse({'success':True})


@login_required
def api_add_like(request):
    data = json.loads(request.body)
    oink_id = data['oink_id']

    if not Like.objects.filter(oink_id=oink_id).filter(created_by=request.user).exists():
        like = Like.objects.create(oink_id=oink_id,created_by=request.user)
        oink=Oink.objects.get(pk=oink_id)
        create_notification(request,oink.created_by,'like')
        
    return JsonResponse({'success':True})    