from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Image, Location, Category
from django.core.exceptions import ObjectDoesNotExist

def welcome(request):
    '''
    Method to return our images, locations & categories
    '''
    images = Image.objects.all()
    location = Location.objects.all()
    categories = Category.get_all_categories()
    return render(request, 'welcome.html', {"images":images[::-1], "location":location, "categories":categories})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'image': image})

def about(request):
    return render(request, 'about.html')
