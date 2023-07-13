
from django.urls import path
from .views import index, title_list, AlbumDetailView, AlbumDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', index, name='index'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='view_album'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)