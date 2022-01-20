from cytopy.data.setup import global_init
global_init('MyDatabase')



# We store HDF5 files on our local drive and provide the path to 'data_directory'
from cytopy.data.project import Project
new_project = Project(project_id='TestProject',
                      data_directory='/home/user/CytoPyData')
new_project.save()

new_project = Project.objects(project_id='TestProject').get(

# Returns a list of Project documents
Project.objects()

new_project.update_data_directory('/home/user/new/path')