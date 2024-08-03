from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from functools import wraps

from metube.identity_portal.models.app_user import AppUser


def signin_required(*group_names):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            # Check if user is in the required groups
            if len(group_names) > 0 and not request.user.groups.filter(name__in=group_names).exists():
                print("group_names", group_names, request.user.groups)
                # Redirect to a 'permission denied' page
                return HttpResponseRedirect(reverse('signin'))
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def signout_required(redirect_url='videos'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse(redirect_url))
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

