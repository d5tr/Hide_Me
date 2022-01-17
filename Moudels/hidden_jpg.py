# python3 -m pip install stegano
from stegano import exifHeader
from colorama import Fore

class JPG :
    
    def __init__(self, name_image):
        self.name_image = name_image


    def massage_jpg(self, new_name_image, massage):
        
        # hidden massage    name_image - new name image - massage
        ST = exifHeader.hide(self.name_image, new_name_image, secret_message=massage)
        # decode massage 
        des = exifHeader.reveal(new_name_image).decode('UTF-8')
        print('\nDone hidden massage => ', des, f'{Fore.WHITE}')

    def file_jpg(self, new_name_images, massage_in_file):

        ST = exifHeader.hide(self.name_image, new_name_images, secret_file=massage_in_file)
        des = exifHeader.reveal(new_name_images).decode('UTF-8')
        print('\nDone hidden massage => ', des, f'{Fore.WHITE}')

    def show_massage_jpg(self):
        
        Name = str(self.name_image)
        des = exifHeader.reveal(Name).decode('UTF-8')
        print(f'\nMassage is ==> {Fore.GREEN}', des, f'{Fore.WHITE}')