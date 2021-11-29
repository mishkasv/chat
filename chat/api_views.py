import datetime
from django.utils import timezone
from rest_framework import viewsets, generics,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User,Messages,GroupChat
from chat import serializers
from .paginations import CustomPagination

@api_view(['POST'])
def update_user_group(request,group):
    group_obj = GroupChat.objects.get(name=group,users=request.user)
    if not group_obj:
        group_obj.users.add(request.user)
        group_obj.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

class MessageChatView(generics.GenericAPIView):
    queryset = Messages.objects.all().prefetch_related('user','group')
    serializer_class = serializers.MessagesChatSerializer
    pagination_class = CustomPagination

    def get(self, request, format=None, *args, **kwargs):
        """
        Return a list of all users.
        """
        group = kwargs['group']
        messages_queryset = self.get_queryset().filter(group__name=group,date_posted__lte=timezone.now()).order_by('-date_posted').all()

        page = self.paginate_queryset(messages_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(messages_queryset, many=True)
        return Response(serializer.data)

class GroupChatViewSet(viewsets.ModelViewSet):
    queryset = GroupChat.objects.all().prefetch_related('users','group_messages','group_messages__user')
    serializer_class = {
        'list':serializers.GroupChatListSerializer,
        'create':serializers.GroupChatCreateSerializer
    }
    default_serializer_class = serializers.GroupChatDetailSerializer
    
    def update(self, request, *args, **kwargs):
        return super(GroupChatViewSet, self).update(request, *args, **kwargs)
    def get_serializer_class(self):
        return self.serializer_class.get(self.action,self.default_serializer_class)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all().prefetch_related('user','group')
    serializer_class = serializers.MessagesSerializer