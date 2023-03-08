from django.contrib import admin

# Register your models here.
from loan_back import models

admin.site.register(models.Loan)
admin.site.register(models.Users)
admin.site.register(models.Borrowers)
admin.site.register(models.Applications)

