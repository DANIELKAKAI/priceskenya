
from django.shortcuts import render
from .forms import TextForm
from finalapp.reader import *

def firstview(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name'].replace(" ","+")
            a = jumia_reader(data); b = kili_reader(data);c = masoko_reader(data);
            return render(request, "finalapp/finaldesign.html", {'jdata': a[:4],'kdata': b[:4],'mdata': c[:4]})
    else:
        form = TextForm()
        return render(request, 'finalapp/bar.html', {'form': form})

