from django.db import models


# Create your models here.
# User Model
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    sexe = models.CharField(null=True, max_length=50)
    phone = models.CharField(null=True, max_length=50)
    social_security_number = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name + ' ' + self.last_name




# Tutor Model
class UserTutor(models.Model):
    user_id = models.ForeignKey(User, related_name="tutored",on_delete=models.CASCADE)
    tutor_id = models.ForeignKey(User, related_name="tutor", on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()


    def __str__(self):
        return self.tutor_id.first_name + ' ' + self.tutor_id.last_name




# Pathology Model
class Pathology(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()

    def __str__(self):
        return self.name + ' - ' + self.category




# UserPathology Model
class UserPathology(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    pathology_id = models.ForeignKey(Pathology,on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    severity = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.pathology_id.name + ' - ' + self.user_id.first_name + ' ' + self.user_id.last_name




# UserPathology Model
class HealthMeasurements(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    pathology_id = models.ForeignKey(Pathology,on_delete=models.CASCADE)
    measurement_type = models.CharField(max_length=50)
    measurement_date = models.DateTimeField()
    value = models.FloatField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.measurement_type + ' - ' + self.user_id.first_name + ' ' + self.user_id.last_name + ' - ' + self.measurement_date.__str__()