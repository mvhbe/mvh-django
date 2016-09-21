"""Models voor de app kalenders."""

from django.db import models

KALENDER_PREFIX = "Wedstrijdkalender "


class Kalender(models.Model):
    """Beschrijving velden model kalender."""

    jaar = models.CharField(max_length=4, unique=True)
    opmerkingen = models.TextField()

    def __unicode__(self):
        """String (unicode) reprensentatie voor kalender."""
        return KALENDER_PREFIX + self.jaar

    def __str__(self):
        """String reprensentatie voor kalender."""
        return KALENDER_PREFIX + self.jaar
