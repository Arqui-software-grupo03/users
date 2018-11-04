from django.conf.urls import include, url

from mysite.views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, UserRetrieveAPIView,
    AllUserRetrieveAPIView
)

urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/search/(?P<user>[^/.]+)?$', UserRetrieveAPIView.as_view()),
    url(r'^users/all/?$', AllUserRetrieveAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
