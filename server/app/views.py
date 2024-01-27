from rest_framework import generics
from .models import Category, Award, Nominee
from .serializers import CategorySerializer, AwardSerializer, NomineeSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AwardList(generics.ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class AwardDetail(generics.RetrieveAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class NomineeCreate(generics.CreateAPIView):
    queryset = Nominee.objects.all()
    serializer_class = NomineeSerializer
