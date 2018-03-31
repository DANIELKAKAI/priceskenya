from django.conf.urls import url
from finalapp.views import firstview,secondview

urlpatterns = [
	url(r'^$', firstview),
	url(r'^page2/',secondview,name='page2'),
	url(r'^searchresult/', firstview)
 ]