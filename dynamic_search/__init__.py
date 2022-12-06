from django.utils.translation import gettext_lazy as _

from common.api import register_menu

register_menu([
    {'text': _(u'Search'), 'view': 'search', 'famfam': 'zoom', 'position': 5},
])
