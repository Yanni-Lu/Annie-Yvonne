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

def squirrel_add(request, add_web = 'mysite/add.html'):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'mysite/notice.html')
    else:
        form = SquirrelForm()
    
    context = {
            'form':form,
    }

    return render(request, add_web ,context)

def squirrel_stats(request, stats_web = 'mysite/stats.html'):
    total_number = Squirrel.objects.all().count()
    adult = Squirrel.objects.filter(Age="Adult").count()/total_number
    gray_fur = Squirrel.objects.filter(Primary_Fur_Color="Gray").count()/total_number
    above_ground = Squirrel.objects.filter(Location="Above Ground").count()/total_number
    running = Squirrel.objects.filter(Running=True).count()/total_number
    context = {
            'total_number':total_number,
            'adult':adult,
            'gray_fur':gray_fur,
            'above_ground':above_ground,
            'running':running,
    }
    return render(request, stats_web, context)
