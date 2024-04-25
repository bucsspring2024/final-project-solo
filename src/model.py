import random
import pygame
class LotteryModel:
    def __init__(self):
        self.winning_numbers = random.sample(range(1, 51), 5)
        self.your_numbers = random.sample(range(1, 51), 25)
        self.cash_values_distribution = [1.00] * 450 + [5.00] * 250 + [15.00] * 50 + [100] * 8 + [250] * 3 + [5000] * 2
        self.your_numbers_with_values = [(num, random.choice(self.cash_values_distribution)) for num in self.your_numbers]
        self.user_text = ''
        self.winnings = ''
        self.jackpot_numbers = random.sample(range(1, 11), 5)
        self.jackpot_ball_number = random.randint(1, 12)
        self.your_jackpot_numbers = random.sample(range(1,11), 5)
        self.your_jackpot_ball_number = random.randint(1,12)
        self.winnings = 0
    
    def update_winnings(self, winnings_info):
        # Check each winning number
        self.winnings += int(winnings_info)

    def reset_pot_ticket(self):
        self.winning_numbers = random.sample(range(1, 51), 5)
        self.your_numbers = random.sample(range(1, 51), 25)
        self.your_numbers_with_values = [(num, random.choice(self.cash_values_distribution)) for num in self.your_numbers]  

    def reset_wolves_ticket(self):
        self.jackpot_numbers = random.sample(range(1, 11), 5)
        self.jackpot_ball_number = random.randint(1, 12)
        self.your_jackpot_numbers = random.sample(range(1,11), 5)
        self.your_jackpot_ball_number = random.randint(1,12)

    def add_char(self, char):
        if char.isdigit():
            self.user_text += char

    def remove_char(self):
        self.user_text = self.user_text[:-1]
        

    def get_number(self):
        if self.user_text.isdigit():
            return int(self.user_text)
        return None

    def set_text(self, text):
        self.user_text = text
    
    def purchase_big_pot_ticket(self):
        number = int(self.user_text)
        self.user_text = str(number - 10)
        return None
        

    def purchase_seawolves_jackpot(self):
        number = int(self.user_text)
        self.user_text = str(number - 5)
        return None
    
    def calculate_winnings(self):
        # Check for matches and update winnings accordingly
        self.ticket_winnings = 0
        match_count = len(set(self.your_jackpot_numbers) & set(self.jackpot_numbers))
        if match_count == 0 and self.your_jackpot_ball_number == self.jackpot_ball_number:
            self.ticket_winnings = 3
            self.winnings += 3
        elif match_count == 1 and self.your_jackpot_ball_number == self.jackpot_ball_number:
            self.ticket_winnings = 3
            self.winnings += 3
        elif match_count == 2 and self.your_jackpot_ball_number == self.jackpot_ball_number:
            self.ticket_winnings = 7
            self.winnings += 7
        elif match_count == 3 and self.your_jackpot_ball_number != self.jackpot_ball_number:
            self.ticket_winnings = 7
            self.winnings += 7
        elif match_count == 3 and self.your_jackpot_ball_number == self.jackpot_ball_number:
            self.ticket_winnings = 100
            self.winnings += 100
        elif match_count == 4 and self.your_jackpot_ball_number != self.jackpot_ball_number:
            self.ticket_winnings = 100
            self.winnings += 100
        elif match_count == 4 and self.your_jackpot_ball_number == self.jackpot_ball_number:
            self.ticket_winnings = 1000
            self.winnings += 1000
        elif match_count == 5 and self.your_jackpot_ball_number != self.jackpot_ball_number:
            self.ticket_winnings = 5000
            self.winnings += 5000
        elif match_count == 5 and self.your_jackpot_ball_number == self.jackpot_ball_number:
            self.ticket_winnings = 10000
            self.winnings += 10000
        return self.ticket_winnings
        
        
    

   
