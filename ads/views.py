from django.shortcuts import render
from .models import Ad

# Create your views here.
def ads(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ads.html', {'ads': ads})