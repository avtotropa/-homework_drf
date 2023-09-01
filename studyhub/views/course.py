from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from studyhub.models import Course
from studyhub.paginator import CoursePaginator
from studyhub.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator
    # permission_classes = [IsAuthenticated]
