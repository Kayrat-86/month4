from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    experience = models.PositiveIntegerField(help_text="Опыт в годах")
    stack = models.CharField(max_length=200)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    about = models.TextField()
    desired_salary = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

