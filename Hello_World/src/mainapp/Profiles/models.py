from django.db import models


TITLE_CHOICES = {
    ('Mr.','Mr.'),
    ('Mrs.','Mrs.'),
    ('Ms.','Ms.'),
    ('Dr.','Dr.'),
    ('Prof.','Prof.'),
    ('Rev.','Rev.'),
    ('Gen.','Gen.'),
    ('Sen.','Sen.'),
}

class Profiles(models.Model):
    title = models.CharField(max_length=60, choices=TITLE_CHOICES, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    username = models.CharField(max_length=60)

    objects = models.Manager()

    def __str__(self):
        return self.first_name

