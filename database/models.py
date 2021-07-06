from django.db import models
from django.contrib.auth.models import AbstractUser
import django.contrib.auth.validators
from utility import filepath
import os, glob, pytz, datetime, uuid

UTC = pytz.utc
datetimeNow = datetime.datetime.now(UTC)+datetime.timedelta(hours=5.5)

class User(AbstractUser):
	username = models.CharField(primary_key=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
	about = models.TextField(max_length=500, null=True, blank=True)
	number = models.IntegerField(null=True, blank=True, unique=True)
	profile_picture = models.ImageField(upload_to=filepath.User_Profile_Picture_Path, null=True, blank=True)
	userid = models.UUIDField(unique = True, default = uuid.uuid4, editable = False)

	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)
		if self.profile_picture.__str__() != '':
			path = self.profile_picture.path
			path = path.replace(path.split(os.sep)[-1], '')
			path = glob.glob(path + '*.png')
			path.remove(self.profile_picture.path)
			for file in path:
				os.remove(file)

class Post(models.Model):
	PostId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	ByUser = models.ForeignKey(User, on_delete=models.CASCADE)
	DateTimePosted = models.DateTimeField(default=datetimeNow, editable=False)
	Title = models.CharField(max_length=200)
	Content = models.TextField(max_length=1000, null=True, blank=True)
	Image = models.ImageField(upload_to=filepath.Post_Image_Path, null=True, blank=True)
	Likes = models.ManyToManyField(User, related_name="Likes")

	def __str__(self):
		return self.PostId.__str__()

class StarredPost(models.Model):
	Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="PostStarred")
	ByUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="PostStarredByUser")

class Message(models.Model):
	MessageId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	ByUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageByUser")
	ToUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageToUser")
	Content = models.TextField(null=True, blank=True)
	File = models.FileField(upload_to=filepath.Message_File_Path, null=True, blank=True)

class StarredMessage(models.Model):
	Message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="MessageStarred")
	ByUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageStarredByUser")