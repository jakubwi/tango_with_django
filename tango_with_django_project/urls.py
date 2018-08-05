"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic.base import TemplateView
from registration.backends.simple.urls import RegistrationView
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rango import views

@method_decorator(login_required, name='dispatch')
class RestrictedView(TemplateView):
    template_name = "rango/restricted.html"

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return "/rango/register_profile/"

class TopSearchView(TemplateView):
    template_name = "rango/search.html"

urlpatterns = [
    path('rango/', include('rango.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('search/', TopSearchView.as_view(), name='search'),
    path('restricted/', RestrictedView.as_view(), name='restricted'),
    path('accounts/', include('registration.backends.simple.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
