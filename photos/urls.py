from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<object_id>\d+)/delete/$', 'generic_photo_delete', name='generic_photo_delete'),
    url(r'^(?P<object_id>\d+)/mark_as_main/$', 'generic_photo_mark_main', name='generic_photo_mark_main')
]
