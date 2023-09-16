from django.shortcuts import render
from dependapp.models import Project,Site
from dependapp.Logfile import logdata
def dependantfield(request):
    projectid = request.GET.get('project', None)
    logdata(projectid)
    siteid = request.GET.get('site',None)
    logdata(siteid)
    site = None

    if projectid:
        getproject = Project.objects.get(id=projectid)
        site = Site.objects.filter(project=getproject)
        logdata(getproject)
        
    project = Project.objects.all()
    return render(request,'dependapp/home.html',locals())

