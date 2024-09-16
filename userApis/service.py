from .serializers import UserSerializer
from django.http import JsonResponse
from .models import User
from rest_framework import status
from django.contrib.auth.hashers import check_password

def createUser(payload):
    try:
       structuredData = dtoToModel(payload)
       user = UserSerializer(data=structuredData)
       if user.is_valid():
         user.save()
         return JsonResponse({"user":modelToDto(user.data)},status=status.HTTP_201_CREATED)
       else:
            return JsonResponse({"errors": user.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
       return JsonResponse({"error": error}, status=500)
    
def findOne(id):
    try:
       user = User.objects.get(user_id=id)
       userSerializer = UserSerializer(user)
       return JsonResponse({"user":modelToDto(userSerializer.data)},status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
       return JsonResponse({"error": str(error)}, status=500)
    
def findAll():
    try:
       users = User.objects.all()
       usersSerializer = UserSerializer(users, many=True)
       modifiedUsersData= []
       for user in usersSerializer.data:
          modifiedUsersData.append(modelToDto(user)) 
       return JsonResponse({"users":modifiedUsersData},status=status.HTTP_200_OK)
    except Exception as error:
       return JsonResponse({"error": str(error)}, status=500)
    
def updateOne(id, data):
    try:
       user = User.objects.get(user_id=id)
       if 'password' in data:
            data.pop('password')
       userSerializer = UserSerializer(user, data = dtoToModel(data), partial=True)
       if userSerializer.is_valid():
          userSerializer.save()
          return JsonResponse({"users": modelToDto(userSerializer.data)},status=status.HTTP_200_OK)
       else:
            return JsonResponse({"errors": userSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
       return JsonResponse({"error": str(error)}, status=500)
    
def delete(id):
    try:
        user = User.objects.get(user_id=id)
        user.delete()
        return JsonResponse({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return JsonResponse({"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def changePassword(id, data):
    try:
        user = User.objects.get(user_id=id)
        userSerializer = UserSerializer(user)
        if check_password(data["oldPassword"], userSerializer.data['password']): 
           updatePassword = UserSerializer(user, data = dtoToModel(data), partial=True)
           if updatePassword.is_valid():
               updatePassword.save()
               return JsonResponse({"message": "Password changed successfully"}, status=status.HTTP_204_NO_CONTENT)
           else :
               return JsonResponse({"errors": userSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
             return JsonResponse({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)  
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return JsonResponse({"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def dtoToModel(payload):
    model_data = {}
    if "firstName" in payload:
        model_data["first_name"] = payload["firstName"]
    if "lastName" in payload:
        model_data["last_name"] = payload["lastName"]
    if "email" in payload:
        model_data["email"] = payload["email"]
    if "password" in payload:
        model_data["password"] = payload["password"]
    return model_data

def modelToDto(data):     
    return {
        "userId": data["user_id"],
        "firstName": data["first_name"],
        "lastName": data["last_name"],
        "email": data["email"],
        "updatedAt": data["updated_at"],
        "createdAt": data["created_at"],
}