from django.db import models


# Create your models here.
class MIRFileModel(models.Model):
    """MIRFileModel.

    Handles .MIR files, parsing them and creating valid json"""

    mir_file = models.FileField(upload_to="mirs/")
    date_submitted = models.DateField(auto_now_add=True)
