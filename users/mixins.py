from django.contrib.auth import logout


class LogOutRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            logout(request)
        return super().dispatch(request, *args, **kwargs)
