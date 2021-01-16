from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from .mixin import LoginRequiredMixin

# Create your views here.


class SystemView(LoginRequiredMixin, TemplateView):

    template_name = 'system/system_index.html'
