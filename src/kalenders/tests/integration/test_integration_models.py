"""Integratie testen voor de app kalenders."""

# stand python imports
# third party imports
import pytest
from django.core.exceptions import ObjectDoesNotExist
# local imports
from kalenders.models import Kalender

pytestmark = pytest.mark.django_db


class TestIntegrationKalenderModel(object):
    """Integratie testen voor model kalender."""

    def test_crud_kalender(self):
        """Kalender wordt correct bewaard."""
        KALENDER_JAAR = "2015"
        KALENDER_OPMERKINGEN = "Geen opmerkingen"
        KALENDER_NIEUWE_OPMERKINGEN = "Gewijzigde opmerkingen"
        origineleKalender = Kalender.objects.create(
            jaar=KALENDER_JAAR, opmerkingen=KALENDER_OPMERKINGEN
        )
        assert origineleKalender.pk == 1
        assert origineleKalender.jaar == KALENDER_JAAR
        assert origineleKalender.opmerkingen == KALENDER_OPMERKINGEN
        kalender = Kalender.objects.get(pk=origineleKalender.pk)
        assert origineleKalender.pk == kalender.pk
        assert origineleKalender.jaar == kalender.jaar
        assert origineleKalender.opmerkingen == kalender.opmerkingen
        origineleKalender.opmerkingen = KALENDER_NIEUWE_OPMERKINGEN
        origineleKalender.save()
        kalender = Kalender.objects.get(pk=origineleKalender.pk)
        assert origineleKalender.pk == kalender.pk
        assert origineleKalender.jaar == kalender.jaar
        assert origineleKalender.opmerkingen == kalender.opmerkingen
        origineleKalender.delete()
        with pytest.raises(ObjectDoesNotExist):
            kalender = Kalender.objects.get(pk=origineleKalender.pk)
