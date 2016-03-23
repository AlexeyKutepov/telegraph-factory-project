from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Portfolio
from django.utils.translation import ugettext_lazy as _


class PortfolioPlugin(CMSPluginBase):
    model = Portfolio
    name = _("Portfolio Plugin")
    render_template = "portfolio.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(PortfolioPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(PortfolioPlugin)