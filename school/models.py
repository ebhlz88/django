from django.db import models

# Create your models here.
class studentsdetail(models.Model):
    rollnbr = models.BigAutoField(primary_key=True)
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
    january = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    february = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    march = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    april = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    may = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    june = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    july = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    august = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    september = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    october = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    november = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    december = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    
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

class teachpaymonths(models.Model):
    years = models.ForeignKey(yearclass,on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(teacherdetail,on_delete=models.CASCADE)
    january = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    february = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    march = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    april = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    may = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    june = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    july = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    august = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    september = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    october = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    november = models.PositiveSmallIntegerField(blank=True,null=True,default=0)
    december = models.PositiveSmallIntegerField(blank=True,null=True,default=0)


class schoolclasses(models.Model):
    standardname = models.CharField(max_length=100)
    def __str__(self):
        return self.standardname
class subjects(models.Model):
    subjectname = models.CharField(max_length=100)
    def __str__(self):
        return self.subjectname
class marks(models.Model):
    years = models.ForeignKey(yearclass,on_delete=models.DO_NOTHING)
    standard = models.ForeignKey(schoolclasses,on_delete=models.DO_NOTHING)
    subjectname = models.ForeignKey(subjects,on_delete=models.DO_NOTHING)
    student = models.ForeignKey(studentsdetail,on_delete=models.CASCADE)
    subjectmarks = models.PositiveSmallIntegerField()
    def __str__(self):
        return str(self.student)
   
