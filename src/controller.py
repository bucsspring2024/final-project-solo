import pygame
from src.model import LotteryModel
from src.view import LotteryView

class Controller:
    def __init__(self):
        self.model = LotteryModel()
        self.state = 'START' #Creates State-Dependent Screens, and starts the game at 'START' screen.
        self.last_message = '' #Only used in self.state == 'PLAY_GAME'
        self.color = '' # Same as last_message
        self.last_message2 = '' # Same as last_message
        self.input_locked = False
        self.running = True  
        self.barcode_scratched = False
        self.winnings_displayed = False

    def check_number(self):
        # For self.state == 'PLAY_GAME'; checks if the user's typed input is a number, and if so that number should be 5 or higher because the cheapest ticket is $5. 
        number_text = self.model.user_text
        if number_text.strip().isdigit():
            number = int(number_text)
            if number < 5:
                self.last_message = 'NEED AT LEAST $5'
                self.last_message2 = 'INSUFFICIENT FUNDS'
                self.color = 'red'
                return False
            else:
                self.last_message = 'PLEASE SELECT A TICKET'
                self.last_message2 = ''
                self.color = 'green'
                self.input_locked = True # Sets the user's inital cash amount. 
                return True
        else:
            self.last_message = 'PLEASE ENTER A NUMBER' # If user enters nothing.
            self.last_message2 = 'INVALID INPUT!'
            self.color = 'red'
            return False
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            
        elif self.state == 'START':
            # First few statements reset values to clear data from the previous game
            self.model.winnings = 0
            self.input_locked = False
            self.model.user_text = ''
            self.last_message = '' # Resets the last_message text
            self.view.draw_start_screen(self.model.score_history())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.buttons['play'].collidepoint(event.pos):
                    self.state = 'PLAY_GAME'  # Proceed to game
                elif self.view.buttons['exit'].collidepoint(event.pos):
                    self.state = 'CONFIRM_EXIT' # Proceed to confirm_exit screen

        elif self.state == 'CONFIRM_EXIT':
            # Asks the user if they are certain that they want to exit the game
            self.view.draw_confirm_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.confirmbuttons['yes'].collidepoint(event.pos):
                    self.state = 'Secret'
                elif self.view.confirmbuttons['no'].collidepoint(event.pos):
                    self.state = 'START'

        elif self.state == 'Secret':
            # Secret screen to congratulate them for not being a gambler.
            self.view.draw_secret_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.rects['secret_box'].collidepoint(event.pos):
                    self.running = False

        elif self.state == 'PLAY_GAME':
            # Creates screen for self.state == 'PLAY_GAME', and creates the events for the screen.
            self.barcode_scratched = False # Resets barcode state
            self.view.draw_play_screen()
            self.view.updated_display(self.model.user_text, self.last_message, self.color, self.last_message2)
            if event.type == pygame.MOUSEBUTTONDOWN and self.view.rects['exit_text'].collidepoint(event.pos):
                self.state = 'END_GAME'# Brings user to end_game screen.
            elif event.type == pygame.KEYDOWN and not self.input_locked:
                if event.key == pygame.K_BACKSPACE:
                    self.model.remove_char()
                elif event.key == pygame.K_RETURN:
                    self.check_number() # Calls function to see if the user's typed input is greater than or equal to 5; and sets that amount if self.input_locked = True
                elif event.unicode.isdigit():
                    self.model.add_char(event.unicode) # If user's typed input is a number, then add the input into model data for user_text.
            elif self.input_locked and event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.gamebuttons['binghamton_pot'].collidepoint(event.pos) and int(self.model.user_text) >= 10:
                    self.state = 'POT'
                    self.model.purchase_big_pot_ticket() # Substracts the ticket cost ($10) from the user_text, giving them a new balance.
                elif self.view.gamebuttons['binghamton_pot'].collidepoint(event.pos) and int(self.model.user_text) < 10:
                    self.last_message = 'NOT ENOUGH FUNDS'
                    self.color = 'red'
                elif self.view.gamebuttons['seawolves_jackpot'].collidepoint(event.pos) and int(self.model.user_text) >= 5:
                    self.state = 'WOLVES'
                    self.model.purchase_seawolves_jackpot() # Substracts the ticket cost ($5) from the user_text, giving them a new balance.
                elif self.view.gamebuttons['seawolves_jackpot'].collidepoint(event.pos) and int(self.model.user_text) < 5:
                    self.last_message = 'NOT ENOUGH FUNDS'
                    self.color = 'red'

        elif self.state == 'POT':  
            #Creates Binghamton Pot Ticket Screen
            self.view.draw_text()
            self.view.draw_fake_barcode(self.barcode_scratched)

            # Update the display continuously with the latest winnings calculated.

            if event.type == pygame.MOUSEMOTION:
                if self.view.rects['barcode'].collidepoint(event.pos):
                    self.barcode_scratched = True
                    #reveals barcode
                self.view.scratching(event, scratching=True) # Allow "scratching" effect.

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the barcode is revealed and the user clicks on the next page rectangle, bring them back to PLAY_GAME screen
                if self.view.rects['exit'].collidepoint(event.pos) and self.barcode_scratched: 
                    if not self.winnings_displayed: 
                        # Confirm and add the last calculated winnings only once when the user clicks the exit area.
                        self.model.binghamton_pot_winnings(self.last_winnings) 
                        self.view.display_winnings(self.last_winnings)  # Ensure display matches the final winnings
                    # Reset the game state and prepare for a new game or exit
                    self.model.reset_pot_ticket() # Reset numbers for next binghamton pot ticket
                    self.view.reset_surfaces() # Reset the scratched surfaces (unscratch all the boxes)
                    
                    self.state = 'PLAY_GAME'
            self.last_winnings = self.view.update_scratching_surface(self.model.winning_numbers, self.model.your_numbers_with_values)
            # Updates the "scratched" ticket display continously
            
        elif self.state == 'WOLVES':
            # Creates screen for the Stony Brook SeaWolves Ticket.
            if not self.winnings_displayed: # Ensures winnings is only calculated once.
                self.view.draw_brook_surface(self.model.jackpot_numbers, self.model.jackpot_ball_number, self.model.your_jackpot_numbers, self.model.your_jackpot_ball_number)
                self.view.display_winnings(self.model.calculate_winnings())
                self.winnings_displayed = True
            elif event.type == pygame.MOUSEMOTION and self.view.rects['barcode'].collidepoint(event.pos):
                self.barcode_scratched = True # Again reveals barcode
            self.view.draw_fake_barcode(self.barcode_scratched)
            if self.barcode_scratched == True and event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.rects['exit'].collidepoint(event.pos):
                    self.model.reset_wolves_ticket() # Resets the numbers for the next seawolves ticket
                    self.winnings_displayed = False
                    self.state = 'PLAY_GAME'
                    return False
                
        elif self.state == 'END_GAME':
            # Create END GAME screen and display the total winnings, also asks if the user wants to replay or quit the game
            self.view.draw_end_screen(self.model.winnings)
            if event.type == pygame.MOUSEBUTTONDOWN and self.view.end_buttons['PLAY AGAIN'].collidepoint(event.pos):
                self.model.score_history()
                self.state = 'START'
            elif event.type == pygame.MOUSEBUTTONDOWN and self.view.end_buttons['EXIT'].collidepoint(event.pos):
                self.running = False

    def main_loop(self):
        # Continously runs the game until user quits
        screen = pygame.display.set_mode((800, 800))
        self.view = LotteryView(screen)
        while self.running:
            for event in pygame.event.get():
                self.handle_events(event)
                pygame.display.flip()  # Update the display after each event
        pygame.quit()