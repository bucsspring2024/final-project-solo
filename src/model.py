import random
import os
class LotteryModel:
    def __init__(self):
        #Give the inital numbers for each tickets
        self.winning_numbers = random.sample(range(1, 51), 5)
        self.your_numbers = random.sample(range(1, 51), 25)
        self.cash_values_distribution = [1.00] * 450 + [5.00] * 250 + [15.00] * 50 + [100] * 8 + [250] * 3 + [5000] * 2
        self.your_numbers_with_values = [(num, random.choice(self.cash_values_distribution)) for num in self.your_numbers]
        self.jackpot_numbers = random.sample(range(1, 11), 5)
        self.jackpot_ball_number = random.randint(1, 12)
        self.your_jackpot_numbers = random.sample(range(1,11), 5)
        self.your_jackpot_ball_number = random.randint(1,12)
        self.user_text = '' # Stores user's typed input
        self.winnings = '' # Stores total winnings
        self.winnings = 0 # Sets the inital winnings to 0
        self.file_path = 'gamedata.txt'
        self.current_winnings = 0

        
    def score_history(self):
        # Adjusts the high_score as needed (Data Permanence)
        if not os.path.exists(self.file_path):
            file = open(self.file_path, 'w')
            file.write('0')
            file.close()
            
        file = open(self.file_path, "r")
        contents = file.read()
        file.close()
        self.current_winnings = float(contents.strip())
        if self.winnings > self.current_winnings:
            file = open(self.file_path, 'w')
            file.write(str(self.winnings))
            file.close()
        elif self.current_winnings == '':
            file.open(self.file_path, 'w')
            file.write('0')
            file.close()
            pass
        return self.current_winnings

    def reset_pot_ticket(self):
        #Resets the numbers for Binghamton pot ticket
        self.winning_numbers = random.sample(range(1, 51), 5)
        self.your_numbers = random.sample(range(1, 51), 25)
        self.your_numbers_with_values = [(num, random.choice(self.cash_values_distribution)) for num in self.your_numbers]  

    def reset_wolves_ticket(self):
        #Resets the numbers for Seawolves ticket
        self.jackpot_numbers = random.sample(range(1, 11), 5)
        self.jackpot_ball_number = random.randint(1, 12)
        self.your_jackpot_numbers = random.sample(range(1,11), 5)
        self.your_jackpot_ball_number = random.randint(1,12)

    def add_char(self, char):
        #if the user types a number, add it to user_text
        if char.isdigit():
            self.user_text += char

    def remove_char(self):
        #Deletes previous character from user_text; essentially same thing as the backspace button on keyboard
        self.user_text = self.user_text[:-1]
        
    
    def purchase_big_pot_ticket(self):
        #subtracts the cost of the Binghamton pot ticket ($10) from user_text
        number = int(self.user_text)
        self.user_text = str(number - 10)
        return None
        

    def purchase_seawolves_jackpot(self):
        #substracts the cost of the Seawolves ticket ($5) from user_text
        number = int(self.user_text)
        self.user_text = str(number - 5)
        return None
    
    def binghamton_pot_winnings(self, last_winnings):
        # Add winnings from binghamton pot ticket to total winnings 
        self.winnings += last_winnings
        return None
    
    def calculate_winnings(self):
        # Check for matches and update winnings accordingly for the SEAWOLVES Ticket
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
        return self.ticket_winnings #updates total winnings and returns winnings for each individual seawolves ticket
    
    

    
        
        
    

   
