from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, Image

from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from django.core.exceptions import ValidationError

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'
    context_object_name = 'album'

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_delete.html'
    success_url = reverse_lazy('index')

# Create your views here.
def index(request):
    
    album_list = Album.objects.all()
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        query_dict = request.POST
        title = query_dict['title']  # Correct
        
        album_list = Album.objects.all()
        new_album = Album(title=title)
        
        new_album.save()
        

        for file in files:
            new_image = Image(src=file, album=new_album)
            try:
                new_image.full_clean()
            except ValidationError as e:
                print(e.message_dict)
                errors = e.message_dict['src']
                return render(request, 'index.html', {'album_list': album_list, 'errors': errors, 'error_file': file})
            # new_image.validate()
            new_image.save()
        album_list = Album.objects.all()
        

        return render(request, 'index.html', {'album_list': album_list},)
    else:

        return render(request, 'index.html', {'album_list': album_list})
    
def title_list(request):
    album_list = Album.objects.all()
    context ={ 'album_list': album_list}
    return render(request, 'title_list.html', context)
    # return HttpResponse("List of Title")

def album(request):


    return 'Album'