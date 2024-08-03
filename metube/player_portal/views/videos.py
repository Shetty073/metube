from django.shortcuts import render

from metube.decorators import signin_required
from metube.upload_portal.models.content import Content


@signin_required()
def videos_view(request):
    watch_id = request.GET.get('watch')
    if watch_id:
        content = Content.objects.get(id=watch_id)
        stars = content.stars.all()
        categories = content.categories.all()
        tags = content.tags.all()

        context = {
            'content': content,
            'stars': stars,
            'categories': categories,
            'tags': tags,
        }
        
        return render(request, 'player/player.html', context)
    
    contents = Content.objects.all()

    context = {
        'contents': contents
    }
    
    return render(request, 'player/videos.html', context)
    

