from django.urls import path, include
from rest_framework.routers import DefaultRouter


app_name = 'API'

router = DefaultRouter()

urlpatterns = [
    # path('get-token/', get_token_view, name='get_token'),
    path('', include(router.urls)),
]