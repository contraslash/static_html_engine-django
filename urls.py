from django.conf.urls import url

from . import views
from . import conf
urlpatterns = [
    url(
        r'^$',
        views.List.as_view(),
        name=conf.LIST_HTML_URL_NAME
    ),
    url(
        r'^create/$',
        views.Create.as_view(),
        name=conf.CREATE_HTML_URL_NAME
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        views.Detail.as_view(),
        name=conf.DETAIL_HTML_URL_NAME
    ),
    url(
        r'^(?P<slug>[\w-]+)/edit/$',
        views.Update.as_view(),
        name=conf.EDIT_HTML_URL_NAME
    ),

]