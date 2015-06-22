from django.db import models

class BitcoinInfo(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    last_checked = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.price

    def save(self, *args, **kwargs):
        super(BitcoinInfo, self).save(*args, **kwargs)