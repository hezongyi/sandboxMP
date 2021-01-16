from django.views.generic import TemplateView
from .mixin import LoginRequiredMixin
from .models import Role
from custom import SandboxCreateView, SandboxUpdateView

import json

from django.views.generic.base import View
from django.shortcuts import HttpResponse


class RoleView(LoginRequiredMixin, TemplateView):

    template_name = 'system/role.html'


class RoleCreateView(SandboxCreateView):

    model = Role
    fields = '__all__'


class RoleListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'name', 'desc']
        ret = dict(data=list(Role.objects.values(*fields)))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class RoleUpdateView(SandboxUpdateView):

    model = Role
    fields = '__all__'
    template_name_suffix = '_update'
