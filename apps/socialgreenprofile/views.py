from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SocialgreenProfileForm

# Create your views here.


def socialgreenprofile(request, username):
    user = get_object_or_404(User, username=username)

    leafs = user.leafs.all()

    for leaf in leafs:
        likes = leaf.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            leaf.liked = True
        else:
            leaf.liked = False

    context = {
        'user': user,
        'leafs': leafs
    }

    return render(request, 'socialgreenprofile/socialgreenprofile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = SocialgreenProfileForm(
            request.POST, request.FILES, instance=request.user.socialgreenprofile)

        if form.is_valid():
            form.save()

            return redirect('socialgreenprofile', username=request.user.username)
    else:
        form = SocialgreenProfileForm(instance=request.user.socialgreenprofile)

    context = {
        'user': request.user,
        'form': form
    }

    return render(request, 'socialgreenprofile/edit_profile.html', context)


@login_required
def follow_planter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.socialgreenprofile.follows.add(user.socialgreenprofile)

    return redirect('socialgreenprofile', username=username)


@login_required
def unfollow_planter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.socialgreenprofile.follows.remove(user.socialgreenprofile)

    return redirect('socialgreenprofile', username=username)


def followers(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'socialgreenprofile/followers.html', {'user': user})


def follows(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'socialgreenprofile/follows.html', {'user': user})
