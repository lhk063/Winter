from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<ink:pk>',posting, name="posting"),
]