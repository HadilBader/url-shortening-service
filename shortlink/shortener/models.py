from django.db import models


class URL(models.Model):
    long_version = models.URLField(unique=True)
    short_version = models.URLField(unique=True, max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'''
            Original url: {self.long_version}
            Shortened version: {self.short_version}
        '''

