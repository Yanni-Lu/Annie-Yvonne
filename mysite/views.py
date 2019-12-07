from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Squirrel
from .forms import SquirrelForm


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

def squirrel_edit(request,unique_squirrel_id):
    s = Squirrel.objects.get(Unique_Squirrel_ID = unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = s)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance = s)

    context = {
            'form':form,
            }
    return render(request, 'mysite/edit.html',context)
