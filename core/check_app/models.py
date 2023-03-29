from django.db import models

class Printer(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    check_type = models.CharField(max_length=100)
    point_id = models.IntegerField()

    def __str__(self):
        return self.name

class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(max_length=130)
    order = models.JSONField(default=dict)
    status = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdf', blank=True)

    def __str__(self):
        return self.type

