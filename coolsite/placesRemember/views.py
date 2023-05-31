from allauth.account.views import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Remember
from .forms import RememberModels
import folium
import geocoder


def index(request):
    return render(request, 'placesRemember/auth.html')


def remember(request):
    remembers = Remember.objects.all()
    return render(request, 'placesRemember/remember.html', {'remembers': remembers})


def logout_view(request):
    logout(request)
    return redirect('home')


def add_remember(request):
    if request.method == 'POST':
        form = RememberModels(request.POST)
        if form.is_valid():
            form.save()
            return redirect('remember')
    else:
        form = RememberModels()
    address = RememberModels.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')
    # Create Map Object
    m = folium.Map(location=[10, 10], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': RememberModels,
    }
    return render(request, 'placesRemember/add_remember.html', context)