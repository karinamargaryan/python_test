
from django.shortcuts import  render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from main.models import Product

def index(request):
    products = Product.objects.all().values()
    return render_to_response("index.html",{'products':products}, RequestContext(request))


@csrf_exempt
def insert(request):
    name=request.POST['name']
    model=request.POST['model']
    category=request.POST['category']
    price=request.POST['price']
    status=1
    weight=request.POST['weight']
    product = Product(name=name, model=model,category=category,price=price,status=status,weight=weight)
    product.save()
    return redirect('/')

@csrf_exempt
def update(request):
    id=request.POST['id']
    name = request.POST['name']
    model = request.POST['model']
    category = request.POST['category']
    price = request.POST['price']
    status = 1
    weight = request.POST['weight']
    Product.objects.filter(id=id).update(name=name, model=model, category=category, price=price, status=status, weight=weight)
    return redirect('/')

@csrf_exempt
def delete(request,pk):
    Product.objects.get(id=pk).delete()
    return redirect('/')


