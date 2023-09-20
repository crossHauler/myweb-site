from django.db import models

# Create your models here.
from django.db import models

class Artwork(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="Martin J Walls")
    description = models.TextField()
    youtube_link = models.CharField(max_length=255, blank=True, null=True)

    def get_embedded_youtube_link(self):
        if self.youtube_link:
            video_id = None
            if "youtu.be" in self.youtube_link:
                video_id = self.youtube_link.split("/")[-1]
            elif "watch?v=" in self.youtube_link:
                video_id = self.youtube_link.split("https://www.youtube.com/embed/SuyZD4IwK7k")[1].split("&")[0]
            
            if video_id:
                return f"https://www.youtube.com/embed/{video_id}"
            
        return None

    def __str__(self):
        return self.title



my_title_standard = "'Eagle Head' by Martin J Walls (@mjwalls_art) - TikTok Live(PRINT)"