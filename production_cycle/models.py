from django.db import models


class Day(models.Model):
    date = models.DateTimeField(auto_now=True)
    cycle_day = models.IntegerField(default=0)
    deads = models.IntegerField(default=0)
    selection = models.IntegerField(default=0)
    daily_mortality_rate = models.FloatField(default=0)
    feed_consumption = models.FloatField(default=0)
    wather_consumption = models.FloatField(default=0)
    average_body_weight = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    medications = models.CharField(max_length=100, default="brak")
    cycle = models.ForeignKey("Cycle", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)


class Cycle(models.Model):
    date_of_insertion = models.DateTimeField(auto_now=True)
    hybryd = models.CharField(max_length=30, default="hybryd")
    herd_size = models.IntegerField(default=0)
    chick_avarage_weight = models.FloatField(default=0)
    age_of_the_reproductive_stock = models.CharField(
        max_length=30, default="age")
    hatchery = models.CharField(max_length=30, default="hatchery")
    current_herd_size = models.IntegerField(default=herd_size)

    def __str__(self):
        return str(self.id)


class Slaughter(models.Model):
    date = models.DateTimeField(auto_now=True)
    cycle = models.ForeignKey("Cycle", on_delete=models.CASCADE)
    day_id = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    average_weight = models.FloatField(default=0)
    slaughterhouse = models.CharField(max_length=50)


class FeedDelivery(models.Model):
    STARTER = 'ST'
    GROWER = 'GR'
    FINISHER = 'FR'
    FEED_CHOICES = [
        (STARTER, 'Starter'),
        (GROWER, 'Grower'),
        (FINISHER, 'Finisher')
    ]
    date = models.DateTimeField(auto_now=True)
    choices = models.CharField(
        max_length=2, choices=FEED_CHOICES, default=STARTER)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=1)
    cycle = models.ForeignKey("Cycle", on_delete=models.CASCADE)


class Standards(models.Model):
    cycle_day = models.IntegerField(default=0)
    average_body_weight = models.FloatField(default=0)
    daily_weight_gain = models.FloatField(default=0)
    average_daily_weight_gain = models.FloatField(default=0)
    feed_consumption = models.FloatField(default=0)
    cumulative_feed_consumption = models.FloatField(default=0)
    wather_consumption = models.FloatField(default=0)
    cumulative_wather_consumption = models.FloatField(default=0)
    feed_conversion = models.FloatField(default=0)

    def __str__(self):
        return str(self.cycle_day)
