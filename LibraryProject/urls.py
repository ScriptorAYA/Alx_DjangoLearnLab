from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LibraryProject.relationship_app.urls')),  # points to your app's urls.py
]
