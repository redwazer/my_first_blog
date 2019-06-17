from django.shortcuts import render
from django.core.mail import send_mail

from .forms import MailForm

def mailform(request):
	if (request.method =='POST'):

		form = MailForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			print("name", name)
			print("not cleaned", form['name'])

			email=form.cleaned_data['email']
			send_mail(
				' {}{}'.format(name, email),
				'test message',
				'redwazer7@gmail.com',
				['kairatawer@gmail.com', '150103076@stu.sdu.edu.kz', "diana.omarova2013@gmail.com"],
				fail_silently=False,
				)
			return render(request, 'mail_sending/result.html',{
					'name': form.cleaned_data['name'],
					'email': form.cleaned_data['email'],	
			})
	else:
		form = MailForm()
	return render(request, 'mail_sending/index.html', {'form' :form});
	# Create your views here.
