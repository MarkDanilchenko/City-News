from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('viewContent/', TemplateView.as_view(template_name="viewContent.html")),
]