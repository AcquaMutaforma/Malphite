from django.urls import path
from . import views

app_name = "Malphite"
urlpatterns = [
    path('', views.index, name='index'),
    path('risposte/', views.risposte, name='risposte'),
    path('chiedi-elimina/<int:id>', views.chiediElimina, name='chiediElimina'),
]