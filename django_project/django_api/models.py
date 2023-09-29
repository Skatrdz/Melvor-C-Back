from django.db import models


class PVE(models.Model):
    id = models.IntegerField("PVE_ID", max_length=240, primary_key=True)
    title = models.CharField("PVE_Title", max_length=20)
    lvlMax = models.IntegerField("PVE_LvlMax")
    currentLvl = models.IntegerField("PVE_CurrentLvl")
    exp = models.IntegerField("PVE_Exp")


    def __str__(self):
        return self.title
