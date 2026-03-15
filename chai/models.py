from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here
class ChaiVarity (models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KI','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='chais/')
    date_added= models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    
    def __str__(self):
        return str(self.name)
    
    
    #one to many relationship
    
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)   
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name} '   
    
#Many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varities = models.ManyToManyField(ChaiVarity,related_name='sotre')
    
    def __str__(self):
        return str(self.name) 
    
#one to one relationship

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_no = models.CharField(max_length=50)
    date_issued = models.DateField()
    
    def __str__(self):
        return f'Certificate {self.certificate_no}'
    