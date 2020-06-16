from django.db import models

from alyx.base import BaseModel
from subjects.models import Subject
from actions.models import WaterRestriction


class Incomplete(Subject):
    """
    This proxy class allows to register as a different admin page.
    The database is left untouched
    New methods are fine but not new fields
    """

    class Meta:
        proxy = True
