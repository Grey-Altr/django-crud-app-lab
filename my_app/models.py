from django.db import models
from django.contrib.auth.models import User

class Synth(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.PositiveBigIntegerField()
    synth_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.manufacturer})'
    
class SynthLog(models.Model):
    LOG_TYPES = [
        ('Repair', 'Repair'),
        ('Service', 'Service'),
        ('Mod', 'Modification'),
        ('Accessory', 'Accessory'),
    ]
    
    synth = models.ForeignKey(Synth, on_delete=models.CASCADE, related_name='logs')
    log_type = models.CharField(max_length=20, choices=LOG_TYPES)
    date = models.DateField()
    description = models.TextField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.log_type} for {self.synth.name} on {self.date}'
