"""socialgreen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views
from apps.core.views import frontpage, signup
from apps.feed.views import feed, search
from apps.chat.views import chats, chat
from apps.socialgreenprofile.views import socialgreenprofile, follow_planter, unfollow_planter, followers, follows, edit_profile
from apps.chat.api import api_add_message
from apps.feed.api import api_add_leaf, api_add_like

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),
    path('api/add_leaf/', api_add_leaf, name='api_add_leaf'),
    path('api/add_like/', api_add_like, name='api_add_like'),
    path('u/<str:username>/', socialgreenprofile, name="socialgreenprofile"),
    path('u/<str:username>/followers/', followers, name="followers"),
    path('u/<str:username>/follows/', follows, name="follows"),
    path('u/<str:username>/follow/', follow_planter, name="follow_planter"),
    path('u/<str:username>/unfollow/', unfollow_planter, name="unfollow_planter"),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('chats/<int:user_id>/', chat, name="chat"),
    path('chats/', chats, name="chats"),
    path('api/add_message/', api_add_message, name='api_add_message'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
