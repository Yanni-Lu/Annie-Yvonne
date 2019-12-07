from django.urls import path
from . import views
urlpatterns = [
    path('sightings/', views.all_squirrels, name='all_squirrels'),
    path('sightings/<unique_squirrel_id>/',views.squirrel_edit, name='squirrel_edit'),
    

]

