from django.conf.urls import url
from . import views

app_name = "mario"

urlpatterns = [
    url(r'^', views.signup_view, name='signup')
]

