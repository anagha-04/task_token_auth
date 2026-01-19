from rest_framework import serializers

from user_app.models import *

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields =['username','password','email']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email = validated_data['email']
        )
        return user
    
class PersonalSerializer(serializers.ModelSerializer):

    class  Meta:

        model = PersonalModel

        exclude =('user',)
