from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from .serializers import ContactSerializer,BookMeetingSerializer
from rest_framework.mixins import CreateModelMixin
# Create your views here.
class ContactView(APIView,CreateModelMixin):
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
    serializer_class=ContactSerializer
    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=201)
    def perform_create(self, serializer):
        serializer.save()
class BookMeetingView(APIView,CreateModelMixin):
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
    serializer_class=BookMeetingSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    def perform_create(self, serializer):
        serializer.save()