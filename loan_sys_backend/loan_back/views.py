from django.shortcuts import render

# Create your views here.
# create views from the models created
from django.http import HttpResponse
from django.shortcuts import render
from .models import Loan, Users, Borrowers, Applications

#create a view for base template
def base_view(request):
    return render(request, 'loan_back/home.html')

# create a view for the loan model
def loan_view(request):
    loan = Loan.objects.all()
    return render(request, 'loan_back/loan.html', {'loan': loan})

# create a view for the users model
def users_view(request):
    users = Users.objects.all()
    return render(request, 'loan_back/users.html', {'users': users})

# create a view for the borrowers model
def borrowers_view(request):
    borrowers = Borrowers.objects.all()
    return render(request, 'loan_back/borrowers.html', {'borrowers': borrowers})

# create a view for the applications model
def applications_view(request):
    applications = Applications.objects.all()
    return render(request, 'loan_back/applications.html', {'applications': applications})

