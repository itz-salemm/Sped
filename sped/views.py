from django.shortcuts import render, redirect

# Create your views here.

#imports 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

#Database import and smart_open
import pymysql
from smart_open import smart_open


#Initializing the database variable
endpoint = 'spedd.crky75dionik.us-east-2.rds.amazonaws.com'
username = 'admindatabase'
password = 'Admindatabase'
database_name = 'spedd'


def upload_file(request):
	#connetion to the database
	connection = pymysql.connect(host=endpoint, user=username, password=password, db=database_name)
	mycursor = connection.cursor()

	#recieve post requests and save form
	form = UploadFileForm()
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			#read the file 
			with smart_open('s3://sped-1250/SPED.txt', 'rb') as s3_source:
				for line in s3_source:
					line = line.decode('cp1250')

					#Insert data into RDS table
					if line[1:5] == "I250":
						grade_data = line.strip().replace("||", "|NULL|").split('|')
						mycursor.execute(f'INSERT INTO SPED VALUES ("{grade_data[1]}" ,"{grade_data[2]}" , "{grade_data[3]}" , "{grade_data[4]}" ,"{grade_data[5]}", "{grade_data[6]}","{grade_data[7]}","{grade_data[8]}")')
						connection.commit()
		else:
			form = UploadFileForm()


	context = {'form': form}
	return render(request, 'sped/index.html', context)