from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidateForm
from .models import Candidate
from django.contrib.auth.decorators import login_required


def register_job(request):

    if request.method == "POST":
        form = CandidateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            print(form.errors)   # <-- Add this

    else:
        form = CandidateForm()

    return render(request, "job_form.html", {"form": form})

def success(request):
    return render(request, "success.html")
from django.db.models import Q

@login_required
def dashboard(request):

    search = request.GET.get("search", "")
    education = request.GET.get("education", "")
    branch = request.GET.get("branch", "")

    candidates = Candidate.objects.all()

    if search:
        candidates = candidates.filter(
            Q(name__icontains=search) |
            Q(branch__icontains=search) |
            Q(college__icontains=search)
        )

    if education:
        candidates = candidates.filter(education=education)

    if branch:
        candidates = candidates.filter(branch=branch)

    context = {
        "candidates": candidates,
        "total": Candidate.objects.count(),
        "diploma": Candidate.objects.filter(education="Diploma").count(),
        "iti": Candidate.objects.filter(education="ITI").count(),

        "search": search,
        "education": education,
        "branch": branch,

        "education_choices": Candidate.EDUCATION_CHOICES,
        "branch_choices": Candidate.BRANCH_CHOICES,
    }

    return render(request, "dashboard.html", context)


from django.contrib import messages

@login_required
def detail(request, pk):

    candidate = get_object_or_404(Candidate, id=pk)

    if request.method == "POST":

        candidate.status = request.POST.get("status")
        candidate.save()

        messages.success(request, "Status updated successfully.")

        return redirect("detail", pk=pk)

    return render(request, "candidate_detail.html", {
        "candidate": candidate,
        "status_choices": Candidate.STATUS_CHOICES,
    })

@login_required
def delete_candidate(request, pk):

    candidate = get_object_or_404(Candidate, id=pk)

    candidate.delete()

    return redirect("dashboard")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/")

