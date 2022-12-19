from django.urls import path 
from imageapp import views 
from imageapp.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView


router = DefaultRouter()
router.register('register',views.RegisterViewset,basename='register')


urlpatterns = [
    path('upload-image/',views.ImageUploadView.as_view()),
    path('list/',views.ImageUploadView.as_view()),
    path('login/',LoginAPIView.as_view()),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/',LogoutApiview.as_view()),
    
]+router.urls
