# libraries
from colorama import Fore
from Core.banner import *
from Moudels.show_in_image import info_image
from Moudels.hidden_jpg import *
from Moudels.hidden_png import *
from sys import platform
import os 
from time import sleep


class Hide_me :
    
    def system_clear(self):
        # what is your system ?
        if platform == 'linux':
            os.system('clear')
        elif platform == 'win32':
            os.system('cls')        

    def ChooseX(self):
        # choose system ?
        Choose = input(f'{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Choose number : ')
        return Choose

    def your_choice(self, number, clear):
        
        if number == '1' :
            
            Name = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter name Image : ')
            info_image(Name)
        
        elif number == '2':
            
            def JPG_Hide():

                # clear screen and print banner
                clear
                JPG_banner()
                
                # Choose what you want 
                choose_jpg = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Choose number : ')

                if choose_jpg == '1':
                   
                    Name = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter name Image : ')
                    New_name = input(f'{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter new for name Image : ')
                    Massage = input(f'{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter massage : ')
                    JPG(Name).massage_jpg(New_name, Massage)
                
                elif choose_jpg == '2':
                    
                    Name = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter name Image : ')
                    New_name = input(f'{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter new for name Image : ')
                    name_file = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter name file : ')
                    JPG(Name).file_jpg(New_name, name_file)

                elif choose_jpg == '3':

                    Name = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter name Image : ')
                    JPG(Name).show_massage_jpg()
                                
                else :

                    print('\n Erorr : This number does not exist')
                    sleep(1.5)
                    
                    if platform == 'linux':
                        os.system('clear')
                    elif platform == 'win32':
                        os.system('cls') 

                    JPG_Hide()
            JPG_Hide()
            
        elif number == '3':
                
            clear
            PNG_banner()

            choose_png = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Choose number : ')

            if choose_png == '1':

                Name = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter name Image : ')
                New_name = input(f'{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter new for name Image : ')
                Massage = input(f'{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter massage : ')
                PNG(Name).message_png(Massage, New_name)

            elif choose_png == '2':

                Name = input(f'\n{Fore.RED}[{Fore.CYAN}?{Fore.RED}]{Fore.WHITE} Enter name Image : ')
                PNG(Name).show_massage_png()

            
    # for run tool
    system_clear('')
    banner()
    CX = ChooseX('')
    your_choice('',CX, system_clear(''))

# start 
Hide_me()


