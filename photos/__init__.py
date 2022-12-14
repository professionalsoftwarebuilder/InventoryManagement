# from __future__ import absolute_import
#
# from django.utils.translation import gettext_lazy as _
#
# from common.api import register_links
#
# from .models import GenericPhoto
#
# generic_photo_delete = {'text': _('Delete photo'), 'view': 'generic_photo_delete', 'args': 'object.id', 'famfam': 'picture_delete'}
# generic_photo_mark_main = {'text': _('Mark photo as main'), 'view': 'generic_photo_mark_main', 'args': 'object.id', 'famfam': 'picture_edit'}
#
# register_links(GenericPhoto, [generic_photo_mark_main, generic_photo_delete])
# register_links(['generic_photo_mark_main', 'generic_photo_delete'], [generic_photo_mark_main, generic_photo_delete], menu_name='sidebar')
