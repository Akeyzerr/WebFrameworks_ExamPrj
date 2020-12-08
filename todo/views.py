from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django_currentuser.middleware import get_current_authenticated_user

from .models import Task
# from .todo_forms import TaskForm


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by("created")
    # form = TaskForm()
    user = get_current_authenticated_user()
    if request.method == "POST":
        Task.objects.create(
            user = user,
            title=request.POST['title']
        )
        # form = TaskForm(request.POST)
        # if form.is_valid():
        #     form.save()
        # return redirect('todo-app')
    context = {"tasks": tasks,
               # "form": form,
              }
    return render(request, 'todo/list.html', context)


# def update_task(request, pk):
#     title = "Update Task"
#     task = Task.objects.get(id=pk)
#     form = TaskForm(instance=task)
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect("todo/")
#     context = {'form': form,
#                'page_title': title}
#     return render(request, "todo/update_task.html", context)
#
#
# def delete_task(request, pk):
#     item = Task.objects.get(id=pk)
#     if request.method == "POST":
#         item.delete()
#         return redirect("todo/")
#     context = {"item":item}
#     return render(request, 'todo/delete.html', context)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title',]
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