from pymarket.models import Food, Notification
from pymarket.serializers import FoodSerializer, NotificationSerializer
from rest_framework import viewsets

class FoodViewSets(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class NotificationViewSets(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer