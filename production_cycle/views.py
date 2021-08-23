from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *


def cycles(request):
    cycles = Cycle.objects.all()

    context = {
        'cycles': cycles
    }

    return render(request, 'production_cycle/cycles.html', context)


class CreateCycleView(CreateView):
    model = Cycle
    form_class = CreateCycleForm
    template_name = 'production_cycle/createCycle.html'
    success_url = '/cycles/'


class CycleDetailView(DetailView):
    model = Cycle

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class DeleteCycleView(DeleteView):
    model = Cycle
    success_url = '/cycles/'


class CycleUpdateView(UpdateView):
    model = Cycle
    fields = ['hybryd', 'herd_size', 'chick_avarage_weight',
              'age_of_the_reproductive_stock', 'hatchery', 'current_herd_size']
    template_name_suffix = '_update_form'


def create_slaughter(request, pk):
    cycle = Cycle.objects.get(id=pk)
    form = CreateSlaughterForm()
    if request.method == 'POST':
        form = CreateSlaughterForm(request.POST)
        if form.is_valid():
            form.save()
            cycle.current_herd_size -= int(request.POST.get("quantity"))
            cycle.save()
            return redirect('/cycles')

    context = {
        'form': form
    }
    return render(request, 'production_cycle/createSlaughter.html', context)


def day(request, pk):
    day = Day.objects.get(id=pk)

    context = {
        'day': day
    }
    return render(request, 'production_cycle/day.html', context)


def create_day(request, pk):
    cycle = Cycle.objects.get(id=pk)
    #day = cycle.day_set.last()
    form = CreateDayForm()
    if request.method == 'POST':
        form = CreateDayForm(request.POST)
        if form.is_valid():
            form.save()
            cycle.current_herd_size -= int(request.POST.get("deads"))
            cycle.save()
            return redirect('/cycles')

    context = {
        'form': form
    }
    return render(request, 'production_cycle/createDay.html', context)


def update_day(request, pk):
    day = Day.objects.get(id=pk)
    form = CreateDayForm(instance=day)

    if request.method == 'POST':
        day.cycle.current_herd_size += day.deads
        day.cycle.save()
        form = CreateDayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            day.cycle.current_herd_size -= int(request.POST.get("deads"))
            day.cycle.save()
            return redirect('/cycles')

    context = {
        'form': form
    }
    return render(request, 'production_cycle/updateDay.html', context)


def delete_day(request, pk):
    day = Day.objects.get(id=pk)
    form = CreateDayForm(instance=day)
    if request.method == 'POST':
        day.delete()

    context = {
        'form': form
    }
    return render(request, 'production_cycle/deleteDay.html', context)
