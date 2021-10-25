"""URLs for the ``subscribe`` app."""
from django.urls import path

from subscribe.views import SubscriptionCreateView, SubscriptionDeleteView


urlpatterns = [
    path('create/<int:ctype_pk>/<int:object_pk>/',
        SubscriptionCreateView.as_view(),
        name='subscriptions_create',),
    path('delete/<int:ctype_pk>/<int:object_pk>/',
        SubscriptionDeleteView.as_view(),
        name='subscriptions_delete',),
]
