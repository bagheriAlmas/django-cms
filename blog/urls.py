from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    # path('', list_view, name='list_view'),
    path('', PostListView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',PostDetailView.as_view(), name='detail_view')

]
