from django.db import models

# Create your models here.


class App_User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="user")

    def __hash__(self) -> int:
        return hash((self.username, self.role))
    
class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_date = models.CharField(max_length=20, null=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.CharField(max_length=5000)
    user = models.CharField(max_length=100)
    
    def __hash__(self) -> int:
        return hash((self.blog_id, self.blog_content, self.blog_title))
    