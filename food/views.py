from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    items=Item.objects.all()
    template=loader.get_template('food/index.html')
    return HttpResponse(template.render({
        'items':items
    },request))
    # return HttpResponse(items)

def details(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    return render(request,'food/details.html',context)