from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.


def register_user(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
