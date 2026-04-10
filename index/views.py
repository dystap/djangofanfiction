from django.shortcuts import redirect, render

from index.forms import ProfileForm
from index.models import Profile

# Create your views here.

def home(request):
    profiles = Profile.objects.all()
    
    return render(request, "index/home.html", {
        "profiles": profiles,
    })

def profile(request, id):

    profile = Profile.objects.filter(id=id).first()

    if not profile:
        raise 

    return render(request, 'index/profile.html', {
        "profile": profile,
    })

def isiform(request):
    return render(request, "index/isiform.html")

def isiformsubmit(request):

    print(request.POST)

    Profile.objects.create(
        name = request.POST.get("name"),
        email = request.POST.get("email"),
        birthday = request.POST.get("date_of_birth"),
        hobby = request.POST.get("hobby"),
        quote = request.POST.get("quote"),
    )

    

    return redirect("index/home.html")


def isiForm2(request):

    form = ProfileForm()

    return render(request, "index/isiForm2.html", {
        "form": form,
    })


def fio(request):
    return render(request, "index/fio.html")