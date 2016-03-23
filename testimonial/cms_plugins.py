from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Testimonial
from django.utils.translation import ugettext_lazy as _


class TestimonialPlugin(CMSPluginBase):
    model = Testimonial
    name = _("Testimonial Plugin")
    render_template = "testimonial.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(TestimonialPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(TestimonialPlugin)