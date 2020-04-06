from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render, reverse

from .forms import RegistrationForm


@user_passes_test(lambda user: user.is_anonymous, '/', None)
def register_user(request):
    ''' Register user. '''

    if request.method == 'GET':
        form = RegistrationForm()

    elif request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email    = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # Create user
            user = User.objects.create_user(username, email, password)
            # Login user
            user = authenticate(username=username, password=password)
            # Attach session
            login(request, user)

            return redirect(reverse('show-user-profile', args=[username]))

    return render(request, 'registration/register.html', {'form': form})
