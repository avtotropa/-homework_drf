from rest_framework import serializers

from studyhub.models import Course, Lesson
from studyhub.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons_of_course = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    def get_lessons_of_course(self, obj):
        return LessonSerializer(Lesson.objects.filter(course=obj), many=True).data

    class Meta:
        model = Course
        fields = ('id', 'name', 'lesson_count', 'lessons_of_course')
