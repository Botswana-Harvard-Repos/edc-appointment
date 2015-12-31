from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_sync.models import SyncModelMixin

from ..choices import APPT_TYPE


class SubjectConfiguration(SyncModelMixin, BaseUuidModel):
    """Store subject specific defaults."""

    subject_identifier = models.CharField(
        max_length=36)

    default_appt_type = models.CharField(
        max_length=10,
        default='clinic',
        choices=APPT_TYPE,
        help_text='')

    def __unicode__(self):
        return self.subject_identifier

    def natural_key(self):
        return (self.subject_identifier, )

    class Meta:
        app_label = 'edc_appointment'
        # db_table = 'bhp_subject_config_subjectconfiguration'