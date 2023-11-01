from functools import wraps
from django.shortcuts import redirect

def redirect_authenticated_user(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homeapp:index')
        return view_func(request, *args, **kwargs)
    return _wrapped_view