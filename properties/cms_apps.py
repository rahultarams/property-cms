from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

class PropertyApphook(CMSApp):
    app_name = "properties"
    name = _("Property Application")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["properties.main_urls"]

apphook_pool.register(PropertyApphook)


class PropertyAddApphook(CMSApp):
    app_name = "addproperties"
    name = _("Property additions")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["properties.second_urls"]

apphook_pool.register(PropertyAddApphook)

