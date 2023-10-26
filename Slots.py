import random
import statistics
import time
from multiprocessing import Pool

class player:
    def __init__(self, cash, bet):
        self.startcash = cash
        self.cash = cash
        self.bet = bet
    
    def checkCash(self):
        if self.cash <= 0:
            #print("You have no more money! Game over!")
            return False
        else:
            return True
    
    def outcome(self):
        x = random.random()
        if x <= 19/64:
            #BAR/BAR/BAR
            if 0 <= x <= 1/64:
                return self.bet * 20
            #BELL/BELL/BELL
            elif 1/64 < x <= 2/64:
                return self.bet * 15
            #LEMON/LEMON/LEMON
            elif 2/64 < x <= 3/64:
                return self.bet * 5
            #CHERRY/CHERRY/CHERRY
            elif 3/64 < x <= 4/64:
                return self.bet * 3
            #CHERRY/CHERRY/?
            elif 4/64 < x <= 7/64:
                return self.bet * 2
            #CHERRY/?/?
            else:
                return self.bet * 1
        #LOSE
        return self.bet * -1

    
    def playGame(self):
        cnt = 0
        while self.checkCash() == True:
            x = self.outcome()
            self.cash += x
            #print(self.cash)
            cnt += 1
            if cnt > 50000:
                break
            #time.sleep(.01)
        return cnt
    
    def simulate(self, iters):
        plays = []
        for i in range(iters):
            plays.append(self.playGame())
            #print("Game ", i+1, " finished!")
            #print("Completed ", plays[i], " plays!")
            self.cash = self.startcash
        return plays  

def main():
    p = player(10, 1)
    game_results = p.simulate(1000)
    print("Maximum number of plays per game: 50,000")
    print("Number of games: ", len(game_results))
    print("Mean: ", statistics.mean(game_results))
    print("Median: ", statistics.median(game_results))
    pass

if __name__ == "__main__":
    main()


