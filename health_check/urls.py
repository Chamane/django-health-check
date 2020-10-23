from django.conf.urls import url

from health_check.views import MainView

app_name = 'health_check'

urlpatterns = [
    url(r'^$', MainView.as_view(), name='health_check_home'),
]
