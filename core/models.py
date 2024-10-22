from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Titulo",
        unique=True
    )
    content = models.TextField(
        verbose_name='Conteúdo'
    )
    created_ad = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    tags = models.ManyToManyField(
        'Tag', 
        verbose_name='Tags', 
        related_name='posts'
    )
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name='Nome'
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name