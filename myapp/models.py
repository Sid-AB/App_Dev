from django.db import models

# Create your models here.
class APTEST(models.Model):
     # Num: Auto-incrementing integer
    num = models.AutoField(primary_key=True)
    
    # Libelle: String field
    libelle = models.CharField(max_length=255)
    
    # AP: Float field
    ap = models.FloatField()
    
    # annee: Date field (only year)
    annee = models.DateField()

    def __str__(self):
        return f"{self.libelle} ({self.annee.year})"