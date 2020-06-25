from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    url(r'^books/$', views.BookList.as_view(), name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view())
])