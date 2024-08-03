from django.shortcuts import redirect
from django.contrib import messages

from metube.decorators import signin_required
from metube.upload_portal.models.star import Star
from metube.upload_portal.models.tag import Tag


@signin_required('Root', 'Admin')
def star_view(request):
    if request.method == 'POST':
        name = request.POST.get('star_name')
        bio = request.POST.get('star_bio')
        date_of_birth = request.POST.get('star_dob')
        photo = request.FILES.get('star_image')
        breast_size = request.POST.get('breast_size')
        cup_size = request.POST.get('cup_size')
        waist_size = request.POST.get('waist_size')
        ass_size = request.POST.get('ass_size')
        tags = request.POST.getlist('star_tags')

        star = Star.objects.create(
            name=name,
            bio=bio,
            date_of_birth=date_of_birth,
            photo=photo,
            breast_size=breast_size,
            cup_size=cup_size,
            waist_size=waist_size,
            ass_size=ass_size,
        )

        # Associate tags with the star
        for tag_id in tags:
            tag = Tag.objects.get(pk=tag_id)
            star.tags.add(tag)

        # Save the star with tags
        star.save()

        messages.success(request, 'Star added successfully!')
        return redirect('upload')
    
    return redirect('upload')
