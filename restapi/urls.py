from django.urls import path
from restapi import views

urlpatterns = [
    path("expenses/", views.ExpenseListCreate.as_view(), name="expense-list-create"),
    path(
        "exepenses/<pk>",
        views.ExepenseRetrieveDelete.as_view(),
        name="expense-retrieve-delete",
    ),
]
