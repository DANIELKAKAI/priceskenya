from django.conf.urls import include, url
from myapp.views import firstview,search,idtest

urlpatterns = [
	url(r'^$', firstview),
	url(r'^search/',search,name='search'),
	url(r'^idtest/(?P<id>\d+)/$',idtest,name = 'idtest'),
]