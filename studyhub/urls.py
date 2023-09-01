from django.urls import path
from rest_framework import routers

from studyhub.views.course import *
from studyhub.views.lesson import *
from studyhub.views.payment import PaymentListView
from studyhub.views.subscription import SubscriptionCreateAPIView

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson-list'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('create/', LessonCreateView.as_view(), name='lesson-create'),
    path('<int:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),
    path('<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),

    # payment
    path('payment/', PaymentListView.as_view(), name='payment-list'),

    # subscription
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription-list'),
] + router.urls
