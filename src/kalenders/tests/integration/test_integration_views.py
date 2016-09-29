# standard python imports
# third party imports
from django.test import RequestFactory
# local imports
from kalenders import views


class TestKalendersView(object):
    """Test overzicht kalenders."""

    def test_kalenders_home(self):
        request = RequestFactory().get("/kalenders/")
        response = views.home(request)
        assert response.status_code == 200
