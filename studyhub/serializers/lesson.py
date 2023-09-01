from rest_framework import serializers

from studyhub.models import Lesson
from studyhub.validators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'video',)

        validators = [
            URLValidator(field_name='video'),
        ]
