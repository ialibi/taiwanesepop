from django.shortcuts import render

def index(request):
	return render(request, 'index.html')
	#defining variables
	number=6
	songname="Happy Christmas!"
	return render(request, 'index.html',{
		'number': number,
		'songname': songname,
	})
