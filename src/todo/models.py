from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=150)
    done = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Todo."""

        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """Unicode representation of Todo."""
        return self.content
