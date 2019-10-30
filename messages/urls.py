from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>', views.chat),
    path('', views.chat),
    path('message/new', views.add_message)
]