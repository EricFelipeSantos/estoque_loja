from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='core:login')
def home(request):
    return render(request, 'core/home.html')

def login_view(request):

    if request.user.is_authenticated:
        return redirect('core:home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:home')

    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})