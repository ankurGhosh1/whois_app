from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

class LoginMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        return super().dispatch(request, *args, **kwargs)
