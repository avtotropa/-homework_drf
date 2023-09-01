from rest_framework import serializers

from studyhub.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'payment_amount', 'paid_course', 'paid_lesson',)
