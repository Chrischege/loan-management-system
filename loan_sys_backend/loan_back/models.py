from django.db import models

#create a loan model for a loaning system
class Loan(models.Model):
    #loan id
    user_id = models.IntegerField(primary_key=True)
     #loan name
    loan_name = models.CharField(max_length=100)
    #loan amount
    loan_amount = models.IntegerField()
    #loan interest
    loan_interest = models.IntegerField()
    #loan duration
    loan_duration = models.IntegerField()
    #loan status
    loan_status = models.CharField(max_length=100)
    #loan_details
    loan_details = ("user_id" + "loan_name" + "loan_amount" + "loan_interest")

    def __str__(self):
        return self.loan_details


# create a users model for the loaning system
class Users(models.Model):
    #user id
    user_id = models.AutoField(primary_key=True)
    #user name
    user_name = models.CharField(max_length=100)
    #user email
    user_email = models.EmailField()
    #user password
    user_password = models.CharField(max_length=100)
    #user phone
    user_phone = models.CharField(max_length=100)
    #user address
    user_address = models.CharField(max_length=100)
    #user status
    user_status = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
    
# permissions model for the loaning system that will store information about the permissions granted to users


# create an borrowers model for a loan borrower for the loaning system 
class Borrowers(models.Model):
    #user_id to be the foreign key for the borrowers
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    #borrower name
    borrower_name = models.CharField(max_length=100)
    #borrower email
    borrower_email = models.EmailField()
    #borrower phone
    borrower_phone = models.CharField(max_length=100)
    #borrower address
    borrower_address = models.CharField(max_length=100)
    #borrower status
    borrower_status = models.CharField(max_length=100)

    def __str__(self):
        return self.borrower_name
    
# Applications table: This table will store information about loan applications submitted by borrowers. It might include fields such as application ID, borrower ID, loan ID, application date, status (approved, pending, rejected), and other application-related information.
# create an applications model for a loan application for the loaning system
class Applications(models.Model):
    #application id
    #user_id to be the foreign key for the applications
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    #application date
    application_date = models.DateField()
    #application status
    application_status = models.CharField(max_length=100)

    def __str__(self):
        return self.application_status

# create a payments model for a loan payment for the loaning system
class Payments(models.Model):
    #payment id
    # user_id to be the foreign key for the payments
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    #payment date
    payment_date = models.DateField()
    #payment amount
    payment_amount = models.IntegerField()
    #payment status
    payment_status = models.CharField(max_length=100)

    def __str__(self):
        return self.payment_status
    
    