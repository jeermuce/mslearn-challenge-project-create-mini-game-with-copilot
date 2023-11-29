class GameState:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.ratio = 0
    
    def update(self, result):
        if result == 'win':
            self.wins += 1
        elif result == 'loss':
            self.losses += 1
        else:
            self.ties += 1
            
    
    def print_stats(self):
        print(f"Wins-Ties-Losses: {self.wins}:{self.ties}:{self.losses}")
