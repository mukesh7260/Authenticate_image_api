from rest_framework.response import Response 
from imageapp.models import Photo
from imageapp.serializers import *
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.conf import settings
User = get_user_model()

# Genereate token manually 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class RegisterViewset(viewsets.ViewSet):
    
    serializer_class=RegisterSerializer
    def create(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user =serializer.save()  
        token = get_tokens_for_user(user) 
        return Response({'token':token,'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

    def list(self,request):
        queryset = User.objects.all()
        serializers = RegisterSerializer(queryset,many=True)
        return Response({'status':200,'payload':serializers.data}) 


class LoginAPIView(APIView):
    serializer_class = LogSerializers
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        token = get_tokens_for_user(user) 
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
            
        return Response({'token':token, 'login':'login has successfully'},status=status.HTTP_200_OK)








class LogoutApiview(APIView):	
	def post(self, request, format = None):
		try:
			refresh_token = request.data.get('refresh_token')
			token_obj = RefreshToken(refresh_token)
			token_obj.blacklist()
			return Response({"message": " Logout successfully"})
		except Exception as e:
			return Response({"message": "token has expired ! plesase take another token !!"})


class ImageUploadView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors) 

    def get(self, request, format= None):
        candidates = Photo.objects.all()
        serializer = ProfileSerializer(candidates,many= True)
        return Response({'status':'success','candidates':serializer.data},status = status.HTTP_200_OK)