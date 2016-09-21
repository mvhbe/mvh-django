"""Integratie testen voor de app kalenders."""

# stand python imports
# third party imports
from mixer.backend.django import mixer
import pytest
# local imports
from kalenders.models import Kalender

pytestmark = pytest.mark.django_db


class TestIntegrationKalenderModel(object):
    """Integratie testen voor model kalender."""

    def test_kalender_wordt_bewaard(self):
        """Kalender wordt correct bewaard."""
        KALENDER_JAAR = "2015"
        KALENDER_OPMERKINGEN = "Geen opmerkingen"
        kalender = mixer.blend(Kalender, jaar=KALENDER_JAAR, opmerkingen=KALENDER_OPMERKINGEN)
        assert kalender.pk == 1
        assert kalender.jaar == KALENDER_JAAR
        assert kalender.opmerkingen == KALENDER_OPMERKINGEN
