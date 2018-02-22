from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os

from contents.models import Content
from account.models import User
UPLOAD_DIR = '/home/vagrant/contents'
TEMPLATE_DIR = 'TemplateData'
BUILD_DIR = 'Build'

@login_required
def form(request):
    if request.method != 'POST':
        return render(request, 'upload/upload.html')

    title = request.POST['title']
    index_file = request.FILES['index']
    template_files = request.FILES.getlist("Template[]")
    build_files = request.FILES.getlist("Build[]")
    user_id = request.POST['user']

    user = User(id = user_id)
    data = Content(name = title, author = user)
    data.save()

    dir_path = os.path.join(UPLOAD_DIR, str(data.id))
    template_path = os.path.join(dir_path, TEMPLATE_DIR)
    build_path = os.path.join(dir_path, BUILD_DIR)

    index_path = os.path.join(dir_path, index_file.name)
    template_pathes = []
    for file in template_files:
        template_pathes.append(os.path.join(template_path, file.name))
    build_pathes = []
    for file in build_files:
        build_pathes.append(os.path.join(build_path, file.name))

    os.mkdir(dir_path)
    os.mkdir(template_path)
    os.mkdir(build_path)

    with open(index_path, "wb") as index_data:
        for chunk in index_file.chunks():
            index_data.write(chunk)

    template_length = len(template_files)
    for i in range(template_length):
        with open(template_pathes[i], "wb") as data:
            for chunk in template_files[i]:
                data.write(chunk)

    build_length = len(build_files)
    for i in range(build_length):
        with open(build_pathes[i], "wb") as data:
            for chunk in build_files[i]:
                data.write(chunk)

    return redirect('upload:complete')

def complete(request):
    return render(request, 'upload/complete.html')
