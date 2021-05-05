from django.db import models

# Create your models here.
class studentsdetail(models.Model):
    s_name = models.CharField(max_length=50)
    s_fname = models.CharField(max_length=50)
    dob = models.DateField()
    m_number = models.CharField(max_length=20)
    s_email = models.CharField(max_length=50)
    date_join = models.DateField()
    c_position = models.BooleanField(default=True)

def __str__(self):
    return self.s_name