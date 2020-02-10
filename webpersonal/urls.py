"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from core import views
from portfolio import views as portfolio_views
from contact import views as contact_views

urlpatterns = [
    path('', views.home, name='home'), # server root
    path('about-me/', views.about, name='about'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', contact_views.contact, name='contact'),
    path('admin/', admin.site.urls),
]


# If we are in debug mode, add path to see media files
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
