from rest_framework import serializers
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = ('body', 'author', 'published')
        read_only_fields = ('id', 'published')


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'slug', 'body', 'author', 'answers')
