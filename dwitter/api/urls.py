from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateDweeterView

urlpatterns = {
    url(r'^dweeters/$', CreateDweeterView.as_view(), name="createSweeter"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
