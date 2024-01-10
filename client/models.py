from django.db import models


class Client(models.Model):
    GENDER = (
        ('O', "Other"),
        ('M', "Male"),
        ('F', "Female"),
    )
    MEMBERSHIP_STATUS = (
        ('R', "Regular"),
        ('P', "Premium"),
        ('G', "Gold"),
        ('D', "Diamond"),
    )

    id = models.CharField(max_length=100, primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER)
    password = models.TextField()
    status = models.CharField(max_length=5, choices=MEMBERSHIP_STATUS, default='R')
    avatar = models.ImageField(blank=True, upload_to="client/avatar")
    joined = models.DateField(auto_now=True)

    def get_status(self):
        for i in self.MEMBERSHIP_STATUS:
            if self.status == i[0]:
                return i[1]
