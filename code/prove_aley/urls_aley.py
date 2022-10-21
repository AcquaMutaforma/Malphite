from django.urls import path

import views_aley as views

app_name = "Malphite"
urlpatterns = [
    path('', views.index, name='index'),
    path('risposte/', views.risposte, name='risposte'),
    path('chiedi-elimina/<int:id>', views.chiediElimina, name='chiediElimina'),
]
