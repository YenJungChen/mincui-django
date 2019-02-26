from __future__ import unicode_literals
from django.conf.urls import url
from . import views
from core import views as core_views

urlpatterns = [
               url(r'^$', core_views.company, name='company'),
               url(r'^game/$', core_views.game, name='game'),
               url(r'^contact/$', core_views.contact, name='contact'),
               url(r'^news/$', core_views.news, name='news'),

]
