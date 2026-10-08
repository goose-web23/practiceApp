from django.urls import path
from django.http import HttpResponse


def placeholder(request):
    return HttpResponse("practices placeholder OK")


urlpatterns = [
    path('', placeholder, name='practices-index'),
    path('test/', placeholder, name='practices-test'),
    path('about/', placeholder, name='practices-about'),
]