from rest_framework import serializers
from imageapp.models import Photo
from PIL import Image
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)
        class Meta:
                model = User

                fields = [ 
                        "username",
                        "email",
                        "first_name",
                        "last_name",
                        "password"
                ]
                # exctra_kwargs  ={"write_only" : True} 
        def create(self,validated_data):
                password=validated_data.pop('password',None)
                instance = self.Meta.model(**validated_data)
                if password is not None:
                        instance.set_password(password)
                instance.save()
                return instance  


class LogSerializers(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField() 
    class Meta:
        model = User
        fields = ['email','password'] 

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        return attrs






class ProfileSerializer(serializers.ModelSerializer):
    thumbnails = serializers.ImageField(required=False , read_only=True)
    medium  = serializers.ImageField()
    large = serializers.ImageField(required=False,read_only=True)
    grayscale = serializers.ImageField(required=False,read_only=True)
    class Meta:
        model = Photo
        fields = ['thumbnails','medium','large','grayscale'] 


    def create(self, validated_data):
        medium = validated_data['medium']
        isinstance = Photo.objects.create(
            thumbnails=medium,
            medium=medium,
            large=medium,
            grayscale=medium
        ) 
        isinstance.save()
        return isinstance
