import pygame
from model import LotteryModel
from view import LotteryGameScreens

class Controller:
    def __init__(self):
        self.model = LotteryModel()
        self.view = None
        self.state = 'START'
        self.last_message = ''
        self.color = ''
        self.last_message2 = ''
        self.input_locked = False
        self.running = True  
        self.barcode_scratched = False
        self.winnings_displayed = False

    def check_number(self):
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
                self.input_locked = True
                return True
        else:
            self.last_message = 'PLEASE ENTER A NUMBER'
            self.last_message2 = 'INVALID INPUT!'
            self.color = 'red'
            return False
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif self.state == 'PLAY_GAME':
            self.view.draw_play_screen()
            self.view.updated_display(self.model.user_text, self.last_message, self.color, self.last_message2)
            if event.type == pygame.MOUSEBUTTONDOWN and self.view.exit_text_rect.collidepoint(event.pos):
                self.state = 'END_GAME'
            elif event.type == pygame.KEYDOWN and not self.input_locked:
                if event.key == pygame.K_BACKSPACE:
                    self.model.remove_char()
                elif event.key == pygame.K_RETURN:
                    self.check_number()
                elif event.unicode.isdigit():
                    self.model.add_char(event.unicode)
                    # Call updated_display whenever the text changes
            elif self.input_locked and event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.gamebuttons['binghamton_pot'].collidepoint(event.pos) and int(self.model.user_text) >= 10:
                    self.state = 'POT'
                    self.model.purchase_big_pot_ticket()
                elif self.view.gamebuttons['binghamton_pot'].collidepoint(event.pos) and int(self.model.user_text) < 10:
                    self.last_message = 'NOT ENOUGH FUNDS'
                    self.color = 'red'
                elif self.view.gamebuttons['seawolves_jackpot'].collidepoint(event.pos) and int(self.model.user_text) >= 5:
                    self.state = 'WOLVES'
                    self.model.purchase_seawolves_jackpot()
                elif self.view.gamebuttons['seawolves_jackpot'].collidepoint(event.pos) and int(self.model.user_text) < 5:
                    self.last_message = 'NOT ENOUGH FUNDS'
                    self.color = 'red'
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.exit_text_rect.collidepoint(event.pos):
                    self.state = 'START'
        elif self.state == 'START':
            self.model.winnings = 0
            self.input_locked = False
            self.model.user_text = ''
            self.last_message = ''
            self.view.draw_start_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.buttons['play'].collidepoint(event.pos):
                    self.state = 'PLAY_GAME'  # Proceed to game
                elif self.view.buttons['exit'].collidepoint(event.pos):
                    self.state = 'CONFIRM_EXIT'
        elif self.state == 'CONFIRM_EXIT':
            self.view.draw_confirm_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.confirmbuttons['yes'].collidepoint(event.pos):
                    self.state = 'Secret'
                elif self.view.confirmbuttons['no'].collidepoint(event.pos):
                    self.state = 'START'
        elif self.state == 'Secret':
            self.view.draw_secret_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.secret_box.collidepoint(event.pos):
                    self.running = False
        elif self.state == 'POT':  
            self.view.draw_text()
            self.view.draw_fake_barcode(self.barcode_scratched)

            # Update the display continuously with the latest winnings calculated.

            if event.type == pygame.MOUSEMOTION:
                if self.view.barcode_rect.collidepoint(event.pos):
                    self.barcode_scratched = True
                    # Allow scratching only when the mouse is over the barcode area.
                self.view.scratching(event, scratching=True)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.exit_rect.collidepoint(event.pos) and self.barcode_scratched:
                    # Confirm and add the last calculated winnings only once when the user clicks the exit area.
                    if not self.winnings_displayed:
                        self.model.winnings += self.last_winnings
                        self.view.display_winnings(self.last_winnings)  # Ensure display matches the final winnings
                    # Reset the game state and prepare for a new game or exit
                    self.model.reset_pot_ticket()
                    self.view.reset_surfaces()
                    self.barcode_scratched = False
                    self.state = 'PLAY_GAME'
            self.last_winnings = self.view.update_scratching_surface(self.model.winning_numbers, self.model.your_numbers_with_values)
            
        elif self.state == 'WOLVES':
            if not self.winnings_displayed:
                self.view.draw_brook_surface(self.model.jackpot_numbers, self.model.jackpot_ball_number, self.model.your_jackpot_numbers, self.model.your_jackpot_ball_number)
                self.view.display_winnings(self.model.calculate_winnings())
                self.winnings_displayed = True
            elif event.type == pygame.MOUSEMOTION and self.view.barcode_rect.collidepoint(event.pos):
                self.barcode_scratched = True
            self.view.draw_fake_barcode(self.barcode_scratched)
            if self.barcode_scratched == True and event.type == pygame.MOUSEBUTTONDOWN:
                if self.view.exit_rect.collidepoint(event.pos):
                    self.model.reset_wolves_ticket()
                    self.barcode_scratched = False
                    self.winnings_displayed = False
                    self.state = 'PLAY_GAME'
                    return False
        elif self.state == 'END_GAME':
            self.view.draw_end_screen(self.model.winnings)
            if event.type == pygame.MOUSEBUTTONDOWN and self.view.end_buttons['PLAY AGAIN'].collidepoint(event.pos):
                self.state = 'START'
            elif event.type == pygame.MOUSEBUTTONDOWN and self.view.end_buttons['EXIT'].collidepoint(event.pos):
                self.running = False



    def main_loop(self):
        screen = pygame.display.set_mode((800, 800))
        self.view = LotteryGameScreens(screen)
        while self.running:
            for event in pygame.event.get():
                self.handle_events(event)
                pygame.display.flip()  # Update the display after each event
        pygame.quit()