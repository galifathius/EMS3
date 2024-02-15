from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    salary_cap = models.IntegerField()
    allowed_working_hours = models.IntegerField()

    def __str__(self):
        return self.name

class SalaryCalculation(models.Model):
    ALLOWED_WORKING_HOURS_CHOICES = (
        (4, '4 hours'),
        (8, '8 hours')
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    working_days = models.IntegerField()
    allowed_working_hours = models.IntegerField(choices=ALLOWED_WORKING_HOURS_CHOICES)
    official_holidays = models.IntegerField()

    def __str__(self):
        return f"{self.employee.name}'s Salary Calculation for {self.month}"
