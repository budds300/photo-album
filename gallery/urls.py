from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings

# from django.conf.urls.static import static

urlpatterns = [
    path('',views.gallery, name='gallery'),
    # path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_day_picture,name = 'pastDayPicture'),
    # path('', views.search_by_category,name='search_results'),
    # path('pic/<int:image_id>', views.photos, name = 'photo'),
    url(r'^photo/(\d+)',views.photos,name='photo'),
    url(r'^search/$', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)