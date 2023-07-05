from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, GetQuestionSerializer, GetQuizSerializer


class QuizViewSet(ModelViewSet):
      queryset = Quiz.objects.all()
      serializer_class = QuizSerializer

      def get_serializer_class(self):
            if self.request.method == 'GET':
                  return GetQuizSerializer
            return QuizSerializer

class QuestionViewSet(ModelViewSet):
      queryset = Question.objects.all()
      serializer_class = QuestionSerializer

      def get_serializer_class(self):
            if self.request.method == 'GET':
                  return GetQuestionSerializer
            return QuestionSerializer


class AnswerViewSet(ModelViewSet):
      queryset = Answer.objects.all()
      serializer_class = AnswerSerializer



