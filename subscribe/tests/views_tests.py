"""Tests for the views of the ``subscriptions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from mixer.backend.django import mixer

from .. import views
from .. import models


class SubscriptionCreateViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.SubscriptionCreateView

    def setUp(self):
        self.user = mixer.blend('auth.User')
        self.dummy = mixer.blend('test_app.DummyModel')
        self.ctype = ContentType.objects.get_for_model(self.dummy)

    def get_view_kwargs(self):
        return {'ctype_pk': self.ctype.pk, 'object_pk': self.dummy.pk, }

    def test_anonymous(self):
        """Should redirect to login if user is anonymous."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable if user is authenticated."""
        # No subscription should exist before the call.
        pk = self.dummy.pk
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        self.assertEqual(0, len(subscription))
        self.redirects(user=self.user, to=f"/dummy/{self.dummy.pk}")
        # self.is_callable(user=self.user)
        # Query again, and there should be one.
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        self.assertEqual(1, len(subscription))

    def test_postable(self):
        """Should be postable if user is authenticated."""
        # No subscription should exist before the call.
        pk = self.dummy.pk
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        self.assertEqual(0, len(subscription))
        self.is_postable(user=self.user, to=f'/dummy/{pk}')
        # Query again, and there should be one.
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        self.assertEqual(1, len(subscription))


class SubscriptionDeleteViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    view_class = views.SubscriptionDeleteView

    def setUp(self):
        self.subscription = mixer.blend(
            'subscribe.Subscription',
            content_object=mixer.blend('test_app.DummyModel'))
        self.ctype = ContentType.objects.get_for_model(
            self.subscription.content_type)

    def get_view_kwargs(self):
        return {
            'ctype_pk': self.subscription.content_type.pk,
            'object_pk': self.subscription.object_id,
        }

    def test_anonymous(self):
        """Should redirect to login if user is anonymous."""
        self.should_redirect_to_login_when_anonymous()

    def test_callable(self):
        """Should be callable if user is authenticated."""
        pk = self.subscription.object_id
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        # A subscription should exist before the call.
        self.assertEqual(1, len(subscription))
        # self.is_callable(user=self.subscription.user)
        self.redirects(user=self.subscription.user, to=f'/dummy/{pk}')
        # Query again, and there should be none.
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        self.assertEqual(0, len(subscription))

    def test_postable(self):
        """Should be postable if user is authenticated."""
        pk = self.subscription.object_id
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        # A subscription should exist before the call.
        self.assertEqual(1, len(subscription))
        self.is_postable(user=self.subscription.user, to=f'/dummy/{pk}')
        # Query again, and there should be none.
        subscription = models.Subscription.objects.filter(object_id=pk).all()
        self.assertEqual(0, len(subscription))
