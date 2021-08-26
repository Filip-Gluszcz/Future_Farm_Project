from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models.signals import post_delete, post_save
from django.core.signals import request_started
from django.dispatch import receiver
from .models import *
from .forms import *


class CycleListView(ListView):
    model = Cycle
    template_name = 'production_cycle/cycle/cycles.html'
    context_object_name = 'cycles'


class CycleCreateView(CreateView):
    model = Cycle
    form_class = CycleForm
    template_name = 'production_cycle/cycle/create.html'
    success_url = '/cycles/'


class CycleDetailView(DetailView):
    model = Cycle
    context_object_name = 'cycle'
    template_name = 'production_cycle/cycle/detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CycleDeleteView(DeleteView):
    model = Cycle
    success_url = '/cycles/'
    template_name = 'production_cycle/cycle/delete.html'


class FeedDeliveryCreateView(CreateView):
    model = FeedDelivery
    form_class = FeedDeliveryForm
    template_name = 'production_cycle/create_feed_delivery.html'


class CycleUpdateView(UpdateView):
    model = Cycle
    fields = ['hybryd', 'herd_size', 'chick_avarage_weight',
              'age_of_the_reproductive_stock', 'hatchery', 'current_herd_size']
    template_name_suffix = '_update_form'


class SlaughterCreateView(CreateView):
    model = Slaughter
    form_class = SlaughterForm
    template_name = 'production_cycle/create_slaughter.html'
    success_url = '/cycles/'


@receiver(post_save, sender=Slaughter)
def update_by_creating_slaughter(sender, **kwargs):
    instance = kwargs['instance']
    cycle = Cycle.objects.get(id=instance.cycle.id)
    cycle.current_herd_size -= instance.quantity
    cycle.save()


class SlautherUpdateView(UpdateView):
    model = Slaughter
    form_class = SlaughterForm
    template_name = 'production_cycle/update_slaughter.html'
    success_url = '/cycles/'

    def get(self, request, *args, **kwargs):
        slaughter = self.get_object()
        cycle = Cycle.objects.get(id=slaughter.cycle.id)
        cycle.current_herd_size += slaughter.quantity
        cycle.save()
        return super().get(request, *args, **kwargs)


class SlaughterListView(ListView):
    model = Slaughter
    template_name = ''
    context_object_name = 'slaughters'


class SlaugterDeleteView(DeleteView):
    model = Slaughter
    template_name = 'production_cycle/delete_slaughter.html'
    context_object_name = 'slaughter'
    success_url = '/cycles/'


@receiver(post_delete, sender=Slaughter)
def update_by_deleting_slaughter(sender, **kwargs):
    instance = kwargs['instance']
    cycle = Cycle.objects.get(id=instance.cycle.id)
    cycle.current_herd_size += instance.quantity
    cycle.save()


def day(request, pk):
    day = Day.objects.get(id=pk)

    context = {
        'day': day
    }
    return render(request, 'production_cycle/day.html', context)


class DayCreateView(CreateView):
    model = Day
    form_class = DayForm
    template_name = 'production_cycle/create_day.html'
    success_url = '/cycles/'


@receiver(post_save, sender=Day)
def update_by_creating_day(sender, **kwargs):
    instance = kwargs['instance']
    cycle = Cycle.objects.get(id=instance.cycle.id)
    cycle.current_herd_size -= instance.deads
    cycle.save()


class DayUpdateView(UpdateView):
    model = Day
    form_class = DayForm
    template_name = 'production_cycle/update_day.html'
    success_url = '/cycles/'

    def get(self, request, *args, **kwargs):
        day = self.get_object()
        cycle = Cycle.objects.get(id=day.cycle.id)
        cycle.current_herd_size += day.deads
        cycle.save()
        return super().get(request, *args, **kwargs)


class DayDeleteView(DeleteView):
    model = Day
    template_name = 'production_cycle/delete_day.html'
    success_url = '/cycles/'


@receiver(post_delete, sender=Day)
def update_by_deleting_day(sender, **kwargs):
    instance = kwargs['instance']
    cycle = Cycle.objects.get(id=instance.cycle.id)
    cycle.current_herd_size += instance.deads
    cycle.save()
