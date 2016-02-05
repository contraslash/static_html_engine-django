from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as auth_models

from base import models as base_models
from . import conf as static_htlm_conf

# Create your models here.
class StaticHtml(base_models.FullBaseModel):

    url_name = "%s:%s" % (static_htlm_conf.NAMESPACE, static_htlm_conf.DETAIL_HTML_URL_NAME)

    url = models.TextField()
    user = models.ForeignKey(auth_models.User)
    markdown = models.TextField(default="")

    def __unicode__(self):
        return self.url