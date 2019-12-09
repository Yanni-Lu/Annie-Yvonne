from django.urls import path
from . import views
urlpatterns = [
    path('sightings/', views.all_squirrels),
    path('sightings/add/',views.squirrel_add),
    path('sightings/<unique_squirrel_id>/',views.squirrel_edit),
    path('map/',views.map),

]

