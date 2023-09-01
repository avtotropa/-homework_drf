from rest_framework import generics

from studyhub.serializers.subscription import SubscribeSerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
