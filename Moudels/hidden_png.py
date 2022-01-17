from stegano import lsbset
from stegano.lsbset import generators

class PNG :

    def __init__(self, name_image):
        
        self.name_image = name_image

    def message_png(self, secret_message, new_name_image):
        
        # Hide message in photo ( PNG )
        Hide_png = lsbset.hide(self.name_image, secret_message, generators.eratosthenes())
        # Save Image
        Hide_png.save(new_name_image)

    def show_massage_png(self):

        # Show message in PNG 
        Photo = lsbset.reveal(self.name_image, generators.eratosthenes())
        print(Photo)
