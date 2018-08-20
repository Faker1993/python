from django.shortcuts import render,redirect
from django.http import HttpResponse
from super.models import Item

# Create your views here.


def index(request):
    return render(request, 'index.html')


def home_page(request):
    if request.method == "POST":
        print(request.POST.get('item_text'))
        Item.objects.create(text=request.POST.get('item_text'))
#        item = Item.objects.first()
#        print(item.text)
        return redirect('/')
#    Item.objects.create(text='item1')
#
    #     Item.objects.create(text='item2')
    items = Item.objects.all()
    return render(request, 'home_page.html', {'items': items})