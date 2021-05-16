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
    sex = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    fm_number = models.CharField(max_length=15)

    def __str__(self):
        return self.s_name


class yearclass(models.Model):
    year=models.IntegerField(primary_key=True,default=2021)

    def __str__(self):
        return str(self.year)

class months(models.Model):
    years = models.ForeignKey(yearclass,on_delete=models.CASCADE)
    student = models.ForeignKey(studentsdetail,on_delete=models.CASCADE)
    january = models.PositiveSmallIntegerField()
    february = models.PositiveSmallIntegerField()
    march = models.PositiveSmallIntegerField()
    april = models.PositiveSmallIntegerField()
    may = models.PositiveSmallIntegerField()
    june = models.PositiveSmallIntegerField()
    july = models.PositiveSmallIntegerField()
    august = models.PositiveSmallIntegerField()
    september = models.PositiveSmallIntegerField()
    october = models.PositiveSmallIntegerField()
    november = models.PositiveSmallIntegerField()
    december = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return str(self.student)
    
class teacherdetail(models.Model):
    t_name = models.CharField(max_length=50)
    t_fname = models.CharField(max_length=50)
    dob = models.DateField()
    m_number = models.CharField(max_length=20)
    s_email = models.CharField(max_length=50)
    date_hiring = models.DateField()
    c_position = models.BooleanField(default=True)
    sex = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    fm_number = models.CharField(max_length=15)
    salary = models.IntegerField()
    speciality = models.CharField(max_length=200)
    def __str__(self):
        return str(self.t_name)