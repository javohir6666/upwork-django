from django.contrib import admin
from .models import CustomUser, Skill,Education,WorkExperience
from django.contrib.auth.models import Group

class CustomUserEducationInline(admin.TabularInline):
    model = Education


class CustomUserSkillInline(admin.TabularInline):
    model = Skill
    

class CustomUserWorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'user_type', 'date_joined']
    list_filter = ('user_type', 'gender')
    inlines = [CustomUserEducationInline, CustomUserSkillInline, CustomUserWorkExperienceInline]
    
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.unregister(Group)