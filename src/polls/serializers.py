from rest_framework import serializers

from .models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    # unable to resolve type hint for function "was_published_recently". Consider using a type hint or @extend_schema_field. Defaulting to string.
    was_published_recently: bool

    class Meta:
        model = Choice
        fields = ["id", "choice_text", "votes", "question"]
        read_only_fields = ["votes"]


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "question_text", "pub_date", "was_published_recently", "choice_set"]
