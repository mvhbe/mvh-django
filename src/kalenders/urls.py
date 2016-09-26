# standard python imports
# third party imports
from django.conf.urls import url
# local imports
from kalenders import views

urlpatterns = [
    url(r'^$', views.kalenders),
]
