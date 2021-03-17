from django.db import models

class day(models.Model):
    date = models.DateTimeField(auto_now="true")
    cycle_day = models.IntegerField(default=0)
    deads = models.IntegerField(default=0)
    selection = models.IntegerField(default=0)
    daily_mortality_rate = models.FloatField(default=0)
    feed_consumption = models.FloatField(default=0)
    wather_consumption = models.FloatField(default=0)
    average_body_weight = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    medications = models.CharField(max_length=100)
    
