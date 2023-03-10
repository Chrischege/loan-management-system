# Generated by Django 4.1.7 on 2023-03-06 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan_back', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='application_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='borrowers',
            old_name='borrower_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='loan_id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='payments',
            old_name='payment_id',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='borrower_id',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='loan_id',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='application_id',
        ),
    ]
