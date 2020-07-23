from rest_framework import serializers
from .models import Poll, Question, QuestionType, Answer, User

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'poll']

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, source='q')
    class Meta:
        model = Poll
        fields = ['id', 'name', 'start_date', 'end_date', 'questions']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['poll','question', 'value', 'user']

class UserSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True, source='answer_set')
    class Meta: 
        model = User
        fields = ['id', 'answer']
