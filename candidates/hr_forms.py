from django import forms
from .models import Candidate


class CandidateUpdateForm(forms.ModelForm):

    class Meta:
        model = Candidate

        fields = [
            "mobile",
            "email",
            "college",
            "experience",
            "status",
        ]

        widgets = {
            "mobile": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "college": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }