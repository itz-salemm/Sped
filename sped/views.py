from django.shortcuts import render, redirect

# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def upload_file(request):
	form = UploadFileForm()
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		else:
			form = UploadFileForm()

	context = {'form': form}
	return render(request, 'sped/index.html', context)