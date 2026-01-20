from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Candidate
from .forms import CandidateForm, LoginForm
from django.contrib.auth import logout


def register_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CandidateForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("candidate_list")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})



def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, "users/candidates.html", {"candidates": candidates})

def logout_view(request):
    logout(request)
    return redirect('login')

