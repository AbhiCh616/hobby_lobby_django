from django.urls import path
from accounts.api.views import(
    UserCreate
)

urlpatterns = [
    path('create/', UserCreate.as_view(), name='create'),
]