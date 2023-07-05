from rest_framework import serializers
from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
      class Meta:
            model = Quiz
            fields = ['id', 'title', 'description', 'date_created']


class QuestionSerializer(serializers.ModelSerializer):
      class Meta:
            model = Question
            fields = ['id', 'question_text', 'date_created']


class AnswerSerializer(serializers.ModelSerializer):
      class Meta:
            model = Answer
            fields = ['id', 'answer_text', 'question', 'is_correct', 'date_created']


class GetQuestionSerializer(serializers.ModelSerializer):
      list_answers = AnswerSerializer(many=True)

      class Meta:
            model = Question
            fields = ['id', 'question_text', 'quiz', 'list_answers']


class GetQuizSerializer(serializers.ModelSerializer):
      quiz_answer = QuestionSerializer(many=True)

      class Meta:
            model = Quiz
            fields = ['id', 'title', 'description', 'date_created', 'quiz_answer']
