from django.contrib import admin
from django.urls import include, path
from users.views import index

urlpatterns = [
    path('users/', include('users.urls')),
    path('chat/', include('messages.urls')),
    path('admin/', admin.site.urls),
]