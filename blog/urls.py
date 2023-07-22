from django.urls import path
from .views import list_view, detail_view

urlpatterns = [
    path('', list_view, name='list_view'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',detail_view, name='detail_view')

]
