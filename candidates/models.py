from django.db import models

# Create your models here.

class Candidate(models.Model):

    EDUCATION_CHOICES = [
        ("Diploma", "Diploma"),
        ("ITI", "ITI"),
    ]

    BRANCH_CHOICES = [
        ("Mechanical", "Mechanical"),
        ("Electrical", "Electrical"),
        ("Electronics", "Electronics"),
        ("Civil", "Civil"),
        ("Computer", "Computer"),
        ("CNC Operator", "CNC Operator"),
        ("Fitter", "Fitter"),
        ("Turner", "Turner"),
        ("Welder", "Welder"),
        ("Machinist", "Machinist"),
        ("Automobile", "Automobile"),
    ]

    EXPERIENCE_CHOICES = [
        ("Fresher", "Fresher"),
        ("0-1 Year", "0-1 Year"),
        ("1-3 Years", "1-3 Years"),
        ("3-5 Years", "3-5 Years"),
        ("5+ Years", "5+ Years"),
    ]

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Under Review", "Under Review"),
        ("Shortlisted", "Shortlisted"),
        ("Interview Scheduled", "Interview Scheduled"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
        ("Joined", "Joined"),
    ]

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()

    education = models.CharField(
        max_length=20,
        choices=EDUCATION_CHOICES
    )

    branch = models.CharField(
        max_length=50,
        choices=BRANCH_CHOICES
    )

    college = models.CharField(max_length=150)

    passing_year = models.IntegerField()

    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    experience = models.CharField(
        max_length=30,
        choices=EXPERIENCE_CHOICES
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    created_at = models.DateTimeField(auto_now_add=True)