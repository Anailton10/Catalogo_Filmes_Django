from typing import Any
from django.db import models


class Adm(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self):
        return self.nome


