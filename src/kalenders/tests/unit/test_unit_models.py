"""Unit testen voor de app kalenders."""

# stand python imports
# third party imports
# import pytest
# local imports
from kalenders.models import Kalender
from kalenders.models import KALENDER_PREFIX

JAAR = "2015"


class TestKalenderModel(object):
    """unit testen voor model kalender."""

    @staticmethod
    def maak_kalender(jaar=None, opmerkingen=None):
        """Maak een kalender aan, eventueel met waarden."""
        kalender = Kalender()
        if jaar:
            kalender.jaar = jaar
        if opmerkingen:
            kalender.opmerkingen = opmerkingen
        return kalender

    def test_kalender_heeft_jaar(self):
        """Kalender heeft een jaar."""
        kalender = self.maak_kalender()
        assert hasattr(kalender, "jaar")

    def test_kalender_heeft_opmerkingen(self):
        """Kalender heeft opmerkingen."""
        kalender = self.maak_kalender()
        assert hasattr(kalender, "opmerkingen")

    def test_unicode_representatie(self):
        """String (unicode) representatie van kalender object."""
        kalender = self.maak_kalender(jaar=JAAR)
        assert kalender.__unicode__() == KALENDER_PREFIX + JAAR

    def test_string_representatie(self):
        """String representatie van kalender object."""
        kalender = self.maak_kalender(jaar="2015")
        assert str(kalender) == KALENDER_PREFIX + JAAR
