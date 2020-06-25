from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', admin.site.urls),
    path('docs/', include_docs_urls(title='后端API')),
    path('books/', include('book.urls')),
]
