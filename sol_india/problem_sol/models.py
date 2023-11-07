from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class publicPOST(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    post_content=models.TextField(default=None)
    post_image=models.ImageField(upload_to="", default=None, null=True)
    is_question=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=timezone.now()+timedelta(hours=5,minutes=30), null=True)

    def __str__(self):
        return self.user_id.username

class publicCOMMENT(models.Model):
    post_id=models.ForeignKey(publicPOST,on_delete=models.CASCADE, default=0)
    commenter_details=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(default="hello", null=True, blank=True)

    def __str__(self):
        return self.commenter_details.username
    
class publicLIKE(models.Model):
    post_id=models.ForeignKey(publicPOST,on_delete=models.CASCADE, default=0)
    LIKER_details=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.LIKER_details.username
    