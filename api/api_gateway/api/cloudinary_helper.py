import cloudinary.uploader

def upload_image(photo):
    if (photo != None):
        upload_photo = cloudinary.uploader.upload(photo, 
            transformation = [
                {'width': 600, 'height': 350, 'crop': 'fit'}, 
            ]
        )
        photo_url = upload_photo['url']

    return photo_url