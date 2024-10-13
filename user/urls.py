from django.urls import path
from user.views import name, age, hobby

urlpatterns = [
    path('name/', name, name='name'),
    path('age/', age, name='age'),
    path('hobby/', hobby, name='hobby'),
    ]
