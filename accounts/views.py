from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import CompanyProfile
from .forms import ProfileForm

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('catalog')

    else:

        form = RegisterForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )

@login_required
def profile_view(request):

    profile = CompanyProfile.objects.get(
        user=request.user
    )

    return render(
        request,
        'accounts/profile.html',
        {
            'profile': profile
        }
    )

@login_required
def edit_profile(request):

    profile = CompanyProfile.objects.get(
        user=request.user
    )

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect(
                'profile'
            )

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'accounts/edit_profile.html',
        {
            'form': form
        }
    )