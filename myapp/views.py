from django.shortcuts import render
from .forms import TextForm


def search(request):
    return render(request, "myapp/search.html", {})


def firstview(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            return render(request, "myapp/result.html", {'data': form.cleaned_data['name']})
    else:
        form = TextForm()
        return render(request, 'myapp/template.html', {'form': form})


def idtest(request, id):
    id = 59;
    return render(request, 'myapp/idtest.html', {'id': id})

