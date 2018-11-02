from django.conf.urls import include, url

from mysite.views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveAPIView, UserRetrieveUpdateAPIView
)

urlpatterns = [
    url(r'users/(?P<user>[^/.]+)', UserRetrieveAPIView.as_view()),
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
