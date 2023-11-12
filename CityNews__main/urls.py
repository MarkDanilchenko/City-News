from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('viewContent/', TemplateView.as_view(template_name="viewContent.html")),
    path('facts/', views.facts, name='facts'),
    re_path(r'^facts/delete/(?P<id>\d+)$', views.delete_facts, name='delete_facts'),
    path('facts/search', views.facts_search, name='facts_search'),
]