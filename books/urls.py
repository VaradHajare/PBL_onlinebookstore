
from django.urls import path
from .views import BooksListView, BooksDetailView, BookCheckoutView, SearchResultsListView


urlpatterns = [
    path('', BooksListView.as_view(), name = 'list'),
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
]