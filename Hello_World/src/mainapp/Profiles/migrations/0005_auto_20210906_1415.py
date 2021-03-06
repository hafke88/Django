# Generated by Django 3.2.7 on 2021-09-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0004_alter_profiles_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Gen.', 'Gen.'), ('Sen.', 'Sen.'), ('Mr.', 'Mr.'), ('Prof.', 'Prof.'), ('Rev.', 'Rev.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.')], max_length=60, null=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]
