from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(help_text="Percentage (0-100)")
    icon = models.ImageField(upload_to="skill_logo/", blank=True)

    def __str__(self):
        return self.name
