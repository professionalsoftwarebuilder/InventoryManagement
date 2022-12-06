from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from generic_views.forms import DetailForm

from .models import (Inventory, InventoryTransaction, ItemTemplate, Location,
                     Log, Supplier)


class LocationForm_view(DetailForm):
    class Meta:
        model = Location
        fields = '__all__'


class ItemTemplateForm(forms.ModelForm):
    class Meta:
        model = ItemTemplate
        exclude = ('photos', 'supplies', 'suppliers')


class ItemTemplateForm_view(DetailForm):
    class Meta:
        model = ItemTemplate
        exclude = ('photos',)


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

class InventoryForm_view(DetailForm):
    class Meta:
        model = Inventory
        fields = '__all__'

class InventoryTransactionForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        fields = '__all__'


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
