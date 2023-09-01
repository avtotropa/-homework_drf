from django.urls import path
from rest_framework import routers

from studyhub.apps import StudyhubConfig
from studyhub.views.course import *
from studyhub.views.lesson import *
from studyhub.views.payment import PaymentListAPIView, PaymentCreateAPIView

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)

app_name = StudyhubConfig.name

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson-list'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('create/', LessonCreateView.as_view(), name='lesson-create'),
    path('<int:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),
    path('<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),

    # payment
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create')
] + router.urls
