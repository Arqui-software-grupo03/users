from django.conf.urls import include, url

from mysite.views import RegistrationAPIView

urlpatterns = [
    url(r'^users/?$', RegistrationAPIView.as_view()),
]
