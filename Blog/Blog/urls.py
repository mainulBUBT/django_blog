from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('', views.index, name='index')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


