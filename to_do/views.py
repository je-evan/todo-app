from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from to_do.models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from to_do import forms


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = forms.TodoForm
    template_name = "to_do/create.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "to_do/list.html"
    paginate_by = 5
    
    def get_queryset(self):
        todos = Todo.objects.filter(created_by=self.request.user)
        return todos


class TodoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Todo
    template_name = "to_do/detail.html"

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.created_by:
            return True
        return False

class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    template_name = "to_do/update.html"
    fields = ['completed',]

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.created_by:
            return True
        return False

class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = "to_do/delete.html"
    success_url = '/todo/list/'

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.created_by:
            return True
        return False