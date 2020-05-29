from django.shortcuts import render, redirect
from .models import List
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ListForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    return render(request, 'about.html', {})

def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    return redirect('home')

def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return redirect('home')