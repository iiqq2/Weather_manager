from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from wsite.serializers import *
from wsite.models import *
from wsite.services import *



class UserCollectionView(APIView):
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return User.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCollectionViewDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, link):
        user = User.objects.get(link=link)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, link):
        try:
            user = User.objects.get(link=link)
            user.delete()
            return HttpResponse(status=204)
        except City.DoesNotExist:
            return HttpResponse(status=404)


class CityCollectionView(APIView):
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return City.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityCollectionViewDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, name):
        city = City.objects.get(name=name)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def delete(self, request, name):
        try:
            city = City.objects.get(name=name)
            city.delete()
            return HttpResponse(status=204)
        except City.DoesNotExist:
            return HttpResponse(status=404)


class SubCollectionView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        subs = Subscriptions.objects.all()
        ser = SubSerializer(subs, many=True)
        return Response(ser.data)

    def post(self, request):
        serializer = SubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_city = serializer.data["city_name"]
            create_city(new_city)
            user = User.objects.get(username=serializer.data["user_name"])
            schedule_email(time=serializer.data["time"], email=user.email, city=serializer.data["city_name"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)