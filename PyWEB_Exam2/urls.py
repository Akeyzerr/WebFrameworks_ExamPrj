from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from PyWEB_Exam2 import settings
from homepage import views as handler_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls'), name='homepage'),
    path('blog/', include('blog.urls')),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
