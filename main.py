import pygame
import src.game as game

def main():
    pygame.init()
    g = game.Game()
    #Create an instance on your controller object
    #Call your mainloop
    g.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
