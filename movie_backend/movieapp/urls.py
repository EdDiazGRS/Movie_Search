from django.urls import path, include
from .models import Movie
from .views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('',include(router.urls))

]