from django.contrib import admin
from dependapp.models import Project,Site
# Register your models here.
class adminProject(admin.ModelAdmin):
    list_display = ['projectname']
    
admin.site.register(Project,adminProject)


class adminSite(admin.ModelAdmin):
    list_display = ['project','sitename']
    
admin.site.register(Site,adminSite)


