from django.urls import path
from . import views

app_name = "Malphite"
urlpatterns = [
    path('', views.index, name='index'),
    path('risposte/', views.risposte, name='risposte'),
    path('chiediElimina/<idr>', views.chiediElimina, name='chiediElimina'),
    path('eliminaConfermato/<idr>', views.eliminaConfermato, name='eliminaConfermato'),
    path('attivaSveglia/', views.attivaSveglia, name='attivaSveglia'),
    path('spegniSveglia/', views.spegniSveglia, name='spegniSveglia'),
    path('modificaSveglia/', views.modificaSveglia, name='modificaSveglia'),
    path('modificaUserId/', views.modificaUserId, name='modificaUserId'),
]