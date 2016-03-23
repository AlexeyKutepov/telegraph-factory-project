from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import HappyClient
from django.utils.translation import ugettext_lazy as _


class HappyClientPlugin(CMSPluginBase):
    model = HappyClient
    name = _("Happy Client Plugin")
    render_template = "happy_client.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(HappyClientPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(HappyClientPlugin)