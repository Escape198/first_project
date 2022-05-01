from django.db import models
from faker import Faker



fake = Faker()
text = fake.text()
number = fake.phone_number()


class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name='Department')
    description = models.TextField(verbose_name='Description')
    url = models.URLField(verbose_name='Website')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Member(models.Model):
    member = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Name')
    description = models.TextField(verbose_name='Description', default=text)
    photo = models.ImageField('Photo', upload_to='main/photos', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Phone', default='+' + number)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Feedback(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='My name')
    description = models.TextField(verbose_name='Description')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
