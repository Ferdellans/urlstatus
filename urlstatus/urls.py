from django.contrib import admin
from django.urls import path
from checker.views import Index, RequestUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('check', RequestUrl.as_view())
]
