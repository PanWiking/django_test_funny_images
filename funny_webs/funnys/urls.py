from django.urls import path

from funnys import views

app_name = "funnys"

urlpatterns = [
    path('', views.post_list, name="post_list")
]