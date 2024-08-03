from django.shortcuts import redirect
from django.contrib import messages

from metube.decorators import signin_required
from metube.upload_portal.models.category import Category

@signin_required('Root', 'Admin')
def category_view(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_description = request.POST.get('category_description')

        category = Category.objects.create(name=category_name, description=category_description)
        category.save()

        messages.success(request, 'Category added successfully!')
        return redirect('upload')
    
    return redirect('upload')
