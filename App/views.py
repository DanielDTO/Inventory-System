from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Avg,Max,Min
from itertools import chain
from operator import attrgetter

# Create your views here.
def index(request):
    return render(request, 'index.html')

'''.........................DESKTOP SECTION .....................................!!!'''

def get_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktops',
    }
    return render(request, 'index.html', context)

def add_desktop(request):
    if request.method == "POST":
        form = desktopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = desktopForm()
        return render(request, 'add_new.html', {'form': form})

def edit_desktop(request,pk):
    item = get_object_or_404(Desktop, pk=pk)
    if request.method == "POST":
        form = desktopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = desktopForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})

def del_desktop(request,pk):
    Desktop.object.filter(id=pk).delete()

    items = Desktop.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)

'''.........................................LAPTOP SECTION!!!!!.............................'''

def get_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'index.html', context)

def add_laptop(request):
    if request.method == "POST":
        form = laptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = laptopForm()
        return render(request, 'add_new.html', {'form': form})

def edit_laptop(request,pk):
    item = get_object_or_404(Laptop, pk=pk)
    if request.method == "POST":
        form = laptopForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = laptopForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})

def del_laptop(request,pk):
    Laptop.object.filter(id=pk).delete()

    items = Laptop.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)

'''......................................MOBILE SECTION!!!!!....................................'''

def get_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles',
    }
    return render(request, 'index.html', context)

def add_mobile(request):
    if request.method == "POST":
        form = mobileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = mobileForm()
        return render(request, 'add_new.html', {'form': form})

def edit_mobile(request,pk):
    item = get_object_or_404(Mobile, pk=pk)
    if request.method == "POST":
        form = mobileForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = mobileForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def del_mobile(request,pk):
    Mobile.object.filter(id=pk).delete()

    items = Mobile.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)

'''.........................................STATIONARY SECTION!!!.............................'''

def get_stationary(request):
    items = Stationary.objects.all()
    context = {
        'items': items,
        'header': 'Stationary',
    }
    return render(request, 'index.html', context)

def add_stationary(request):
    if request.method == "POST":
        form = stationaryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = stationaryForm()
        return render(request, 'add_new.html', {'form': form})

def edit_stationary(request,pk):
    item = get_object_or_404(Stationary, pk=pk)
    if request.method == "POST":
        form = stationaryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = stationaryForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})



def del_stationary(request,pk):
    Stationary.object.filter(id=pk).delete()

    items = Stationary.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)

def get_all(request):
    desktop = Desktop.objects.filter()
    laptop= Laptop.objects.filter()
    mobile= Mobile.objects.filter()
    stationary= Stationary.objects.filter()
    item_list = sorted(
        chain(desktop, laptop, mobile, stationary),
        key=attrgetter('Date'),
        reverse=True
    )
    context = {
        'items' : item_list,
        'header' : 'All',
    }
    return render(request, 'index.html',context)

#def get_by_price(get_all):
 #   def get_price(request):
  #      if 'min_price' in request.GET:
   #         filter_price1 = request.GET.get('min_price')
    #        filter_price2 = request.GET.get('max_price')
     #       if filter_price1 == '':
      #          filter_price1 =0
       #     elif filter_price2 == '':
        #        filter_price2= All.objects.all().aggregate(Max('Price'))

        