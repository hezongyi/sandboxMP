from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .models import Structure

User = get_user_model()


class TestView(ListView):
    model = User
    context_object_name = 'user_all'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['structure_all'] = Structure.objects.all()
        return context

    def get_queryset(self):
        return User.objects.filter(gender=self.kwargs['gender'])