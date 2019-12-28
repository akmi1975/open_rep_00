from django.urls import path
from .views import index, by_otrasl


urlpatterns = [
    path('', index),
    path('<int:otrasl_id>/<int:podotrasl_id>/<int:rayon_id>/<int:nsp_id>/', by_otrasl),
]
