from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PropertyPluginModel
from django.utils.translation import gettext_lazy as _

@plugin_pool.register_plugin
class PersonPluginPublisher(CMSPluginBase):
    model = PropertyPluginModel
    name = _("property Display Plugin")
    render_template = "property_plugin/display_person.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['property'] = instance.property
        return context


