from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AccountCreationForm, AccountChangeForm


def signIn(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AccountCreationForm()

    return render(request, template_name='accounts/signin.html', context={'form': form})

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = AccountChangeForm(rquest.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AccountChangeForm()

    return render(request, template_name='accounts/editprofile.html', context={'form':form})
