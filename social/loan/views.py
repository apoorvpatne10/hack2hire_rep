from django.shortcuts import render, redirect, get_object_or_404
from .models import Rule, MyUser
from .forms import RulesForm, UIDForm
import csv
import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "apoorvwatsky@gmail.com"
password = 'Testing@999'


def check_status(request):
    if request.method == 'POST':
        form = UIDForm(request.POST)

        if form.is_valid():
            get_uid = form.cleaned_data['uid']

            get_user = MyUser.objects.get(uid=get_uid)
            receiver_email = get_user.email
            if get_user.approved:
                approve = True
                message = "Loan approved! Congrats!"
            else:
                approve = False
                message = "Sorry couldnt happen :("

            context = ssl.create_default_context()

            # Try to log in to server and send email
            try:
                server = smtplib.SMTP(smtp_server,port)
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            except Exception as e:
                # Print any error messages to stdout
                print(e)
            finally:
                server.quit()
                
            print('EMAIL SENT.')
            return redirect('home')
    else:
        form = UIDForm()

    return render(request, 'loan/check_approval.html', {'form': form})


def index(request):
    context= {}
    return render(request, 'loan/home.html', context)

def display_rules(request):
    my_rule = Rule.objects.get(pk=1)
    context = {
        'my_rule': my_rule
    }
    return render(request, 'loan/display_rules.html', context)

def rules(request, id=None):
    my_rule = Rule.objects.get(pk=1)
    if id:
        rule = get_object_or_404(Rule, pk=id)
    else:
        rule = Rule()

    form = RulesForm(request.POST or None, instance=rule)
    if request.POST and form.is_valid():
        form.save()
        return redirect("display_rules")

    context = {
        'my_form': form,
        'my_rule': my_rule
    }
    return render(request, 'loan/rules.html', context)
