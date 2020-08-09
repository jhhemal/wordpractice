from django.urls import path
from .views import (
    index,
    WordCreateView,
    allwords,
    WordUpdateView,
    WordDetailView,
    WordDeleteView
)
urlpatterns = [
    path('', index, name='home'),
    path('word/create/', WordCreateView.as_view(), name='create-word'),
    path('word/<int:pk>/update', WordUpdateView.as_view(), name='update-word'),
    path('word/<int:pk>/detail', WordDetailView.as_view(), name='detail-word'),
    path('word/<int:pk>/delete', WordDeleteView.as_view(), name='delete-word'),
    path('word/all/', allwords, name='all-words')
]