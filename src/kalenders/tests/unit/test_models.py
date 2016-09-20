"""Unit testen voor de app kalenders."""
import pytest


class TestKalenderModel(object):
    """unit testen voor model kalender."""

    def test_kalender_heeft_omschrijving(self):
        """Kalender heeft een omschrijving."""
        kalender = Kalender()
        assert hasattr(kalender, "omschrijving")
