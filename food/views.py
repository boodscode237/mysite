from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


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

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    path_ = 'food/detail.html'
    return render(request, path_, context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)
    path_ = 'food/item-form.html'
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, path_, {'form':form})

# class based view for create item

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']

    template_name = 'food/item-form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    path_ = 'food/item-form.html'
    return render(request, path_, {'form': form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    context = {'item': item}
    path_ = 'food/item-delete.html'
    return render(request, path_, context)


