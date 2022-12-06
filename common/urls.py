from __future__ import absolute_import

import django
from django.urls import re_path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'^password/change/done/$', password_change_done, (), name='password_change_done'),
]

urlpatterns += ['',
    re_path(r'^login/$', auth_views.LoginView, {'template_name': 'common/login.html'}, name='login_view'),
    re_path(r'^logout/$', auth_views.LogoutView, {'next_page': reverse_lazy('home')}, name='logout_view'),

    re_path(r'^password/change/$', auth_views.PasswordChangeView, {'template_name': 'common/password_change_form.html', 'post_change_redirect': reverse_lazy('password_change_done')}, name='password_change_view'),
    re_path(r'^password/reset/$', auth_views.PasswordResetView, {'email_template_name': 'common/password_reset_email.html', 'template_name': 'common/password_reset_form.html', 'post_reset_redirect': '/password/reset/done'}, name='password_reset_view'),
    re_path(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView, {'template_name': 'common/password_reset_confirm.html', 'post_reset_redirect': '/password/reset/complete/'}, name='password_reset_confirm_view'),
    re_path(r'^password/reset/complete/$', auth_views.PasswordResetCompleteView, {'template_name': 'common/password_reset_complete.html'}, name='password_reset_complete_view'),
    re_path(r'^password/reset/done/$', auth_views.PasswordResetDoneView, {'template_name': 'common/password_reset_done.html'}, name='password_reset_done_view'),
]

urlpatterns += ['',
    re_path(r'^set_language/$', django.views.i18n.set_language, name='set_language'),
]
