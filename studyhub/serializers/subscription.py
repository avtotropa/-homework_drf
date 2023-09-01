from rest_framework import serializers

from studyhub.models import Subscription


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
