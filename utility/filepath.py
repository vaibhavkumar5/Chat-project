user_profile_picture_path = 'profilepictures/profilepicture_{0}.png'
post_image_path = 'posts/{0}/post_{1}/{2}'
message_file_path = 'messages/{0}to{1}/{2}'

def User_Profile_Picture_Path(instance, filename):
	return user_profile_picture_path.format(instance.userid)

def Post_Image_Path(instance, filename):
	return post_image_path.format(instance.ByUser.userid, instance.PostId, filename)

def Message_File_Path(instance, filename):
	return message_file_path.format(instance.ByUser.userid, instance.ToUser.userid, filename)