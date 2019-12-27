from django.urls import path
from .views import index, by_otrasl, by_otrasl_2, by_otrasl_4


urlpatterns = [
    path('', index),
    path('<int:otrasl_id>/', by_otrasl, name='by_otrasl'),
    path('<int:otrasl_id>/<int:podotrasl_id>/', by_otrasl_2, name='by_otrasl_2'),
    path('<int:otrasl_id>/<int:podotrasl_id>/<int:rayon_id>/<int:nsp_id>/', by_otrasl_4, name='by_otrasl_4'),
]
