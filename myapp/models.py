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
class etat_project(models.Model):
    id_etat=models.IntegerField(primary_key=True)
    nom_etat=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.id_etat

class project(models.Model):
    id_project=models.IntegerField(primary_key=True)
    nom_project=models.CharField(max_length=150)
    etablissement_project=models.CharField(max_length=150)
    definition_project=models.TextField()
    date_chng=models.DateField()
    etat_project=models.ForeignKey(etat_project,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id_project} {slef.nom_project}"

class sector(models.Model):
    id_sect=models.IntegerField(primary_key=True)
    nom_sect=models.CharField(max_length=100)
    id_project=models.ForeignKey(project,on_delete=models.CASCADE)
    def __str__(self):
        return slef.id_sect

class operation(models.Model):
    id_libelle_op=models.CharField(max_length=100,primary_key=True)
    num_op=models.CharField(max_length=100)
    object_vise_po=models.TextField()
    notifcation_an_MF_op=models.TextField()
    indiv_an_op= models.DateField()
    AP_init_op=models.FloatField()
    AP_real_op=models.FloatField(default=0.0)
    cum_AP_eng_an_op=models.FloatField(default=0.0)
    cum_AP_pai_an_op=models.FloatField(default=0.0)
    taux_real_ph_an_op=models.FloatField(default=0.0)
    date_cre_op=models.DateField()
    id_project=models.ForeignKey(project,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id_libelle_op} ({self.num_op})"
