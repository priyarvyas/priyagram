from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'priyagram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^instaWeb/', include('instaWeb.urls', namespace="instaWeb")),
    url(r'^$', include('instaWeb.urls', namespace="instaWeb")),
]
