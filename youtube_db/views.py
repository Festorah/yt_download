from django.shortcuts import render, redirect
from pytube import YouTube
import os

url = ''




def home(request):
	return render(request, 'youtube_db/home.html')

def yt_download(request):
	global url
	url = request.GET.get('url')
	yt = YouTube(url)
	title = yt.title
	print(title)
	thumbnail = yt.thumbnail_url
	video = yt.streams.filter(progressive=True)
	embed = url.replace('watch?v=', 'embed/')
	context = {
		'video': video,
		'title': title,
		'thumbnail':thumbnail,
		'embed': embed,
	}
	return render(request, 'youtube_db/download.html', context)

def complete_download(request, resolution):
	global url
	homedir = os.path.expanduser("~")
	dirs = homedir + '/Downloads'
	if request.method == "POST":
		YouTube(url).streams.get_by_resolution(resolution).download(dirs)
		return render(request, 'youtube_db/complete_download.html')
	else:
		return render(request, 'sorry.html')

	