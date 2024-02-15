from django.contrib import admin
from .models import *


# Register your models here.

# Inlines

class EmailInline(admin.StackedInline):
    model = Email
    extra = 0


class ContactNumberInline(admin.StackedInline):
    model = ContactNumber
    extra = 0


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0


class TeachingExperienceInline(admin.StackedInline):
    model = TeachingExperience
    extra = 0


class Other_Professional_ExperienceInline(admin.StackedInline):
    model = Other_Professional_Experience
    extra = 0


class SkillInline(admin.StackedInline):
    model = Professional_Skills
    extra = 0


class Religious_Or_Political_AfInline(admin.StackedInline):
    model = Religious_Or_Political_Af
    extra = 0


class ReferencesInline(admin.StackedInline):
    model = References
    extra = 0


# Inline over
@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    inlines = [EmailInline,
               ContactNumberInline,
               AddressInline,
               EducationInline,
               TeachingExperienceInline,
               Other_Professional_ExperienceInline,
               SkillInline,
               Religious_Or_Political_AfInline,
               ReferencesInline
               ]
    list_display = ('first_name', 'last_name', 'gender', 'cnic', 'date_of_birth')


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name_of_employee', 'position', 'core_area', 'reporting_supervisor')

