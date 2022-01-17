# python3 -m pip install Pillow

def info_image(name_image):
    from PIL import Image
    from PIL.ExifTags import TAGS

    # open IMAGE
    image = Image.open(name_image)

    # extracting the exif metdata
    datas = image.getexif()
    
    for Tag_id in datas :

        # getting the tag name
        Tag_name = TAGS.get(Tag_id)

        # passing the Tag_id to get respective value
        Val = datas.get(Tag_id)
        print("{} : {}".format(Tag_name, Val))

