from rest_framework import serializers
from .models import Category, Award, Nominee


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"


class NomineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominee
        fields = "__all__"
