#coding=utf-8

from django.template.context_processors import csrf
from django.views.generic import TemplateView

class TemplateViewWithCsrf(TemplateView):
    """
    This set the csrf which could be called by the Django template
    """
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.update(csrf(request))

        return self.render_to_response(context)