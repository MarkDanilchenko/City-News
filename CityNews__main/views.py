from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from fuzzywuzzy import fuzz, process
from . import forms, models
from django.contrib.admin.views.decorators import staff_member_required


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
    return render(request, "registration.html", {"form": form})


# Facts functions
# Facts functions
# Facts functions
def facts(request):
    result = models.Fact.objects.all()
    return render(request, "facts.html", {"result": result})


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
                    if fuzz.partial_ratio(searchFact, str(j)) > 50:
                        break
                else:
                    result = result.exclude(id=i[0])
            else:
                print(f"----->>>>>{result}")
                return render(request, "facts.html", {"result": result.values()})
    except:
        print("Error")
        result = models.Fact.objects.all()
        return render(request, "facts.html", {"result": result})
