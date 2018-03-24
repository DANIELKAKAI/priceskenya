from django.conf.urls import url
from finalapp.views import firstview

urlpatterns = [
	url(r'', firstview),
 ]