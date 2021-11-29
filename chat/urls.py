from django.urls import path, include
from rest_framework import routers
from .api_views import GroupChatViewSet, UserViewSet, MessageViewSet, MessageChatView, update_user_group

router = routers.SimpleRouter()
router.register(r'groups', GroupChatViewSet)
router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)

api_routers = [
    path('', include(router.urls)),
    path('messageschat/<str:group>', MessageChatView.as_view()),
    path('update_groups/<str:group>', update_user_group)
]

from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout', views.logout, name='logout'),
    path('<str:room_name>/', views.room, name='room'),
]