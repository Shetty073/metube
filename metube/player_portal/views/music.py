from django.shortcuts import render

from metube.decorators import signin_required


@signin_required()
def music_view(request):
    if request.method == 'POST':
        pass
    
    return render(request, 'player/music.html')
