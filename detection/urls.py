from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="root"),
    path("detect_image", DetectImage.as_view(), name="image_detect")
]
