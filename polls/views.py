from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import PollSerializer, QuestionSerializer, QuestionTypeSerializer, AnswerSerializer, UserSerializer
from .models import Poll, Question, QuestionType, Answer, User
from datetime import date

class PollsList(generics.ListAPIView):
    """
    Returns a list of all active polls
    """
    serializer_class = PollSerializer
    
    def get_queryset(self):
        today = date.today()
        return Poll.objects.filter(start_date__lte=today, end_date__gte=today)

class PollCreate(generics.ListCreateAPIView):
    """
    Create poll list all polls
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]
    

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Create poll, list all polls
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(start_date=serializer.instance.start_date)

class QuestionTypeList(generics.ListAPIView):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class AnswerList(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    
class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

