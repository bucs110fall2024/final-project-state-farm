import pygame
import src.controller as controller

def main():
    pygame.init()
    ctrl = controller.Controller()
    #Create an instance on your controller object
    #Call your mainloop
    ctrl.menuloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
