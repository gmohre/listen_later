from django.conf.urls import patterns, url
from audio import views

urlpatterns = patterns('', 
	url(r'^input_submit', views.add_audio, name='add_audio'),
	url(r'^input', views.audio_input_form,name='audio_input_form'),
	)