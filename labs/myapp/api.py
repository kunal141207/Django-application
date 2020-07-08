from myapp.models import User, ActivityPeriod
from rest_framework import permissions, viewsets
from .serializers import UserSerializer, ActivityPeriodSerializer

#User viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer