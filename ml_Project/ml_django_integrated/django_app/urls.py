from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='INDEX'),
    path("predict/", views.predict_datapoint, name='PREDICTION'),
]


