from django.urls import path
from .views import index, by_otrasl, by_otrasl_2


urlpatterns = [
    path('', index),
    path('<int:otrasl_id>/', by_otrasl, name='by_otrasl'),
    path('<int:otrasl_id>/<int:podotrasl_id>/', by_otrasl_2, name='by_otrasl_2'),
]
