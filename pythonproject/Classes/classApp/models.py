from django.db import models

# creating class
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, null=True)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField(max_length=10)

    objects = models.Manager()

    def __str__(self):
        return self.title