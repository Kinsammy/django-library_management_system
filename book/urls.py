from django.urls import path
from . import views
urlpatterns = [
    path('email/', views.playground),
    path('mail/', views.send_email),
    path('template/', views.send_with_template)
]