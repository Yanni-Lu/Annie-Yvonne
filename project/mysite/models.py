from django.db import models

class Squirrel(models.Model):
    X = models.FloatField(
            max_digits = 15,
            decimal_places = 13,
            )
    Y = models.FloatField(
            max_digits = 15,
            decimal_places = 13,
            )
    Unique_Squirrel_ID = models.CharField(
            max_length=20,
            default = None,
            primary_key = True,
            )
    Hectare = models.CharField(
            max_length=3,
            default = None,
            )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES=(
            (AM,'AM'),
            (PM,'PM'),
            )

    Shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
            )
    Date = models.CharField(
            max_length=20,
            default = None,
            )

    Hectare_Squirrel_Number = models.IntegerField(
            default=0,
            blank = True,
            )

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    ? = '?'

    AGE_CHOICES=(
            (Adult,'Adult'),
            (Juvenile,'Juvenile'),
            (?,'?')
            )
    Age = models.CharField(
            max_length=16,
            choices=AGE_CHOICES,
            default = None,
            blank = True,
            )

    Primary_Fur_Color = models.CharField(
            max_length=15,
            default = None,
            blank = True,
            )

    Highlight_Fur_Color = models.CharField(
            max_length=20,
            default = None,
            blank = True,
            )

    Combination_of_Primary_and_Highlight_Color = models.CharField(
            max_length=20,
            default = None,
            blank = True,
            )

    Color_Notes = models.CharField(
            max_length=100,
            default=None,
            blank = True,
            )

    Ground_Plane='Ground Plane'
    Above_Ground='Above Ground'
    LOCATION_CHOICES=(
            (Ground_Plane,'Ground Plane'),
            (Above_Ground,'Above Ground'),
            )
    
    Location = models.CharField(
            max_length=20,
            choices=LOCATION_CHOICES,
            default = None,
            blank = True,
            )

    Above_Ground_Sighter_Measurement = models.CharField(
            max_length=10,
            default=None,
            blank=True,
            )

    Specific_Location = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )
    
    Running = models.BooleanField(default=None,)

    Chasing = models.BooleanField(default=None,)
   
    Climbing = models.BooleanField(default=None,)
    
    Eating = models.BooleanField(default=None,)

    Foraging = models.BooleanField(default=None,)

    Other_activities = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    Kuks = models.BooleanField(default=None,)

    Quaas = models.BooleanField(default=None,)
    
    Moans = models.BooleanField(default=None,)
    
    Tail_Flags = models.BooleanField(default=None,)
    
    Tail_Twitches = models.BooleanField(default=None,)
    
    Approaches = models.BooleanField(default=None,)

    Indifferent = models.BooleanField(default=None,)

    Runs_from  = models.BooleanField(default=None,)

    Other_Activities = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    Lat/Long = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    Zip_Code = models.CharField(
            max_length=100,
            default=None,
            blank=True,
            )

    Community_Districts = models.IntegerField(
            default=None,
            blank = True,
            )

    Borough_Boundaries = models.IntegerField(
            default=None,
            blank = True,
            )

    City_Council_Districts = models.IntegerField(
            default=None,
            blank = True,
            )

    Police Precincts = models.IntegerField(
            default=None,
            blank = True,
            )

    def __str__(self):
        return self.Unique_Squirrel_ID


