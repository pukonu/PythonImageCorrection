from PIL import Image, ExifTags

# Image orientation correction for Python

image = Image.open(fully_qualified_filepath)
try:
    for key in ExifTags.TAGS.keys():
        if ExifTags.TAGS[key] == 'Orientation':
            exif = dict(image._getexif().items())

            if exif[key] == 3:
                image = image.rotate(180, expand=True)
            elif exif[key] == 6:
                image = image.rotate(270, expand=True)
            elif exif[key] == 8:
                image = image.rotate(90, expand=True)

            break

    image.save(fully_qualified_filepath)

except:
    traceback.print_exc()
