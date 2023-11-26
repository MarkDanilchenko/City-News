from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import generic
from fuzzywuzzy import fuzz, process
from . import forms, models
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


# registration
# registration
# registration
def registration(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            userLogIn = authenticate(username=username, password=password)
            login(request, userLogIn)
            return redirect("/")
    else:
        form = forms.UserForm()
    return render(request, "registration/registration.html", {"form": form})


# Facts functions
# Facts functions
# Facts functions
def facts(request):
    result = models.Fact.objects.all().order_by('title')
    return render(request, "facts.html", {"result": result})
# class FactListView(generic.ListView):
#     model = models.Fact
#     paginate_by = 3


@staff_member_required
def delete_facts(request, id):
    try:
        if models.Fact.objects.get(id=id):
            models.Fact.objects.get(id=id).delete()
            result = models.Fact.objects.all()
            return render(request, "facts.html", {"result": result})
        else:
            raise Exception
    except:
        result = models.Fact.objects.all()
        return render(request, "facts.html", {"result": result})


def facts_search(request):
    try:
        searchFact = request.POST.get("searchFact")
        if len(searchFact) == 0:
            raise Exception
        else:
            result = models.Fact.objects.values_list()
            for i in models.Fact.objects.values_list():
                for j in list(i):
                    if fuzz.partial_ratio(searchFact, str(j)) > 60:
                        break
                else:
                    result = result.exclude(id=i[0])
            else:
                if len(result) == 0:
                    return render(
                        request, "facts.html", {"resultNotCorrect": "No facts found"}
                    )
                return render(request, "facts.html", {"result": result.values()})
    except:
        result = models.Fact.objects.all()
        return render(request, "facts.html", {"result": result})


# News Articles functions
# News Articles functions
# News Articles functions
def newsArticles(request):
    result = models.NewsArticles.objects.all()
    return render(request, "newsArticles.html", {"result": result})


@login_required
def myNewsArticles(request):
    result = models.SavedArticles.objects.filter(user=request.user)
    return render(request, "myNewsArticles.html", {"result": result})


@staff_member_required
def delete_newsArticles(request, id):
    try:
        if models.NewsArticles.objects.get(id=id):
            models.NewsArticles.objects.get(id=id).delete()
            result = models.NewsArticles.objects.all()
            return render(request, "newsArticles.html", {"result": result})
        else:
            raise Exception
    except:
        result = models.NewsArticles.objects.all()
        return render(request, "newsArticles.html", {"result": result})


def delete_myNewsArticles(request, id):
    try:
        if models.SavedArticles.objects.get(id=id):
            models.SavedArticles.objects.get(id=id).delete()
            result = models.SavedArticles.objects.filter(user=request.user)
            return render(request, "myNewsArticles.html", {"result": result})
        else:
            raise Exception
    except:
        result = models.SavedArticles.objects.filter(user=request.user)
        return render(request, "myNewsArticles.html", {"result": result})


def newsArticles_search(request):
    try:
        searchNewsArticle = request.POST.get("searchNewsArticles")
        if len(searchNewsArticle) == 0:
            raise Exception
        else:
            result = models.NewsArticles.objects.values_list()
            for i in result:
                for j in list(i):
                    if fuzz.partial_ratio(searchNewsArticle, str(j)) > 60:
                        break
                else:
                    result = result.exclude(id=i[0])
            else:
                if len(result) == 0:
                    return render(
                        request,
                        "newsArticles.html",
                        {"resultNotCorrect": "No articles found"},
                    )
                return render(request, "newsArticles.html", {"result": result.values()})
    except:
        result = models.NewsArticles.objects.all()
        return render(request, "newsArticles.html", {"result": result})


def myNewsArticles_search(request):
    try:
        searchNewsArticle = request.POST.get("searchNewsArticles")
        if len(searchNewsArticle) == 0:
            raise Exception
        else:
            result = models.SavedArticles.objects.filter(user=request.user)
            for i in result:
                if (
                    (fuzz.partial_ratio(searchNewsArticle, str(i.article.title)) > 60)
                    or (
                        fuzz.partial_ratio(
                            searchNewsArticle, str(i.article.description)
                        )
                        > 60
                    )
                    or (
                        fuzz.partial_ratio(searchNewsArticle, str(i.article.author))
                        > 60
                    )
                    or (fuzz.partial_ratio(searchNewsArticle, str(i.article.tags)) > 60)
                    or (
                        fuzz.partial_ratio(
                            searchNewsArticle, str(i.article.publish_date)
                        )
                        > 60
                    )
                ):
                    continue
                else:
                    result = result.exclude(id=i.id)
            else:
                if len(result) == 0:
                    return render(
                        request,
                        "myNewsArticles.html",
                        {"resultNotCorrect": "No articles found"},
                    )
                return render(request, "myNewsArticles.html", {"result": result})

    except:
        result = models.SavedArticles.objects.filter(user=request.user)
        return render(request, "myNewsArticles.html", {"result": result})


def newsArticles_detailed(request, id):
    try:
        result = models.NewsArticles.objects.get(id=id)
        commentsCount = models.Comment.objects.filter(article__id=id).count()
        return render(
            request,
            "newsArticlesDetailed.html",
            {"result": result, "commentsCount": commentsCount},
        )
    except:
        result = models.NewsArticles.objects.all()
        return render(request, "newsArticles.html", {"result": result})

@login_required
def addToFavorites_NewsArticles(request, id):
    try:
        article = models.NewsArticles.objects.get(id=id)
        if models.SavedArticles.objects.filter(user=request.user, article=article):
            pass
        else:
            models.SavedArticles.objects.create(user=request.user, article=article)
        return redirect(f"/newsArticles/detailed/{id}")
    except:
        return redirect(f"/newsArticles/detailed/{id}")
