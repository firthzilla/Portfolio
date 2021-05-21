from django.db import models



class BlogPost(models.Model):
    class Meta:
        # ordered by pub_date descending when retrieving
        ordering = ['-pub_date']

    CATEGORY_CHOICES = (
        ('programming', 'Programming'),
        ('coding', 'Coding'),
        ('web development', 'Web Development'),
        ('python', 'Python'),
        ('webdev', 'WebDev'),
    )
    title = models.CharField(max_length=150)
    body0 = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    last_edit_date = models.DateTimeField('last edited', auto_now=True)
    slug = models.SlugField(max_length=200, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    body1 = models.TextField(blank=True)
    body2 = models.TextField(blank=True)
    body3 = models.TextField(blank=True)
    coverImage = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True)
    image0 = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title


