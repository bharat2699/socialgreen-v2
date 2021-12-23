import json


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


from .models import Leaf, Like


@login_required
def api_add_leaf(request):
    data = json.loads(request.body)
    body = data['body']

    leaf = Leaf.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})


@login_required
def api_add_like(request):
    data = json.loads(request.body)
    leaf_id = data['leaf_id']

    if not Like.objects.filter(leaf_id=leaf_id).filter(created_by=request.user).exists():
        like = Like.objects.create(leaf_id=leaf_id, created_by=request.user)

    return JsonResponse({'success': True})
