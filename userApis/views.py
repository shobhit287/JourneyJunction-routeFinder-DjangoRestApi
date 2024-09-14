from django.http import JsonResponse
from rest_framework.views import APIView
from . import service
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .serializers import UserSerializer
from . import service

class User(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: openapi.Response(
                description="User created successfully",
                schema=UserSerializer
            ),
            400: openapi.Response(
                description="Bad request"
            )
        }
    )
    def post(self, request):
        payload = request.data
        if payload:
            response = service.createUser(payload)
            return response
        else:
            return JsonResponse({"error": "Please send valid data."}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="User details or list of users",
                schema=UserSerializer(many=True)
            ),
            404: openapi.Response(
                description="User not found"
            )
        }
    )
    def get(self, request, id=None):
        if id:
            response = service.findOne(id)
            return response
        else:
            response = service.findAll()
            return response

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            200: openapi.Response(
                description="User updated successfully",
                schema=UserSerializer
            ),
            400: openapi.Response(
                description="Bad request"
            )
        }
    )
    def patch(self, request, id=None):
        if id and request.data:
            response = service.updateOne(id, request.data)
            return response
        else:
            return JsonResponse({"error": "UserId is missing or data is not provided"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(
                description="User deleted successfully"
            ),
            400: openapi.Response(
                description="Bad request"
            )
        }
    )
    def delete(self, request, id=None):
        if id:
            response = service.delete(id)
            return response
        else:
            return JsonResponse({"error": "UserId is missing"}, status=status.HTTP_400_BAD_REQUEST)

class ChangeUserPassword(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD),
                'oldPassword': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            },
            required=['password','oldPassword']
        ),
        responses={
            200: openapi.Response(
                description="Password changed successfully"
            ),
            400: openapi.Response(
                description="Bad request"
            )
        }
    )
    def post(self, request, id=None):
        if request.data and id:
            response = service.changePassword(id, request.data)
            return response
        else:
            return JsonResponse({"error": "Data or user id is missing"}, status=status.HTTP_400_BAD_REQUEST)
