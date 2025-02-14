from django.urls import path
from . import views

app_name = 'address_book'

urlpatterns = [
    path('', views.index_address_book, name='index_address_book'),
    path('create/', views.create_contact, name='create_contact'),
    path('<int:contact_id>/edit/', views.edit_contact, name='edit_contact'),
    path('<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('list/', views.contact_list, name='contact_list'),
    path('upcoming-birthdays/', views.upcoming_birthdays, name='upcoming_birthdays'),
    path('search/', views.search_contacts, name='search_contacts'),
    path('<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]
