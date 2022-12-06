from __future__ import absolute_import

from django.urls import re_path
from django.utils.translation import gettext_lazy as _

from generic_views.views import generic_assign_remove
#from inventory import location_filter
from photos.views import generic_photos

#from . import state_filter
from .conf import settings as asset_settings
from .forms import (ItemForm, ItemForm_view, ItemGroupForm, ItemGroupForm_view,
                    PersonForm, PersonForm_view)
from .models import Item, ItemGroup, Person, State
from .views import (AssetCreateView, AssetDeleteView, AssetDetailView, AssetListView,
                    AssetOrphanListView, AssetUpdateView, GroupCreateView,
                    GroupDeleteView, GroupDetailView, GroupListView,
                    PersonCreateView, PersonDeleteView, PersonDetailView,
                    PersonListView, PersonUpdateView, StateCreateView,
                    StateDeleteView, StateListView, StateUpdateView, person_assign_remove_item,
                    item_assign_remove_person, item_setstate, item_remove_state, group_assign_remove_item)

urlpatterns = [
    re_path(r'^person/(?P<object_id>\d+)/photos/$', generic_photos, {'model': Person, 'max_photos': asset_settings.MAX_PERSON_PHOTOS, 'extra_context': {'object_name': _(u'person')}}, 'person_photos'),
    re_path(r'^person/(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person_view'),
    re_path(r'^person/list/$', PersonListView.as_view(), name='person_list'),
    re_path(r'^person/create/$', PersonCreateView.as_view(), name='person_create'),
    re_path(r'^person/(?P<pk>\d+)/update/$', PersonUpdateView.as_view(), name='person_update'),
    re_path(r'^person/(?P<pk>\d+)/delete/$', PersonDeleteView.as_view(), name='person_delete'),
    re_path(r'^person/(?P<object_id>\d+)/assign/$', person_assign_remove_item, (), 'person_assign_item'),

    re_path(r'^asset/create/$', AssetCreateView.as_view(), name='item_create'),
    re_path(r'^asset/(?P<pk>\d+)/update/$', AssetUpdateView.as_view(), name='item_update'),
    re_path(r'^asset/(?P<pk>\d+)/delete/$', AssetDeleteView.as_view(), name='item_delete'),
    re_path(r'^asset/(?P<object_id>\d+)/assign/$', item_assign_remove_person, (), name='item_assign_person'),
    re_path(r'^asset/orphans/$', AssetOrphanListView.as_view(), name='item_orphans_list'),
    re_path(r'^asset/list/$', AssetListView.as_view(), name='item_list'),
    re_path(r'^asset/(?P<pk>\d+)/$', AssetDetailView.as_view(), name='item_view'),
    re_path(r'^asset/(?P<object_id>\d+)/photos/$', generic_photos, {'model': Item, 'max_photos': asset_settings.MAX_ASSET_PHOTOS, 'extra_context': {'object_name': _(u'asset')}}, 'item_photos'),
    re_path(r'^asset/(?P<object_id>\d+)/state/(?P<state_id>\d+)/set/$', item_setstate, (), 'item_setstate'),
    re_path(r'^asset/(?P<object_id>\d+)/state/(?P<state_id>\d+)/unset$', item_remove_state, (), 'item_remove_state'),

    re_path(r'^group/list/$', GroupListView.as_view(), name='group_list'),
    re_path(r'^group/create/$', GroupCreateView.as_view(), name='group_create'),
    re_path(r'^group/(?P<pk>\d+)/$', GroupDetailView.as_view(), name='group_view'),
    re_path(r'^group/(?P<object_id>\d+)/update/$', group_assign_remove_item, (), name='group_update'),
    re_path(r'^group/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='group_delete'),

    re_path(r'^state/list/$', StateListView.as_view(), name='state_list'),
    re_path(r'^state/create/$', StateCreateView.as_view(), name='state_create'),
    re_path(r'^state/(?P<pk>\d+)/update/$', StateUpdateView.as_view(), name='state_update'),
    re_path(r'^state/(?P<pk>\d+)/delete/$', StateDeleteView.as_view(), name='state_delete'),
]
