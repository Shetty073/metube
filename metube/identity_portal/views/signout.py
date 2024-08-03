from django.shortcuts import redirect
from django.contrib.auth import logout

from metube.decorators import signin_required

@signin_required()
def signout_view(request):
    logout(request)
    
    return redirect('signin')
