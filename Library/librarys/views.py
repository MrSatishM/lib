from django.shortcuts import render,redirect
from librarys.models import Library1

# Create your views here.
def home(request):
    content = {}
    content['data'] = Library1.objects.all()
    return render(request,'library/index.html',content)

def add(request):
    if(request.method=="POST"):
        book_ = request.POST['book']
        author_ = request.POST['author']
        price_ = request.POST['price']
        page_ = request.POST['page']
        publication_ = request.POST['publication']
        category_ = request.POST['category']
        insert_data = Library1.objects.create(book= book_, author= author_, price= price_, pages= page_, publication= publication_,category= category_,is_deleted= "n")
        insert_data.save()
        return redirect("/")
    return render(request,'library/add.html')

def delete(request,tid):
    record_deleted=Library1.objects.filter(id=tid)
    record_deleted.delete()
    return redirect("/")

def update(request,tid):
    if(request.method=="POST"):
        book_ = request.POST['book']
        author_ = request.POST['author']
        price_ = request.POST['price']
        page_ = request.POST['page']
        publication_ = request.POST['publication']
        category_ = request.POST['category']
        record_to_be_update = Library1.objects.filter(id=tid)
        record_to_be_update.update(book= book_, author= author_, price= price_, pages= page_, publication= publication_,category= category_,is_deleted= "n")
        return redirect("/")
    else:
        content={}
        content['data']= Library1.objects.get(id=tid)
        return render(request,'library/update.html',content)

def pricehtol(request):
    content = {}
    content['data'] =Library1.objects.order_by('-price')
    return render(request,'library/index.html',content)

def priceltoh(request):
    content = {}
    content['data'] =Library1.objects.order_by('price')
    return render(request,'library/index.html',content)

def authoratoz(request):
    content = {}
    content['data'] =Library1.objects.order_by('-author')
    return render(request,'library/index.html',content)

def authorztoa(request):
    content = {}
    content['data'] =Library1.objects.order_by('author')
    return render(request,'library/index.html',content)

def nonfiction(request):
    content = {}
    content['data'] =Library1.objects.filter(category='non_fiction')
    return render(request,'library/index.html',content)

def fiction(request):
    content = {}
    content['data'] =Library1.objects.filter(category='fiction')
    return render(request,'library/index.html',content)

def edited(request):
    content = {}
    content['data'] =Library1.objects.filter(category='edited')
    return render(request,'library/index.html',content)

def reference(request):
    content = {}
    content['data'] =Library1.objects.filter(category='reference')
    return render(request,'library/index.html',content)
