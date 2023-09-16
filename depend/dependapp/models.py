from django.db import models

class Project(models.Model):
  
    projectname = models.CharField(max_length=100)
           
    def __str__(self):
        return self.projectname

class Site(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)  # New field for project name
    sitename = models.CharField(max_length=100)
    
   
    def __str__(self):
        return self.sitename
    
    
