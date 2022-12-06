from __future__ import absolute_import
from django.urls import path
from dynamic_search.views import search

urlpatterns = [
    path('search/', search, name='search'),
]


