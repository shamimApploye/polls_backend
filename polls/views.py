from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer

@api_view(['GET', 'POST'])
def poll_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def poll_detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def results(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    choices = Choice.objects.filter(question=question)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def vote(request, pk):
    try:
        choice = Choice.objects.get(pk=pk)
    except Choice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    choice.votes += 1
    choice.save()
    serializer = ChoiceSerializer(choice)
    return Response(serializer.data)

@api_view(['GET'])
def choices_list(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    choices = Choice.objects.filter(question=question)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def choice_detail(request, choice_id):
    try:
        choice = Choice.objects.get(pk=choice_id)
    except Choice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ChoiceSerializer(choice)
    return Response(serializer.data)