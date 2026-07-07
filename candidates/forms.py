from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = [
        "name",
        "mobile",
        "email",
        "education",
        "branch",
        "college",
        "passing_year",
        "percentage",
        "experience",
    ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "mobile": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "education": forms.Select(attrs={"class": "form-select"}),
            "branch": forms.Select(attrs={"class": "form-select"}),
            "college": forms.TextInput(attrs={"class": "form-control"}),
            "passing_year": forms.NumberInput(attrs={"class": "form-control"}),
            "percentage": forms.NumberInput(attrs={"class": "form-control"}),
            "experience": forms.Select(attrs={"class": "form-select"}),
        }