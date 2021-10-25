"""URLs for the ``subscribe`` app."""
from django.conf.urls import url

from subscribe.views import SubscriptionCreateView, SubscriptionDeleteView


urlpatterns = [
    url(r'^create/(?P<ctype_pk>)/(?P<object_pk>)/',
        SubscriptionCreateView.as_view(),
        name='subscriptions_create',),
    url(r'^delete/(?P<ctype_pk>)/(^P<object_pk>)/',
        SubscriptionDeleteView.as_view(),
        name='subscriptions_delete',),
]
