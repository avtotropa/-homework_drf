from rest_framework.viewsets import ModelViewSet

from studyhub.models import Course
from studyhub.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
