from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from metube.decorators import signin_required
from metube.identity_portal.models.app_user import AppUser


@signin_required('Root', 'Admin')
def user_view(request):
    # Fetch groups initially based on user permissions
    groups = Group.objects.all() if request.user.is_superuser else Group.objects.exclude(name='Root')
    context = {'groups': groups}
    
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Password and confirm password fields must match')
            return render(request, 'identity/user.html', context)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        group_pk = request.POST.get('user_group')

        try:
            group = Group.objects.get(pk=group_pk)
        except Group.DoesNotExist:
            messages.error(request, 'The selected group does not exist.')
            return render(request, 'identity/user.html', context)

        # Create and save the user
        user = AppUser.objects.create_user(email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name

        user.groups.add(group)

        if group.name in ('Root', 'Admin'):
            user.is_staff = True

            # Add the 'Viewer' group if it exists
            viewer_group = Group.objects.filter(name='Viewer').first()
            if viewer_group:
                user.groups.add(viewer_group)

            if group.name == 'Root':
                user.is_superuser = True

        user.save()

        messages.success(request, 'User added successfully')

        return redirect('user')

    return render(request, 'identity/user.html', context)
