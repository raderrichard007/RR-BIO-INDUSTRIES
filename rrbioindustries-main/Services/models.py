from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class StockList(models.Model):
    date = models.DateField()
    opening = models.DecimalField(max_digits=10, decimal_places=2)
    daily_use = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class Member(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField(null=True, blank=True)  # Allow null for absent members
    time_out = models.TimeField(null=True, blank=True)  # Allow null for absent members
    present = models.BooleanField(default=False)


class Salary(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    month = models.DateField()  # The month for which the salary is calculated
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Basic salary
    total_days_present = models.IntegerField()  # Total days the member was present
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Calculated total salary
    deductions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Deductions if any
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Bonuses if any

    def __str__(self):
        return f"Salary for {self.member.name} - {self.month.strftime('%B %Y')}"
    
    