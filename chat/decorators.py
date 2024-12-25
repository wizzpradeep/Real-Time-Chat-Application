from django.shortcuts import redirect
from django.contrib import messages

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You are not authenticated")
            return redirect('home')
        return view_func(request, *args, **kwargs)

    return _wrapped_view

