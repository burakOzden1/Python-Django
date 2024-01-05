from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = context["task"].filter(user=self.request.user)
        context["count"] = context["task"].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "todo/task.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = "__all__"
    # admin panel uzerinde bulunan form islemlerinin tumunu ekrana verir.

    fields = [
        "title",
        "description",
        "complete",
    ]  # Bu sekilde yaparak tek tek istedigin form elemanini cagirabilirsin.
    success_url = reverse_lazy("task")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # fields = "__all__"
    fields = [
        "title",
        "description",
        "complete",
    ]
    success_url = reverse_lazy("task")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("task")


class CustomLoginView(LoginView):
    template_name = "todo/login.html"
    fields = "__all__"
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy("task")


class CustomLogoutView(LoginView):
    template_name = "todo/login.html"
    fields = "__all__"
    redirect_authenticated_user = False


class RegisterPage(FormView):
    template_name = "todo/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("task")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task")
        return super(RegisterPage, self).get(*args, *kwargs)
