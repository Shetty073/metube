from django.shortcuts import redirect
from django.contrib import messages

from metube.decorators import signin_required
from metube.upload_portal.models.tag import Tag

@signin_required('Root', 'Admin')
def tag_view(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')
        tag_type = request.POST.get('tag_type')

        tag = Tag.objects.create(name=tag_name, tag_type=tag_type)
        tag.save()

        messages.success(request, 'Tag added successfully!')
        return redirect('upload')
    
    return redirect('upload')
