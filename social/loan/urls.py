from django.urls import path, include
from .views import index, rules, display_rules

urlpatterns = [
    path('home/', index, name='home'),
    path('rules/', display_rules, name='display_rules'),
    path('rules/<int:id>/', rules, name='rules'),
]
