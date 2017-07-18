from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.mainview, name='mainview'),
    url(r'^monthly/$', views.monthlyview, name='monthlyview')
}