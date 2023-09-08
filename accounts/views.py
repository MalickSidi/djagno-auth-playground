from django.shortcuts import render
from .models import Profile
from .forms import UserSignupForm

def signup(request):
    form = UserSignupForm()

    if request.method == "POST":
        pass
    else:
        context = {
            'form': form
        }

    return render(request, 'registration/signup.html', context)


def profile(request):
    return(render(request, 'accounts/profile.html'))