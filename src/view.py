import os
import pygame

class LotteryView:
    def __init__(self, screen):
        self.screen_width, self.screen_height = (800, 800) # A reference for the screen-related displays
        self.screen = screen
        # Stores some constants, some constants in my code are, parameter or loop-based
        self.constants = {
            'winning_label_y': 100,
            'your_label_y': 240,
            'winning_num_y': 140,
            'barcode_x': 600,
            'barcode_y': 750,
            'circle_radius': 40,
            'circle_padding': 20,
            'circle_spacing': 100,
            'start_x': 150,
            'start_y': 185,
            'num_circles': 6,
            'red_circle_x': 650,
            'red_circle_2_y': 375

        }
        # Fonts
        self.fonts = {
            'title_font': pygame.font.SysFont('Impact', 30, bold=False),
            'button_font': pygame.font.SysFont('Calibri', 32, bold=True),
            'message_font': pygame.font.SysFont('Calibri', 30, bold=True),
            'secret_font': pygame.font.SysFont('Impact', 32, bold=False),
            'font': pygame.font.SysFont('Calibri', 20, bold=True),
            'large_font': pygame.font.SysFont('Impact', 36, bold=False),
            'number_font': pygame.font.SysFont('Arial', 26, bold=True),
            'val_font': pygame.font.SysFont('Arial', 20, bold=True),
            'bigger_font': pygame.font.SysFont('Calibri', 40, bold=True),
            'smaller_font': pygame.font.SysFont('Calibri', 12, bold=True)
        }

        # Colors
        self.colors = {
            'green': (34, 139, 34),
            'white': (255, 255, 255),
            'light_grey': (200, 200, 200),
            'black': (0, 0, 0),
            'red': (255, 0, 0),
            'button_green': (0, 200, 0),
            'stony_red': (153, 0, 0),
            'gold': (255, 215, 0)
        }
        
        # Rect: Buttons for End Game Screen
        self.end_buttons = {
            'PLAY AGAIN': pygame.Rect(self.screen_width // 2 - 100, 370, 220, 100),
            'EXIT': pygame.Rect(self.screen_width // 2 - 100, 520, 220 , 100)
        }
        # Rect: Buttons for Start Screen
        self.buttons = {
            'play': pygame.Rect(self.screen_width // 2 - 100, 370, 220, 100),
            'exit': pygame.Rect(self.screen_width // 2 - 100, 520, 220, 100),
        }
        # Rect: Buttons for Confirm Screen
        self.confirmbuttons = {
            'yes': pygame.Rect(self.screen_width // 2 - 100, 370, 220, 100),
            'no': pygame.Rect(self.screen_width // 2 - 100, 520, 220, 100)
        }
        # Rect: Buttons for Play Game Screen
        self.gamebuttons = { 
            'seawolves_jackpot': pygame.Rect(70, 100, 300, 300),
            'binghamton_pot': pygame.Rect(70, 450, 300, 300),
        }
        # Stores certain texts, some texts may not be stored here because of certain loops or messages are parameter-based 
        self.texts = {
            'start_title_text': self.fonts['title_font'].render('WIN IT BIG: BINGHAMTON LOTTERY', True, self.colors['black']),
            'confirm_text': self.fonts['title_font'].render('ARE YOU SURE?', True, self.colors['black']),
            'secret_exit_text': self.fonts['button_font'].render('CLICK TO EXIT', True, self.colors['black']),
            'end_game_text': self.fonts['font'].render('CLICK HERE TO END GAME', True, self.colors['black']),
            'play_title_text': self.fonts['large_font'].render("PLEASE TYPE A NUMBER", True, self.colors['black']),
            'money_symbol_text': self.fonts['button_font'].render("$", True, self.colors['black']),
            'binghamton_pot_title': self.fonts['large_font'].render('Binghamton Pot!', True, self.colors['black']),
            'binghamton_pot_cost_text': self.fonts['bigger_font'].render('$10', True, self.colors['black']),
            'seawolves_title_text': self.fonts['large_font'].render('SEAWOLVES JACKPOT!', True, self.colors['black']),
            'seawolves_cost_text': self.fonts['bigger_font'].render('$5', True, self.colors['black']),
            'winning_label_text': self.fonts['font'].render('WINNING NUMBERS', True, self.colors['black']),
            'your_label_text': self.fonts['font'].render('YOUR NUMBERS', True, self.colors['black'])
        }

        # Stores certain rects, some rects may not be stored here because of looping or conditional statements
        self.rects = {
            'barcode': pygame.Rect(self.constants['barcode_x'], self.constants['barcode_y'], 180, 40),
            'exit': pygame.Rect(self.screen_width // 2 + 150, 20, 235, 100),
            'exit_text': pygame.Rect(self.screen_width // 2 + 165, 700, 235, 100),
            'text': pygame.Rect(10, self.screen_height - 40, 200, 40),
            'high_score': pygame.Rect(self.screen_width // 2 - 135, self.screen_height // 2 - 140, 310, 65),
            'display_box': pygame.Rect(self.screen_width // 2 + 60, self.screen_height // 4, 250, 70),
            'secret_box': pygame.Rect((self.screen_width // 2 - 150), (self.screen_height // 2), 300, 150),

        }
        # Calling the pngs in Assets folder
        image_dir = os.path.dirname(os.path.abspath(__file__))
        sourceFileDir = os.path.join(image_dir, '..', 'assets')

        self.filePaths = {
            '1': os.path.join(sourceFileDir, 'binghamton_pot.png'),
            '2': os.path.join(sourceFileDir, 'machine.png'),
            '3': os.path.join(sourceFileDir, 'secret_screen.png'),
            '4': os.path.join(sourceFileDir, 'screen.png'),
            '5': os.path.join(sourceFileDir, 'seawolves_jackpot.png'),
            '6': os.path.join(sourceFileDir, 'info.png')
        }

        self.images = {
            'binghamton_pot': pygame.image.load(self.filePaths['1']),
            'machine_screen': pygame.image.load(self.filePaths['2']),
            'secret_screen': pygame.image.load(self.filePaths['3']),
            'play_screen': pygame.image.load(self.filePaths['4']),
            'seawolves': pygame.image.load(self.filePaths['5']), 
            'info': pygame.image.load(self.filePaths['6'])
        }
        # Certain surfaces contained within 
        self.surfs = {
            'binghamton_pot': self.images['binghamton_pot'].get_rect(midbottom = (400,800)),
            'machine_screen': self.images['machine_screen'].get_rect(midbottom=(self.screen_width // 2, self.screen_height + 60)),
            'secret_screen': self.images['secret_screen'].get_rect(midbottom=(self.screen_width//2, self.screen_height + 60)),
            'play_screen': self.images['play_screen'].get_rect(midbottom=(self.screen_width // 2, self.screen_height)),
            'secret_screen_2': self.texts['secret_exit_text'].get_rect(center=self.rects['secret_box'].center),
            'exit_text': self.texts['end_game_text'].get_rect(center=self.rects['exit_text'].center),
            'seawolves': self.images['seawolves'].get_rect(midbottom=(self.screen_width // 2, self.screen_height)),
            'info': self.images['info'].get_rect(bottomleft=(10, 750)), 
            'title_text': (self.screen_width // 2 - self.texts['start_title_text'].get_width() // 2, self.screen_height//2 - 2.5 * self.texts['start_title_text'].get_height()),
            'user_friendly_text': pygame.Surface((self.rects['display_box'].width, self.rects['display_box'].height)),
            'scratch': [pygame.Surface((120, 60), pygame.SRCALPHA) for _ in range(30)],
            'barcode': pygame.Surface((180, 40))
        }

        
    def draw_start_screen(self, high_score):
    # Make background black
        self.screen.fill(self.colors['black'])
    # Set up screen and title text
        self.screen.blit(self.images['machine_screen'], self.surfs['machine_screen'])
        self.screen.blit(self.texts['start_title_text'], self.surfs['title_text'])
        self.display_high_score(high_score)
        # Draw the buttons with text centered within each button
        for key, rect in self.buttons.items():
            pygame.draw.rect(self.screen, self.colors['button_green'], rect, border_radius=20)
            button_text = self.fonts['button_font'].render(key.capitalize(), True, self.colors['white'])
            self.screen.blit(button_text, (rect.x + (rect.width - button_text.get_width()) // 2,
                                    rect.y + (rect.height - button_text.get_height()) // 2))
            
    def display_high_score(self, high_score):
        # Displays the High Score: creates text, draws rect for text, and displays text & rect 
        text = self.fonts['font'].render(f'Highest Return: ${high_score}', True, self.colors['green'])
        self.screen.blit(text, text.get_rect(center=self.rects['high_score'].center))

    def draw_confirm_screen(self):
        # For self.state == 'CONFIRM': creates cofirm text, draws rects for text, and displays the text & rects
        self.screen.blit(self.images['machine_screen'], self.surfs['machine_screen'])
        confirm_rect = self.texts['confirm_text'].get_rect(topleft=(self.screen_width // 2 - self.texts['confirm_text'].get_width()//2 + 10, self.screen_height//2 - 2.5 * self.texts['confirm_text'].get_height()))
        self.screen.blit(self.texts['confirm_text'], confirm_rect)
        # Draw Rect buttons
        for key, rect in self.confirmbuttons.items():
            pygame.draw.rect(self.screen, self.colors['button_green'], rect, border_radius=20)
            text = self.fonts['button_font'].render(key.capitalize(), True, self.colors['white'])
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    def draw_secret_screen(self):
        # Displays secret screen, allowing the user to quit
        self.screen.blit(self.images['secret_screen'], self.surfs['secret_screen'])
        texts = ["CONGRATULATIONS!", "YOU'RE SMARTER THAN MOST"]
        positions = [(self.screen_width // 2, 175), (self.screen_width // 2, 300)]  # Y positions adjusted for visual appeal
        
        for i, text in enumerate(texts):
            title_text = self.fonts['secret_font'].render(text, True, self.colors['black'])
            pos = (positions[i][0] - title_text.get_width() // 2, positions[i][1])
            self.screen.blit(title_text, pos)

        pygame.draw.rect(self.screen, self.colors['white'], self.rects['secret_box'], border_radius=20)
        self.screen.blit(self.texts['secret_exit_text'], self.surfs['secret_screen_2'])

    def draw_play_screen(self):
        # After user clicks 'PLAY', play screen with rects and images are displayed
        self.screen.blit(self.images['play_screen'], self.surfs['play_screen'])
        pygame.draw.rect(self.screen, self.colors['white'], self.rects['exit_text'], border_radius=20)
        self.screen.blit(self.texts['end_game_text'], self.surfs['exit_text'])
        self.screen.blit(self.texts['play_title_text'], (self.screen_width // 2 - self.texts['play_title_text'].get_width() // 2, 30))
    # Draw the game buttons
        for key, rect in self.gamebuttons.items():
            if key == 'binghamton_pot':
                self.screen.blit(self.images['binghamton_pot'], rect.topleft)
            elif key == 'seawolves_jackpot':
                self.screen.blit(self.images['seawolves'], rect.topleft)
      
        
    # Method within LotteryGameScreens
    def updated_display(self, user_text, message="", color="", message2=""):
        self.surfs['user_friendly_text'].fill(self.colors['white'])  # Fill the surface with white

        # Draw a rectangular outline on the created surface with light grey color
        pygame.draw.rect(self.surfs['user_friendly_text'], self.colors['light_grey'], self.surfs['user_friendly_text'].get_rect(), 2)

        # Render the user text on another surface
        input_surface = self.fonts['button_font'].render(user_text, True, self.colors['black'])
        
        # Blit the user text surface onto the green surface, adjusting so it's inside the rectangle
        text_x = (self.rects['display_box'].width - input_surface.get_width()) // 2
        text_y = (self.rects['display_box'].height - input_surface.get_height()) // 2
        symbol_x = 10 
        symbol_y = (self.rects['display_box'].height - self.texts['money_symbol_text'].get_height()) // 2
        self.surfs['user_friendly_text'].blit(input_surface, (text_x, text_y))
        self.surfs['user_friendly_text'].blit(self.texts['money_symbol_text'], (symbol_x, symbol_y))

        # Blit the whole green surface onto the main screen at the position of display_box
        self.screen.blit(self.surfs['user_friendly_text'], self.rects['display_box'].topleft)

        # If there is a message, display it above the display_box
        if message:
            message_surface = self.fonts['message_font'].render(message, True, self.colors[color])
            message_x = self.rects['display_box'].x + (self.rects['display_box'].width - message_surface.get_width()) // 2
            message_y = self.rects['display_box'].y - message_surface.get_height() - 5  # 10 pixels above the box
            self.screen.blit(message_surface, (message_x, message_y))
        # Message2 made for longer message, stacking messages in a row, rather than one long message, displays it above the display_box
        if message2:
            message2_surface = self.fonts['message_font'].render(message2, True, self.colors[color])
            message_x = self.rects['display_box'].x + (self.rects['display_box'].width - message2_surface.get_width()) // 2
            message_y = self.rects['display_box'].y - message2_surface.get_height() - 30
            self.screen.blit(message2_surface, (message_x, message_y))
    
    def draw_text(self):
        # Binghamton pot ticket screen background texts
        self.screen.fill(self.colors['green'])
        texts = [self.texts['binghamton_pot_title'], self.texts['binghamton_pot_cost_text'], self.texts['winning_label_text'], self.texts['your_label_text']]
        positions = [(self.screen_width // 2 - self.texts['binghamton_pot_title'].get_width() // 2, 20), (10, 10), (self.screen_width // 2 - self.texts['winning_label_text'].get_width() // 2, self.constants['winning_label_y']), (self.screen_width // 2 - self.texts['your_label_text'].get_width() // 2, self.constants['your_label_y'])]
        for text, pos in zip(texts, positions):
            self.screen.blit(text, pos)
   
    def draw_fake_barcode(self, scratched=False):
        # Draw's unscratched or when true, scratched barcode; also used to allow user to click next page text
        if not scratched:
            self.surfs['barcode'].fill(self.colors['light_grey'])
            barcode_text = self.fonts['smaller_font'].render('TOUCH HERE WHEN FINISHED', True, self.colors['black'])
            barcode_text_rect = barcode_text.get_rect(center=self.surfs['barcode'].get_rect().center)
            self.surfs['barcode'].blit(barcode_text, barcode_text_rect)  # Draw text on the barcode surface
        else:
            self.surfs['barcode'].fill(self.colors['white'])
            num_lines = 20
            line_spacing = 10
            for i in range(num_lines + 1):
                line_width = 2 if i % 2 == 0 else 3
                pygame.draw.line(self.surfs['barcode'], self.colors['black'], (i * line_spacing, 0), (i * line_spacing, self.surfs['barcode'].get_height()), line_width)
                pygame.draw.rect(self.screen, self.colors['white'], self.rects['exit'], border_radius=20)
                text = self.fonts['font'].render('CLICK HERE FOR NEXT PAGE', True, self.colors['black'])
                text_rect = text.get_rect(center=self.rects['exit'].center)
                self.screen.blit(text, text_rect)
        pygame.draw.rect(self.screen, self.colors['light_grey'], self.rects['barcode'])  # Visible box
        self.screen.blit(self.surfs['barcode'], (self.constants['barcode_x'], self.constants['barcode_y']))

    def display_winnings(self, winnings):
            # Displays the winnings for each ticket on the bottom left of the screen
            text = self.fonts['font'].render(f'Your Winnings: ${winnings}', True, self.colors['black'])
            pygame.draw.rect(self.screen, self.colors['white'], self.rects['text'], border_radius=20)
            text_rect = text.get_rect(center=self.rects['text'].center)
            self.screen.blit(text, text_rect)

    def update_scratching_surface(self, winning_numbers, your_numbers_with_values):
        # Winning_info allows the program to keep track of how much the winner won by "matching" numbers. This method updates the scratched surfaces
        winnings_info = 0
        for i, surface in enumerate(self.surfs['scratch']):
            x = (i % 5) * 140 + (self.screen_width - 700) // 2
            y = self.constants['winning_num_y'] if i < 5 else 320 + ((i - 5) // 5) * 80
            if i < 5:
                pygame.draw.rect(self.screen, self.colors['gold'], (x, y, 120, 60))
                num_text = self.fonts['number_font'].render(str(winning_numbers[i]), True, self.colors['black'])
                self.screen.blit(num_text, (x + (120 - num_text.get_width()) // 2, y + (60 - num_text.get_height()) // 2))
            else:
                pygame.draw.rect(self.screen, self.colors['light_grey'], (x, y, 120, 60))
                self.screen.blit(surface, (x, y))
                if pygame.Surface.get_at(surface, (60, 30)) == self.colors['green']:
                    number, value = your_numbers_with_values[i - 5]  # Adjust index for your_numbers_with_values
                    num_text = self.fonts['number_font'].render(str(number), True, self.colors['black'])
                    val_text = self.fonts['val_font'].render(f"${value}", True, self.colors['black'])
                    self.screen.blit(num_text, (x + (120 - num_text.get_width()) // 2, y + 5))
                    self.screen.blit(val_text, (x + (120 - val_text.get_width()) // 2, y + 30))
                    if number in winning_numbers:
                         winnings_info += value
            self.display_winnings(winnings_info)
        return winnings_info

    def scratching(self, event, scratching=False):
        # Allows user to "scratch" the scratching surfaces
        for i, surface in enumerate(self.surfs['scratch']):  
                x = (i % 5) * 140 + (self.screen_width - 700) // 2
                y = 320 + ((i - 5) // 5) * 80
                self.rect = pygame.Rect(x, y, 120, 60)
                if scratching == True:
                    pygame.draw.circle(surface, self.colors['green'], (event.pos[0] - x, event.pos[1] - y), 30)
    
    def reset_surfaces(self):
        # Called for resetting scratched surfaces, so that the previous scratches are not on the next
        self.surfs['scratch'] = [pygame.Surface((120, 60), pygame.SRCALPHA) for _ in range(30)]
    
    def draw_brook_surface(self, jackpot_numbers, jackpot_ball_number, your_jackpot_numbers, your_jackpot_ball_number):
        # Display stony brook ticket
        self.screen.fill(self.colors['stony_red'])
        self.screen.blit(self.images['info'], self.surfs['info'])
        texts = [self.texts['seawolves_title_text'], self.texts['seawolves_cost_text'], self.texts['winning_label_text'], self.texts['your_label_text']]
        positions = [(self.screen_width // 2 - self.texts['seawolves_title_text'].get_width() // 2, 20), (10, 10), (self.screen_width // 2 - self.texts['winning_label_text'].get_width() // 2, self.constants['winning_label_y']), (self.screen_width // 2 - self.texts['your_label_text'].get_width() // 2, self.constants['your_label_y'] + 20)]
        for text, pos in zip(texts, positions):
            self.screen.blit(text, pos)        
        
        # Draw the winning circles with numbers (except the last red ball)
        for i in range(self.constants['num_circles'] - 1):
            circle_x = self.constants['start_x'] + i * self.constants['circle_spacing']
            circle_y = self.constants['start_y']
            number_text = self.fonts['number_font'].render(str(jackpot_numbers[i]), True, self.colors['black'])    
            pygame.draw.circle(self.screen, self.colors['light_grey'], (circle_x, circle_y), self.constants['circle_radius'])
            text_rect = number_text.get_rect(center=(circle_x, circle_y))
            self.screen.blit(number_text, text_rect)
        # last red ball
        number_text = self.fonts['number_font'].render(str(jackpot_ball_number), True, self.colors['white'])
        pygame.draw.circle(self.screen, self.colors['red'], (self.constants['red_circle_x'], self.constants['start_y']), self.constants['circle_radius'])
        text_rect = number_text.get_rect(center=(self.constants['red_circle_x'], self.constants['start_y']))
        self.screen.blit(number_text, text_rect)
        self.surfs['barcode'].fill(self.colors['light_grey'])
        pygame.draw.rect(self.screen, self.colors['light_grey'], self.rects['barcode'])  
        self.screen.blit(self.surfs['barcode'], (self.constants['barcode_x'], self.constants['barcode_y']))
        
        # Draw the user's circles with numbers (except the last red ball)
        for i in range(self.constants['num_circles'] - 1):
            circle_x = self.constants['start_x'] + i * self.constants['circle_spacing']
            circle_y = self.constants['start_y'] + self.constants['circle_radius'] * 2 + 110
            number_text = self.fonts['number_font'].render(str(your_jackpot_numbers[i]), True, self.colors['black'])
            pygame.draw.circle(self.screen, (200, 200, 200), (circle_x, circle_y), self.constants['circle_radius'])
            text_rect = number_text.get_rect(center=(circle_x, circle_y))
            self.screen.blit(number_text, text_rect)
        # Last red ball
        number_text = self.fonts['number_font'].render(str(your_jackpot_ball_number), True, self.colors['white'])
        pygame.draw.circle(self.screen, self.colors['red'], (self.constants['red_circle_x'], self.constants['red_circle_2_y']), self.constants['circle_radius'])
        text_rect = number_text.get_rect(center=(self.constants['red_circle_x'], self.constants['red_circle_2_y']))
        self.screen.blit(number_text, text_rect)
    
    def draw_end_screen(self, winnings):
        # Display end screen; which allows user to see their total winnings and asks wheter to quit or play again
        self.screen.fill(self.colors['black'])
        self.screen.blit(self.images['machine_screen'], self.surfs['machine_screen'])
        total = self.fonts['title_font'].render(f'Your Winnings: ${winnings}', True, self.colors['black'])
        total_rect = total.get_rect(topleft=(self.screen_width // 2 - total.get_width()//2 + 10, self.screen_height // 2 - 2.5 * total.get_height()))
        self.screen.blit(total, total_rect)
        for key, rect in self.end_buttons.items():
            pygame.draw.rect(self.screen, self.colors['button_green'], rect, border_radius=20)
            button_text = self.fonts['button_font'].render(key.capitalize(), True, self.colors['white'])
            self.screen.blit(button_text, (rect.x + (rect.width - button_text.get_width()) // 2,
                                    rect.y + (rect.height - button_text.get_height()) // 2))
    