from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from .filters import TaskFilter
from .models import Task
from .todo_forms import TaskForm


@login_required
def index(request):
    user_setting_pages = request.user.profile.tasks_per_page
    tasks = Task.objects.filter(user=request.user).order_by("-created")
    form = TaskForm()
    filter_tasks = TaskFilter(request.GET, queryset=tasks)
    tasks = filter_tasks.qs

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo-app')

    if tasks:
        paginator = Paginator(tasks, user_setting_pages)
        try:
            tasks = paginator.page(request.GET.get('page'))
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)

    context = {"page_obj": tasks,
               "form": form,
               "filter": filter_tasks,
               "tasks_search": True,
               }
    return render(request, 'todo/list.html', context)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'complete', 'tags']
    success_url = '/todo'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/todo'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False
