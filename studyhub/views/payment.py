import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from studyhub.models import Payment, Course, Lesson
from studyhub.serializers.payment import PaymentSerializer, PaymentCreateSerializer
from users.models import User


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_fields = ['date_of_payment']
    permission_classes = [IsAuthenticated]


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        stripe.api_key = settings.DJANGO_STRIPE_API_KEY

        user_id = request.data.get('user_id')
        course_id = request.data.get('course_id')
        lesson_id = request.data.get('lesson_id')
        payment_amount = request.data.get('payment_amount')

        user = User.objects.get(pk=user_id)

        if course_id:
            paid_course = Course.objects.get(pk=course_id)
            payment_intent_description = f'Оплата курса: {paid_course.name}'

        elif lesson_id:
            paid_lesson = Lesson.objects.get(pk=lesson_id)
            payment_intent_description = f'Оплата урока: {paid_lesson.name}'
        else:
            return Response({'error': 'Должен быть указан либо Курс, либо Урок'}, status=400)

        payment_intent = stripe.PaymentIntent.create(
            amount=payment_amount,
            currency='usd',
            description=payment_intent_description,
        )

        payment = Payment.objects.create(
            user=user,
            paid_course=paid_course if course_id else None,
            paid_lesson=paid_lesson if lesson_id else None,
            payment_amount=payment_amount,
            payment_intent_id=payment_intent.id,
        )

        serializer = self.get_serializer(payment)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
