# Main.py

# Imports
import pygame
from controller import Controller

# Main function
def main():
    pygame.init()
    controller = Controller()
    controller.main_loop()

# Calling main function
if __name__ == "__main__":
    main()