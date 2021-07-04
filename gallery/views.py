from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Photo,Cartegory, Location
# Create your views here.

def gallery(request):
    date = dt.date.today()
    photo_gallery = Photo.objects.all()
    image_location = Location.objects.all()
    image_category = Cartegory.objects.all()
    
    return render(request,'home.html',{'date':date, 'photo_gallery':photo_gallery})

def past_day_picture(request,past_date):
    # convert data from the string
    try:
        date= date.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise a 404 error when value error is thrown
        raise Http404
        assert False
    if date == dt.date.today():
        return redirect(gallery)
    return render(request,'past_photos.html',{'date':date})
    
    
def search_by_category(request):
    if 'pic' in request.GET and request.GET('pic'):
        search_term = request.GET.get('pic')
        search_image = Photo.search_by_image_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'search_image':search_image})
    
    else:
        message = "You Haven't searched for any Image"
        return render(request,'search.html',{'message':message})
    

def search_results(request):
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get('pic')
        search_image = Cartegory.search_by_category(search_term)
        message = f'{search_term}'
        
        return render(request,'search.html',{'message':message,'search_images':search_image})
    else:
        message = "You Haven't searched for any Image"
        return render(request,'search.html',{'message':message})
    
def photos(request,image_id):
    try:
        image=Photo.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404
    
    return render(request,'photos.html',{'image':image})
