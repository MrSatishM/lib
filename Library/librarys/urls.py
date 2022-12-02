from django.urls import path
from librarys import views

urlpatterns = [
    path('home/', views.home),
    path('add/', views.add),
    path('delete/<int:tid>',views.delete),
    path('update/<int:tid>',views.update),
    path('pricehtol/',views.pricehtol),
    path('priceltoh/',views.priceltoh),
    path('authoratoz/',views.authoratoz),
    path('authorztoa/',views.authorztoa),
    path('nonfiction/',views.nonfiction),
    path('fiction/',views.fiction),
    path('edited/',views.edited),
    path('reference/',views.reference),

]
