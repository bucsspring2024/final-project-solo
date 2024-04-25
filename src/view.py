import os
import pygame

class LotteryGameScreens:
    def __init__(self, screen):
        self.screen_width, self.screen_height = (800, 800)
        self.title_font = pygame.font.SysFont('Impact', 30, bold=False)
        self.button_font = pygame.font.SysFont('Calibri', 32, bold=True)
        self.text_font = pygame.font.SysFont('Calibiri', 30, bold=False)
        self.confirm_font = pygame.font.SysFont('Impact', 32, bold=False)
        self.number_font = pygame.font.SysFont('Arial', 26, bold=True)
        self.val_font = pygame.font.SysFont('Arial', 20, bold=True)
        self.user_input = ''
        self.screen = screen
        self.scratch_surfaces = [pygame.Surface((120, 60), pygame.SRCALPHA) for _ in range(30)]
        self.display_box = pygame.Rect(self.screen_width // 2 + 60, self.screen_height // 4, 250, 70)
        self.barcode_surface = pygame.Surface((180, 40))
        self.winning_label_y = 100
        self.your_label_y = 240
        self.winning_num_y = self.winning_label_y + (self.your_label_y - self.winning_label_y) // 2 - 30  # Centered between labels
        self.barcode_rect = pygame.Rect(self.screen_width - 200, self.screen_height - 50, 180, 40)
        self.exit_rect = pygame.Rect(self.screen_width // 2 + 150, 20, 235, 100)
        self.exit_text_rect = pygame.Rect(self.screen_width // 2 + 165, 700, 235, 100)
        self.text_rect = pygame.Rect(10, self.screen_height - 40, 200, 40)
        # Colors
        self.fonts = {
            'font': pygame.font.SysFont('Calibri', 20, bold=True),
            'large_font': pygame.font.SysFont('Impact', 36, bold=False),
            'number_font': pygame.font.SysFont('Arial', 26, bold=True),
            'val_font': pygame.font.SysFont('Arial', 20, bold=True),
            'bigger_font': pygame.font.SysFont('Calibri', 40, bold=True),
            'smaller_font': pygame.font.SysFont('Calibri', 12, bold=True)
        }
        self.colors = {
            'green': (34, 139, 34),
            'white': (255, 255, 255),
            'light_grey': (200, 200, 200),
            'black': (0, 0, 0),
            'red': (255, 0, 0),
            'button_green': (0, 200, 0),
            'stony_red': (153, 0, 0)
        }
        
        # Buttons positioned in a column
        self.end_buttons = {
            'PLAY AGAIN': pygame.Rect(self.screen_width // 2 - 100, 370, 220, 100),
            'EXIT': pygame.Rect(self.screen_width // 2 - 100, 520, 220 , 100)
        }
        self.buttons = {
            'play': pygame.Rect(self.screen_width // 2 - 100, 370, 220, 100),
            'exit': pygame.Rect(self.screen_width // 2 - 100, 520, 220, 100),
        }
        self.confirmbuttons = {
            'yes': pygame.Rect(self.screen_width // 2 - 100, 370, 220, 100),
            'no': pygame.Rect(self.screen_width // 2 - 100, 520, 220, 100)
        }
        self.gamebuttons = { 
            'seawolves_jackpot': pygame.Rect(70, 100, 300, 300),
            'binghamton_pot': pygame.Rect(70, 450, 300, 300),
        }
        image_dir = os.path.dirname(os.path.abspath(__file__))
        sourceFileDir = os.path.join(image_dir, '..', 'assets')
        filePath = os.path.join(sourceFileDir, 'big_pot_ticket.png')
        self.big_pot_image = pygame.image.load(filePath).convert_alpha()
        self.big_pot_image_rect = self.big_pot_image.get_rect(midbottom = (400,800))
        filePath2 = os.path.join(sourceFileDir, 'machine.png')
        self.starting_screen_image = pygame.image.load(filePath2)
        self.starting_screen_image_surf = self.starting_screen_image.get_rect(midbottom = (self.screen_width // 2, self.screen_height + 60))
        filePath3 = os.path.join(sourceFileDir, 'secret_screen.png')
        self.secret_screen_image = pygame.image.load(filePath3)
        filePath4 = os.path.join(sourceFileDir, 'screen.png')
        self.play_screen_image = pygame.image.load(filePath4).convert_alpha()
        self.play_screen_image_surf = self.play_screen_image.get_rect(midbottom= (self.screen_width // 2, self.screen_height))
        self.secret_screen_image_surf = self.secret_screen_image.get_rect(midbottom = (self.screen_width//2, self.screen_height + 60))  
        filePath5 = os.path.join(sourceFileDir, 'seawolves_jackpot.png')
        self.seawolves_image = pygame.image.load(filePath5).convert_alpha() 
        self.seawolves_image_surf = self.seawolves_image.get_rect(midbottom = (400, 800))
        filePath6 = os.path.join(sourceFileDir, 'info.png')
        self.info_image = pygame.image.load(filePath6).convert_alpha()
        self.info_image_suf = self.info_image.get_rect(midbottom =(400,800))
    def draw_start_screen(self):
        self.screen.fill(self.colors['black'])
    # Draw the title
        self.screen.blit(self.starting_screen_image, self.starting_screen_image_surf)
        title_text = self.title_font.render('WIN IT BIG: BINGHAMTON LOTTERY', True, self.colors['black'])
        self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, self.screen_height//2 - 2.5 * title_text.get_height()))
        
        # Draw the buttons with text centered within each button
        for key, rect in self.buttons.items():
            pygame.draw.rect(self.screen, self.colors['button_green'], rect, border_radius=20)
            button_text = self.button_font.render(key.capitalize(), True, self.colors['white'])
            self.screen.blit(button_text, (rect.x + (rect.width - button_text.get_width()) // 2,
                                    rect.y + (rect.height - button_text.get_height()) // 2))

    def draw_confirm_screen(self):
        self.screen.blit(self.starting_screen_image, self.starting_screen_image_surf)
        confirm_text = self.title_font.render('ARE YOU SURE?', True, self.colors['black'])
        confirm_rect = confirm_text.get_rect(topleft=(self.screen_width // 2 - confirm_text.get_width()//2 + 10, self.screen_height//2 - 2.5 * confirm_text.get_height()))
        self.screen.blit(confirm_text, confirm_rect)

        for key, rect in self.confirmbuttons.items():
            button_color = self.colors['button_green'] 
            pygame.draw.rect(self.screen, button_color, rect, border_radius=20)
            text = self.button_font.render(key.title(), True, self.colors['white'])
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    def draw_secret_screen(self):
        self.screen.blit(self.secret_screen_image, self.secret_screen_image_surf)
        texts = ["CONGRATULATIONS!", "YOU'RE SMARTER THAN MOST"]
        positions = [(self.screen_width // 2, 175), (self.screen_width // 2, 300)]  # Y positions adjusted for visual appeal

        for i, text in enumerate(texts):
            title_text = self.confirm_font.render(text, True, self.colors['black'])
            pos = (positions[i][0] - title_text.get_width() // 2, positions[i][1])
            self.screen.blit(title_text, pos)

        self.secret_box = pygame.Rect((self.screen_width // 2 - 150), (self.screen_height // 2), 300, 150)
        pygame.draw.rect(self.screen, self.colors['white'], self.secret_box, border_radius=20)
        text = self.button_font.render('CLICK TO EXIT', True, self.colors['black'])
        text_rect = text.get_rect(center=self.secret_box.center)
        self.screen.blit(text, text_rect)
    def draw_play_screen(self):
        self.screen.blit(self.play_screen_image, self.play_screen_image_surf)
        pygame.draw.rect(self.screen, self.colors['white'], self.exit_text_rect, border_radius=20)
        exit_text = self.fonts['font'].render('CLICK HERE TO END GAME', True, self.colors['black'])
        exit_text_rect = exit_text.get_rect(center=self.exit_text_rect.center)
        self.screen.blit(exit_text, exit_text_rect)
        title_text = self.fonts['large_font'].render("PLEASE TYPE A NUMBER", True, self.colors['black'])
        self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 30))
    # Draw the game buttons
        for key, rect in self.gamebuttons.items():
            if key == 'binghamton_pot':
                self.screen.blit(self.big_pot_image, rect.topleft)
            elif key == 'seawolves_jackpot':
                self.screen.blit(self.seawolves_image, rect.topleft)
      
        
    # Method within LotteryGameScreens
    def updated_display(self, user_text, message="", color="", message2=""):
        # Create a surface for the display area
        surface = pygame.Surface((self.display_box.width, self.display_box.height))
        surface.fill(self.colors['white'])  # Fill the surface with green

        # Draw a rectangular outline on the created surface with light grey color
        pygame.draw.rect(surface, self.colors['light_grey'], surface.get_rect(), 2)

        # Render the user text on another surface
        input_surface = self.button_font.render(user_text, True, self.colors['black'])
        money_symbol = self.button_font.render("$", True, self.colors['black'])
        symbol_x = 10 
        symbol_y = (self.display_box.height - money_symbol.get_height()) // 2
        
        # Blit the user text surface onto the green surface, adjusting so it's inside the rectangle
        text_x = (self.display_box.width - input_surface.get_width()) // 2
        text_y = (self.display_box.height - input_surface.get_height()) // 2
        surface.blit(input_surface, (text_x, text_y))
        surface.blit(money_symbol, (symbol_x, symbol_y))

        # Blit the whole green surface onto the main screen at the position of display_box
        self.screen.blit(surface, self.display_box.topleft)

        # If there is a message, display it above the display_box
        if message:
            message_surface = self.text_font.render(message, True, self.colors[color])
            message_x = self.display_box.x + (self.display_box.width - message_surface.get_width()) // 2
            message_y = self.display_box.y - message_surface.get_height() - 5  # 10 pixels above the box
            self.screen.blit(message_surface, (message_x, message_y))
        if message2:
            message_surface = self.text_font.render(message2, True, self.colors[color])
            message_x = self.display_box.x + (self.display_box.width - message_surface.get_width()) // 2
            message_y = self.display_box.y - message_surface.get_height() - 30
            self.screen.blit(message_surface, (message_x, message_y))
    
    def draw_text(self):
        self.screen.fill(self.colors['green'])
        title_text = self.fonts['large_font'].render('Binghamton Pot!', True, self.colors['black'])
        cost_text = self.fonts['bigger_font'].render('$10', True, self.colors['black'])
        winning_label_text = self.fonts['font'].render('WINNING NUMBERS', True, self.colors['black'])
        your_label_text = self.fonts['font'].render('YOUR NUMBERS', True, self.colors['black'])
        self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 20))
        self.screen.blit(cost_text, (10, 10))
        self.screen.blit(winning_label_text, (self.screen_width // 2 - winning_label_text.get_width() // 2, self.winning_label_y))
        self.screen.blit(your_label_text, (self.screen_width // 2 - your_label_text.get_width() // 2, self.your_label_y))

   
    def draw_fake_barcode(self, scratched=False):
        if not scratched:
            self.barcode_surface.fill(self.colors['light_grey'])
            barcode_text = self.fonts['smaller_font'].render('TOUCH HERE WHEN FINISHED', True, self.colors['black'])
            barcode_text_rect = barcode_text.get_rect(center=self.barcode_surface.get_rect().center)
            self.barcode_surface.blit(barcode_text, barcode_text_rect)  # Draw text on the barcode surface
        else:
            self.barcode_surface.fill(self.colors['white'])
            num_lines = 20
            line_spacing = 10
            for i in range(num_lines + 1):
                line_width = 2 if i % 2 == 0 else 3
                pygame.draw.line(self.barcode_surface, self.colors['black'], (i * line_spacing, 0), (i * line_spacing, self.barcode_surface.get_height()), line_width)
                pygame.draw.rect(self.screen, self.colors['white'], self.exit_rect, border_radius=20)
                text = self.fonts['font'].render('CLICK HERE FOR NEXT PAGE', True, self.colors['black'])
                text_rect = text.get_rect(center=self.exit_rect.center)
                self.screen.blit(text, text_rect)
        barcode_x, barcode_y = self.screen_width - 200, self.screen_height - 50
        pygame.draw.rect(self.screen, self.colors['light_grey'], (barcode_x, barcode_y, 180, 40))  # Visible box
        self.screen.blit(self.barcode_surface, (barcode_x, barcode_y))

    def update_scratching_surface(self, winning_numbers, your_numbers_with_values):
        winnings_info = 0
        for i, surface in enumerate(self.scratch_surfaces):
            x = (i % 5) * 140 + (self.screen_width - 700) // 2
            y = self.winning_num_y if i < 5 else 320 + ((i - 5) // 5) * 80
            pygame.draw.rect(self.screen, self.colors['light_grey'], (x, y, 120, 60))
            self.screen.blit(surface, (x, y))
            if i < 5:  # For winning numbers
                if pygame.Surface.get_at(surface, (60, 30)) == self.colors['green']:
                    num_text = self.fonts['number_font'].render(str(winning_numbers[i]), True, self.colors['black'])
                    self.screen.blit(num_text, (x + (120 - num_text.get_width()) // 2, y + (60 - num_text.get_height()) // 2))
            else:  # For your numbers with values
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
        for i, surface in enumerate(self.scratch_surfaces):  # Excluding the barcode for now
                x = (i % 5) * 140 + (self.screen_width - 700) // 2
                y = self.winning_num_y if i < 5 else 320 + ((i - 5) // 5) * 80
                self.rect = pygame.Rect(x, y, 120, 60)
                if scratching == True:
                    pygame.draw.circle(surface, self.colors['green'], (event.pos[0] - x, event.pos[1] - y), 20)
    def reset_surfaces(self):
        self.scratch_surfaces = [pygame.Surface((120, 60), pygame.SRCALPHA) for _ in range(30)]
    
    def display_winnings(self, winnings):
        text = self.fonts['font'].render(f'Your Winnings: ${winnings}', True, self.colors['black'])
        pygame.draw.rect(self.screen, self.colors['green'], self.text_rect, border_radius=20)
        text_rect = text.get_rect(center=self.text_rect.center)
        self.screen.blit(text, text_rect)
    def draw_brook_surface(self, jackpot_numbers, jackpot_ball_number, your_jackpot_numbers, your_jackpot_ball_number):
        self.screen.fill(self.colors['stony_red'])
        title_text = self.fonts['large_font'].render('SEAWOLVES JACKPOT!', True, self.colors['black'])
        cost_text = self.fonts['bigger_font'].render('$5', True, self.colors['black'])
        winning_label_text = self.fonts['font'].render('WINNING NUMBERS', True, self.colors['black'])
        your_label_text = self.fonts['font'].render('YOUR NUMBERS', True, self.colors['black'])
        self.screen.blit(title_text, (self.screen_width // 2 - title_text.get_width() // 2, 20))
        self.screen.blit(cost_text, (10, 10))
        self.screen.blit(winning_label_text, (self.screen_width // 2 - winning_label_text.get_width() // 2, self.winning_label_y))
        self.screen.blit(your_label_text, (self.screen_width // 2 - your_label_text.get_width() // 2, self.your_label_y + 20))
        # Define the positions and dimensions of the circles
        circle_radius = 40
        circle_padding = 20
        circle_spacing = circle_radius * 2 + circle_padding
        start_x = 150
        start_y = 185
        num_circles = 6
        
        # Draw the circles with numbers (except the last red ball)
        for i in range(num_circles - 1):
            circle_x = start_x + i * circle_spacing
            circle_y = start_y
            circle_color = (200, 200, 200)  # Light grey for other circles
            text_color = (0, 0, 0)  # Black text for other circles
            number_text = self.fonts['number_font'].render(str(jackpot_numbers[i]), True, text_color)
                
            pygame.draw.circle(self.screen, circle_color, (circle_x, circle_y), circle_radius)
            
            # Render and blit the text for each circle
            text_rect = number_text.get_rect(center=(circle_x, circle_y))
            self.screen.blit(number_text, text_rect)
            
        
        # Draw the red ball (Powerball) with the jackpot_ball_number
        circle_x = start_x + (num_circles - 1) * circle_spacing
        circle_y = start_y
        circle_color = (255, 0, 0)  # Red color for the last ball (Powerball)
        text_color = (255, 255, 255)  # White text for Powerball
        number_text = self.fonts['number_font'].render(str(jackpot_ball_number), True, text_color)
        
        
                
        pygame.draw.circle(self.screen, circle_color, (circle_x, circle_y), circle_radius)
        
        # Render and blit the text for the Powerball circle
        text_rect = number_text.get_rect(center=(circle_x, circle_y))
        self.screen.blit(number_text, text_rect)
        self.barcode_surface.fill(self.colors['light_grey'])
        barcode_x, barcode_y = self.screen_width - 200, self.screen_height - 50
        pygame.draw.rect(self.screen, self.colors['light_grey'], (barcode_x, barcode_y, 180, 40))  # Visible box
        self.screen.blit(self.barcode_surface, (barcode_x, barcode_y))
        
        
        # Draw the circles without numbers (for Powerball)
        for i in range(num_circles - 1):
            circle_x = start_x + i * circle_spacing
            circle_y = start_y + circle_radius * 2 + 110
            text_color = (0, 0, 0)
            number_text = self.fonts['number_font'].render(str(your_jackpot_numbers[i]), True, text_color)
            pygame.draw.circle(self.screen, (200, 200, 200), (circle_x, circle_y), circle_radius)
            text_rect = number_text.get_rect(center=(circle_x, circle_y))
            self.screen.blit(number_text, text_rect)
            

        # Draw the last circle (far-right) with the same red color
        circle_x = start_x + (num_circles - 1) * circle_spacing
        circle_y = start_y + circle_radius * 2 + 110
        circle_color = (255, 0, 0)  # Red color
        text_color = (255, 255, 255)
        number_text = self.fonts['number_font'].render(str(your_jackpot_ball_number), True, text_color)
        pygame.draw.circle(self.screen, circle_color, (circle_x, circle_y), circle_radius)
        text_rect = number_text.get_rect(center=(circle_x, circle_y))
        self.screen.blit(number_text, text_rect)
    
    def draw_end_screen(self, winnings):
        self.screen.fill(self.colors['black'])
        self.screen.blit(self.starting_screen_image, self.starting_screen_image_surf)
        total = self.title_font.render(f'Your Winnings: ${winnings}', True, self.colors['black'])
        total_rect = total.get_rect(topleft=(self.screen_width // 2 - total.get_width()//2 + 10, self.screen_height // 2 - 2.5 * total.get_height()))
        self.screen.blit(total, total_rect)
        for key, rect in self.end_buttons.items():
            pygame.draw.rect(self.screen, self.colors['button_green'], rect, border_radius=20)
            button_text = self.button_font.render(key.capitalize(), True, self.colors['white'])
            self.screen.blit(button_text, (rect.x + (rect.width - button_text.get_width()) // 2,
                                    rect.y + (rect.height - button_text.get_height()) // 2))
    