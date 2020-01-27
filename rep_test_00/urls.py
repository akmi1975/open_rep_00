from django.urls import path
from .views import index, by_otrasl, new_selection


urlpatterns = [
    path('', index),
    path('<int:otrasl_id>/<int:podotrasl_id>/<int:rayon_id>/<int:nsp_id>/', by_otrasl),
    path('<int:vid_sel>/<int:vid_1_id>/<int:pod_vid_1_id>/<int:vid_2_id>/<int:pod_vid_2_id>/', new_selection),

]
