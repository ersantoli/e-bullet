from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('aluno/', views.aluno, name="aluno"),
    path('testif/', views.testif, name="testif"),
    path('logout/', views.logout_user, name="logout"),
   # path('register/', views.register_user, name='register'),
    path('add_record/', views.add_record, name='add_record'),
   # path('add_notas/', views.add_notas, name="add_notas"),
    path('boletim/', views.boletim_view, name="boletim_view"),
    path('test/<str:matricula>/', views.test, name="test"),
   # path('add_aluno/', views.add_aluno, name="add_aluno"),
    path('testnotas/<str:matricula>/', views.testnotaspage, name="testnotas"),
    path('att_record/<str:matricula>/', views.att_record, name="att_record"),
    path('att_notas/<str:matricula>/', views.att_notas, name="att_notas"),
    path('delete_record/<str:matricula>/', views.delete_record, name="delete_record"),
    path('boletim_list/<str:matricula>/', views.boletim_list, name='boletim_list'),
    path('boletim/create/', views.boletim_create, name='boletim_create'),
    path('matricula_search/', views.matricula_search, name='matricula_search'),
    

   




]