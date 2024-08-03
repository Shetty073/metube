from django.shortcuts import redirect, render
from django.contrib import messages

from metube.decorators import signin_required
from metube.upload_portal.models.category import Category
from metube.upload_portal.models.content import Content
from metube.upload_portal.models.star import Star
from metube.upload_portal.models.tag import Tag

@signin_required('Root', 'Admin')
def upload_view(request):
    if request.method == 'POST':
        title = request.POST.get('content_title')
        description = request.POST.get('content_description')
        content_type = request.POST.get('content_type')
        file = request.FILES.get('file')
        categories = request.POST.getlist('category')
        tags = request.POST.getlist('tags')
        stars = request.POST.getlist('stars')

        content = Content.objects.create(
            title=title,
            description=description,
            content_type=content_type,
            file=file,
            uploaded_by=request.user
        )

        content.categories.set(categories)
        content.tags.set(tags)
        content.stars.set(stars)
        content.save()

        messages.success(request, 'Content uploaded successfully!')
        return redirect('upload')

    context = {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'tag_types': Tag.TAG_TYPE_CHOICES,
        'stars': Star.objects.all(),
    }

    return render(request, 'upload/upload.html', context)
