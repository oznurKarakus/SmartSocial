
from django.db import models
from django.utils.timezone import now

PLATFORM_CHOICES = [
    ('Instagram', 'Instagram'),
    ('TikTok', 'TikTok'),
    ('Twitter', 'Twitter'),
]

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    scheduled_time = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Select a scheduled posting time. Leave blank for immediate posting."
    )

    def __str__(self):
        return f"{self.title} - {self.platform}"

class PostTemplate(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('tiktok', 'Tiktok'),
        ('twitter', 'Twitter'),
    ]
    name = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='instagram')

    def __str__(self):
        return f"{self.title} ({self.get_platform_display()})"
