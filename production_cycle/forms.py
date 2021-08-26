from django.db.models import fields
from django.forms import ModelForm
from .models import Day, Cycle, FeedDelivery, Slaughter


class DayForm(ModelForm):
    class Meta:
        model = Day
        fields = ['cycle_day', 'deads', 'selection', 'feed_consumption', 'wather_consumption',
                  'average_body_weight', 'temperature', 'humidity', 'medications', 'cycle']

        def __init__(self, fields, cycle):
            self.fields = fields
            self.model.cycle = cycle


class CycleForm(ModelForm):
    class Meta:
        model = Cycle
        fields = ['hybryd', 'herd_size', 'chick_avarage_weight',
                  'age_of_the_reproductive_stock', 'hatchery']


class SlaughterForm(ModelForm):
    class Meta:
        model = Slaughter
        fields = ['cycle', 'day_id', 'quantity', 'weight',
                  'average_weight', 'slaughterhouse']


class FeedDeliveryForm(ModelForm):
    class Meta:
        model = FeedDelivery
        fields = ['choices', 'quantity', 'price', 'cycle']
