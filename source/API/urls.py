from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet, get_token_view

app_name = 'API'

router = DefaultRouter()
router.register('quote', QuoteViewSet, basename='quote')

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('', include(router.urls)),
]

