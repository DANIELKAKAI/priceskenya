from django.shortcuts import render
from .forms import TextForm
from finalapp.reader import *


def firstview(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name'].replace(" ", "+");request.session['item'] = data
            a = jumia_reader(data);
            b = kili_reader(data);
            c = masoko_reader(data);
            d = pigia_reader(data);
            return render(request, "finalapp/finaldesign.html",{'jdata': a[:4], 'kdata': b[:4], 'mdata': c[:4], 'pdata': d[:4]})
    else:
        form = TextForm()
        return render(request, 'finalapp/bar2.html', {'form': form})


def secondview(request):
    data = request.session.get('item')
    a = front_reader(data)
    return render(request, "finalapp/page2.html", {'fdata': a[:4]})

def contacts(request):
    return render(request,"finalapp/contacts.html",{})

def about(request):
    return render(request,"finalapp/about.html",{})
