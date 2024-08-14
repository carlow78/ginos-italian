from django.views.generic import TemplateView

"""
Returns the home (index.html)
"""

class Index(TemplateView):
    template_name = 'home/index.html'