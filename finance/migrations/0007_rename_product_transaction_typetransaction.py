# Generated by Django 5.0.2 on 2024-04-27 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_remove_transaction_tipe_transaction_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='product',
            new_name='typeTransaction',
        ),
    ]
