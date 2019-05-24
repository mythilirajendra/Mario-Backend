from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^mario', include('mario.urls')),
    #url(r'^mario', include('django.contrib.auth.urls')) #

]
