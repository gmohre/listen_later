from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from audio.models import Audio

def add_audio(request):
	a = Audio(source_url=request.POST['source_url'], page_title=request.POST['page_title'], clip_title=request.POST['clip_title'], listened=False)
	a.save()
	return HttpResponse("Sure, that submitted.")

def audio_input_form(request):
	return render(request,'audio/input.html')

def audio_list(request):
    clip_list = Audio.objects.all().order_by('-date_time')
    context = {'clip_list': clip_list}
    return render(request, 'audio/list.html', context)

def delete_audio(request):
	deleted_file = Audio.objects.filter(id=request.POST['id'])
	deleted_file.delete()
	return HttpResponse(request.POST['id'])