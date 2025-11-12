from tkinter.font import names

from django.urls import path
from . import views

from pages.urls import urlpatterns

urlpatterns=[
    path('signup/', views.SignUpView.as_view(), name= 'signup')
]