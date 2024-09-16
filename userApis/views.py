from django.http import JsonResponse
from rest_framework.views import APIView
from . import service
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from authApis.jwt import validateJwt
from drf_yasg import openapi
from django.http import JsonResponse
from . import service

class User(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'firstName': openapi.Schema(type=openapi.TYPE_STRING),
                'lastName': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            },
            required=['firstName', 'lastName', 'email', 'password']
        ),
        responses={
            201: openapi.Response(
                description="User Cretaed Successfully"
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
                description="List of users",
            ),
            400: openapi.Response(
                description="Bad request"
            )
        }
    )
    def get(self, request):
        validateToken = validateJwt(request.headers.get('Authorization'))
        if validateToken['status']:
                response = service.findAll()
                return response
        else: 
            return JsonResponse(validateToken,status= validateToken['code'])    

class UserWithId(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="User Details"
            ),
            400: openapi.Response(
                description="Bad request"
            )
        }
    )
    def get(self, request, id=None):
        validateToken = validateJwt(request.headers.get('Authorization'))
        if validateToken['status']:
                response = service.findOne(id)
                return response
        else: 
            return JsonResponse(validateToken,status= validateToken['code'])
        

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'firstName': openapi.Schema(type=openapi.TYPE_STRING),
                'lastName': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL)
            },
        ),
        responses={
            200: openapi.Response(
                description="User Updated Successfully"
            ),
            400: openapi.Response(
                description="Bad request"
            )
        }
    )
    def patch(self, request, id=None):
        validateToken = validateJwt(request.headers.get('Authorization'))
        if validateToken['status']:
            if id and request.data:
                response = service.updateOne(id, request.data)
                return response
            else:
                return JsonResponse({"error": "UserId is missing or data is not provided"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(validateToken,status=validateToken['code']) 

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
        validateToken = validateJwt(request.headers.get('Authorization'))
        if validateToken['status']:
            if id:
                response = service.delete(id)
                return response
            else:
                return JsonResponse({"error": "UserId is missing"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(validateToken,status=status.HTTP_400_BAD_REQUEST)   



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
        validateToken = validateJwt(request.headers.get('Authorization'))
        if validateToken['status']:
            if request.data and id:
                response = service.changePassword(id, request.data)
                return response
            else:
                return JsonResponse({"error": "Data or user id is missing"}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(validateToken, status = validateToken['code']) 
    

