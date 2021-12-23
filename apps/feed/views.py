from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Leaf

# Create your views here.


@login_required
def feed(request):
    userids = [request.user.id]

    for planter in request.user.socialgreenprofile.follows.all():
        userids.append(planter.user.id)

    leafs = Leaf.objects.filter(created_by_id__in=userids)

    for leaf in leafs:
        likes = leaf.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            leaf.liked = True
        else:
            leaf.liked = False

    return render(request, 'feed/feed.html', {'leafs': leafs})


@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        planters = User.objects.filter(username__icontains=query)
        leafs = Leaf.objects.filter(body__icontains=query)
    else:
        planters = []
        leafs = []

    context = {
        'query': query,
        'planters': planters,
        'leafs': leafs
    }

    return render(request, 'feed/search.html', context)
