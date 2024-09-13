from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer


class PollList(APIView):
    def get(self, request, format=None):
      questions = Question.objects.all()
      serializer = QuestionSerializer(questions, many=True)
      return Response(serializer.data)
    
    def post(self, request, format=None):
      serializer = QuestionSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PollDetail(APIView):
    def get_object(self, pk):
      try:
        return Question.objects.get(pk=pk)
      except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
      question = self.get_object(pk)
      serializer = QuestionSerializer(question)
      return Response(serializer.data)
    
    def put(self, request, pk, format=None):
      question = self.get_object(pk)
      serializer = QuestionSerializer(question, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
      question = self.get_object(pk)
      question.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


class Results(APIView):
  def get_object(self, pk):
    try:
      return Question.objects.get(pk=pk)
    except Question.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
  def get(self, request, pk, format=None):
    question = self.get_object(pk)
    choices = Choice.objects.filter(question=question)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)


class Vote(APIView):
  def get_object(self, pk):
    try:
      return Choice.objects.get(pk=pk)
    except Choice.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
  def post(self, request, pk, format=None):
    choice = self.get_object(pk)
    choice.votes += 1
    choice.save()
    serializer = ChoiceSerializer(choice)
    return Response(serializer.data)


class ChoiceList(APIView):
  def get(self, request, format=None):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)

class ChoiceDetail(APIView):
  def get_object(self, pk):
    try:
      return Choice.objects.get(pk=pk)
    except Choice.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def get(self, request, choice_id, format=None):
    choice = self.get_object(choice_id)
    serializer = ChoiceSerializer(choice)
    return Response(serializer.data)