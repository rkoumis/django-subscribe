"""URLs for the ``subscribe`` app."""
from django.urls import re_path

from subscribe.views import SubscriptionCreateView, SubscriptionDeleteView


urlpatterns = [
    re_path(r'^create/(?P<ctype_pk>\d+)/(?P<object_pk>\d+)/$',
        SubscriptionCreateView.as_view(),
        name='subscriptions_create',),
    re_path(r'^delete/(?P<ctype_pk>\d+)/(?P<object_pk>\d+)/$',
        SubscriptionDeleteView.as_view(),
        name='subscriptions_delete',),
]
