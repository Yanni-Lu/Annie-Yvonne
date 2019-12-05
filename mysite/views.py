from django.shortcuts import render
from .models import Squirrel
def all_squirrels(request):
    s = Squirrel.objects.all()
    context = {
            'squirrels': s,
            }
    return render(request,'mysite/sightings.html',context)

def squirrel_detail(request,unique_squirrel_id):
    s = Squirrel.objects.get(Unique_Squirrel_ID=unique_squirrel_id)
    return HttpResponse("Hi,I'm squirrel")

def map(request):
    sightings = Squirrel.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'mysite/map.html',context)
    
