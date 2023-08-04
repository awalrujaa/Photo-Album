from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', views.Home.as_view(), name = 'home'),
    path('home/', views.Home.as_view(), name = 'home'),
    path('AddTitleView/', views.AddTitleView.as_view(), name = 'AddTitleView'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)