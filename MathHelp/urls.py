from django.contrib import admin
from django.urls import include, path

from django.views.generic.base import TemplateView

from .views import login_request, logout_request


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),

    path('admin/', admin.site.urls),
    path('login/',  login_request,  name='login'),
    path('logout/', logout_request, name='logout'),

    path('register/', include('registration.urls')),
    path('theory/', include('theory.urls')),

]
