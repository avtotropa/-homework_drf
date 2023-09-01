from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from studyhub.models import Lesson
from studyhub.permissions import IsModerator, IsOwner
from studyhub.serializers.lesson import LessonSerializer


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator]


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated, IsOwner]


class LessonDeleteView(DestroyAPIView):
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]
