from django.urls import path
from .views import PersonDeleteView, PersonListCreateView, PersonDetailView, AllPersonListView ,PresonUpdateView

urlpatterns = [
    path('person/', PersonListCreateView.as_view(), name="person-list-create"),
    path('person/<int:pk>/', PersonDetailView.as_view(), name="person-detail"),
    path('person/all/', AllPersonListView.as_view(), name="all-person-list"),
    path('person/delete/<int:pk>/', PersonDeleteView.as_view(), name="person-delete"),
    path('person/update/<int:pk>/', PersonListCreateView.as_view(), name="person-list-create")
]
