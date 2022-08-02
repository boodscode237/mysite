from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import ItemForm
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    path_ = 'food/index.html'
    return render(request, path_, context)
    # return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    path_ = 'food/detail.html'
    return render(request, path_, context)


def create_item(request):
    form = ItemForm(request.POST or None)
    path_ = 'food/item-form.html'
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, path_, {'form':form})

def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    path_ = 'food/item-form.html'
    return render(request, path_, {'form': form, 'item': item})



