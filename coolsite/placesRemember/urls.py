from django.urls import path
from django.conf.urls import include

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('accounts/', include('allauth.urls')),
    path('logout', logout_view, name='logout_view'),
    path('remember', remember, name='remember'),
    path('add_remember', add_remember, name='add_remember')
]