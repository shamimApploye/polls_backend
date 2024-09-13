from rest_framework import serializers
from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='question.id', read_only=True)

    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes', 'question_id']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question
