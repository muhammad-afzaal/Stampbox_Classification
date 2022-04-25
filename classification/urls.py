from django.contrib import admin
from django.urls import re_path
from classification.views import ClassificationView


urlpatterns = [
    re_path(r'^suggestion/classification/', ClassificationView.as_view())
]
