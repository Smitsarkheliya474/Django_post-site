from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import NewSite
from django.urls import reverse

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({},request))

"""def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({},request))"""

def insertdata(request):
    a = request.POST['title']
    b = request.POST['description']
    c = request.POST['author']
    inst = NewSite(title = a, description = b, author = c)  
    inst.save()
    return HttpResponseRedirect(reverse("newpost"))

def showall(request):
    return render(request,"data.html")

def newpost(request): 
    template = loader.get_template("index.html")
    return HttpResponse(template.render({},request))
    
'''def showall(request):
    details = NewSite.objects.all().order_by('-id').values()
    template = loader.get_template('data.html')
    context = {
        'details' : details
    }
    return HttpResponse(template.render(context, request))'''

'''def searchbar(request):
    if request.method =='GET':
        sch = request.GET.get('sch')
        if sch:
            other_items = NewSite.objects.filter(author=sch)
            return render(request,"search.html",{'other_items':other_items})
        else:
            print("")
            return render(request,"search.html",{''})'''

def showall(request):
    latest_item = NewSite.objects.latest('datetime')
    other_items = NewSite.objects.exclude(title=latest_item.title).order_by('-id')
    context = {
        'latest_item': latest_item,
        'other_items': other_items
    }
    return render(request, 'data.html', context)

def searchbar(request):
    query = request.GET.get('q')
    results = NewSite.objects.filter(author=query) if query else []
    return render(request, 'search.html', {'results': results})  

def my_view(request):
    my_model_instances = NewSite.objects.all()
    tags = []
    for instance in my_model_instances:
        tag = f"{instance.title}"   
        tags.append(tag)
    return render(request, 'home.html', {'tags': tags})
    
    