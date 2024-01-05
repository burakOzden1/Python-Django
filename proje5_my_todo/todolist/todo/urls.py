from django.urls import path
from .views import (
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    CustomLoginView,
    RegisterPage,
    CustomLogoutView,
)

urlpatterns = [
    path("", TaskList.as_view(), name="task"),
    path("task-create/", TaskCreate.as_view(), name="tasks-create"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="tasks-detail"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="tasks-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="tasks-delete"),
]
