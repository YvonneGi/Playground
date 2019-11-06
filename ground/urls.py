from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$',views.welcome,name = 'welcome'),
  url(r'^accounts/profile/(\d+)', views.profile, name = 'profile'),
  url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
  url(r'^all/$', views.all_playgrounds, name='allplaygrounds')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)