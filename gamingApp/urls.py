
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('home', views.index, name='index'),
    path('signup', views.signupPage, name='signupPage'),
    #Game Section
    path('addGame', views.addGame, name='addGame'),
    path('viewGame/<str:id>', views.viewGame, name='viewGame'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
