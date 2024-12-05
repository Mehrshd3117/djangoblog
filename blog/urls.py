from django.urls import path
from . import views

urlpatterns = [
    path('list', views.BlogListView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<str:slug>', views.BlogDetailView.as_view())
]