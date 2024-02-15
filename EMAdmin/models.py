from django.db import models


# Create your models here.
class PersonalInfo(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary'),
    )

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    cnic = models.BigIntegerField(max_length=13)
    cnicFront = models.ImageField(null=True)
    cnicBack = models.ImageField(null=True)
    image = models.ImageField(null=True)
    date_of_birth = models.DateField()



# Inline Models
class Address(models.Model):
    ADDRESS_TYPE_CHOICES = (
        ('present', 'Present'),
        ('permanent', 'Permanent'),
    )
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50, choices=ADDRESS_TYPE_CHOICES)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class ContactNumber(models.Model):
    CONTACT_TYPE_CHOICES = (
        ('current', 'Current'),
        ('alternative', 'Alternative'),
    )
    contact_type = models.CharField(max_length=50, choices=CONTACT_TYPE_CHOICES)
    contact = models.BigIntegerField(blank=True, null=True)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class Email(models.Model):
    EMAIL_TYPE_CHOICES = (
        ('home', 'Home'),
        ('office', 'Office'),
    )
    email_type = models.CharField(max_length=50, choices=EMAIL_TYPE_CHOICES)
    email = models.CharField(max_length=50)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class Education(models.Model):
    title_of_degree = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    grade = models.CharField(max_length=2)
    year_of_passing = models.IntegerField(max_length=4)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class TeachingExperience(models.Model):
    subject_taught = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    teaching_period_from = models.DateField()
    teaching_period_to = models.DateField()
    age_group_taught = models.IntegerField(max_length=2)
    references_name = models.CharField(max_length=50)
    references_contact_no = models.BigIntegerField(max_length=11)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class Other_Professional_Experience(models.Model):
    title_of_job = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=50)
    job_period_from = models.DateField()
    job_period_to = models.DateField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class Professional_Skills(models.Model):
    skill_description = models.CharField(max_length=50)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class Religious_Or_Political_Af(models.Model):
    position = models.CharField(max_length=50)
    name_of_party = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


class References(models.Model):
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    contact_no = models.BigIntegerField(max_length=11)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)


# Inline models over


class Occupation(models.Model):
    CORE_AREA_TYPE_CHOICES = (
        ('webdeveloper', 'Web Developer'),
        ('graphicdesigner', 'Graphic Designer'),
        ('seoengineer', 'SEO Engineer'),
        ('softwaredeveloper', 'Software Developer'),
    )
    REPORTING_SUPERVISOR_CHOICES = (
        ('alishoaibzaidi', 'Ali Shoaib Zaidi'),
        ('zaynalinaqvi', 'Zayn Ali Naqvi'),
        ('syedmujtaba', 'Syed Mujtaba'),
        ('aijazmahdavi', 'Aijaz Mahdavi'),
    )
    POSITION_TYPE_CHOICES = (
        ('intern', 'Intern'),
        ('regular', 'Regular'),
    )
    name_of_employee = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=50, choices=POSITION_TYPE_CHOICES)
    core_area = models.CharField(max_length=50, choices=CORE_AREA_TYPE_CHOICES)
    reporting_supervisor = models.CharField(max_length=50, choices=REPORTING_SUPERVISOR_CHOICES)



#Sie shoaib code


