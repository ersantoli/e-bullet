
from django.contrib import admin
from django.urls import path,include

from produtos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),
    #path('register/', views.register_user, name='register'),

   # path('aluno', include('produtos.urls')),
    #path('notas', include('produtos.urls')),
    #path('materias', include('produtos.urls')),
    #path('boletim', include('produtos.urls')),
    #path('test/<int:pk>', include('produtos.urls')),
   
   
]
