from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views
from .API import views as views__API
from rest_framework import routers

router = routers.DefaultRouter()
router.register("comments", views__API.CommentViewSet)


urlpatterns = [
    # common
    # common
    # common
    path("", TemplateView.as_view(template_name="index.html")),
    path("viewContent/", TemplateView.as_view(template_name="viewContent.html")),
    # facts
    # facts
    # facts
    path("facts/", views.facts, name="facts"),
    re_path(r"^facts/delete/(?P<id>\d+)$", views.delete_facts, name="delete_facts"),
    path("facts/search", views.facts_search, name="facts_search"),
    # News and Articles
    # News and Articles
    # News and Articles
    path("newsArticles/", views.newsArticles, name="newsArticles"),
    path("myNewsArticles/", views.myNewsArticles, name="myNewsArticles"),
    re_path(
        r"myNewsArticles/delete/(?P<id>\d+)$",
        views.delete_myNewsArticles,
        name="delete_myNewsArticles",
    ),
    re_path(
        r"^newsArticles/delete/(?P<id>\d+)$",
        views.delete_newsArticles,
        name="delete_newsArticles",
    ),
    path("newsArticles/search", views.newsArticles_search, name="newsArticles_search"),
    path(
        "myNewsArticles/search",
        views.myNewsArticles_search,
        name="myNewsArticles_search",
    ),
    re_path(
        r"^newsArticles/detailed/(?P<id>\d+)$",
        views.newsArticles_detailed,
        name="newsArticles_detailed",
    ),
    re_path(
        r"^newsArticles/addToFavorites/(?P<id>\d+)$",
        views.addToFavorites_NewsArticles,
        name="addToFavorites_NewsArticles",
    ),
    # API
    # API
    # API
    path("API/", include(router.urls)),
]
