from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/todos/', include('todo.urls')),  # Make sure this points to your app's URLs
]