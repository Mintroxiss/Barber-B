# pylint: disable=E1101
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import WomanService, ManService, KidService
from .serializers import WomanServiceSerializer, ManServiceSerializer, KidServiceSerializer


class IndexPage(TemplateView):
    template_name = 'main_app/index.html'


class WomenPage(TemplateView):
    template_name = 'main_app/women.html'


class WomenPageAPI(APIView):
    def get(self, request, format=None):
        women_services = WomanService.objects.all()
        serializer = WomanServiceSerializer(women_services, many=True)
        return Response(serializer.data)


class MenPage(TemplateView):
    template_name = 'main_app/men.html'


class MenPageAPI(APIView):
    def get(self, request, format=None):
        men_services = ManService.objects.all()
        serializer = ManServiceSerializer(men_services, many=True)
        return Response(serializer.data)


class KidsPage(TemplateView):
    template_name = 'main_app/kids.html'


class KidsPageAPI(APIView):
    def get(self, request, format=None):
        kid_services = KidService.objects.all()
        serializer = KidServiceSerializer(kid_services, many=True)
        return Response(serializer.data)
    


