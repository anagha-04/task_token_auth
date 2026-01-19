from django.shortcuts import render
from user_app.models import *
from user_app.serializers import*
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


# Create your views here.

class UserRegisterView(APIView):

    permission_classes =[AllowAny]

    def post(self,request):

        user_serializer = UserRegisterSerializer(data= request.data)

        if user_serializer.is_valid():

            serializer = user_serializer.save()

            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):

    permission_classes = [IsAuthenticated]

    authentication_classes =[BasicAuthentication]

    def post(self,request):

        user = request.user

        token,created = Token.objects.get_or_create(user = user)

        return Response({"message":"loginsucess","token":token.key},status=status.HTTP_200_OK)
    
    
class AddpersonalView(APIView):

    authentication_classes =[TokenAuthentication]

    permission_classes =[IsAuthenticated]

    def post(self,request):

        serializer = PersonalSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user =request.user)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):

        data =PersonalModel.objects.filter(user =request.user)

        serializer = PersonalSerializer(data,many =True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

class RetriveUpdateDelete(APIView):

    permission_classes =[IsAuthenticated]

    authentication_classes =[TokenAuthentication]

    def get(self,request,**kwargs):

        id = kwargs.get('pk')

        personal = get_object_or_404(PersonalModel,id=id,user= request.user)

        serializer = PersonalSerializer(personal,many= False)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,**kwargs):

        id = kwargs.get('pk')

        personal = get_object_or_404(PersonalModel,id=id,user= request.user)

        serializer = PersonalSerializer(personal,data= request.data )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,**kwargs):

        id= kwargs.get('pk')

        personal = get_object_or_404(PersonalModel,id= id)

        personal.delete()

        return Response({"message":"deleted"},status=status.HTTP_200_OK)


        

        