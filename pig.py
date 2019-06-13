import random

class Game():
    def __init__ (self):
        self.player = Player("Player")
        self.computerplayer = ComputerPlayer("Player")
        self.die = Die()

    def start_game (self):
        flip_coin = random.randint(1, 2)
        if flip_coin == 1:
            print("You will be Player 1.")
            input("Press <Enter> to continue")
            self.player.name = "Player 1 (You)"
            self.computerplayer.name = "Player 2 (CPU)"
            self.human_turn()
            
        else:
            print("You will be Player 2.")
            input("Press <Enter> to continue")
            self.player.name = "Player 2 (You)"
            self.computerplayer.name = "Player 1 (CPU)"
            self.computer_turn()
            

    def human_turn (self):
        score = 0
        turn_end = False
      
        while turn_end == False:
            roll = self.die.roll()
            print("Roll: ",roll)
            score += roll
            
          
            if roll == 1:
                print("Turn total: 0")
                self.scoreboard()
                print(f"It is {self.computerplayer.name}'s turn")
                input("Press <Enter> to continue")
                turn_end = True
                return self.computer_turn()

            print("Turn total: ",score)
            decision = input("Roll or Hold? ")
            if decision in ("Hold", "h", "H", "hold"):
                print("You have decided to hold.")
                self.player.score += score
                self.scoreboard()
                if self.player.score >= 100:
                    print("Congratulations! You win!")
                    turn_end = True
                else:
                    print(f"It is {self.computerplayer.name}'s turn")
                    input("Press <Enter> to continue")
                    turn_end = True
                    return self.computer_turn()

    def computer_turn (self):
        score = 0
        turn_end = False
      
        while turn_end == False:
            roll = self.die.roll()
            print("Roll: ",roll)
            score += roll

            if roll == 1:
                print("Turn total: 0")
                self.scoreboard()
                print(f"It is {self.player.name}'s turn")
                turn_end = True
                return self.human_turn()
        
            if score >= 20:
                print("Turn total: ",score)
                self.computerplayer.score += score
                self.scoreboard()
                if self.computerplayer.score >= 100:
                    print("The computer player wins!")
                    turn_end = True
                else:
                    print(f"It is {self.player.name}'s turn")
                    turn_end = True
                    return self.human_turn()

    def scoreboard (self):
        if self.player.name == "Player 1":
            print (self.player.name,": ",self.player.score)
            print (self.computerplayer.name,": ",self.computerplayer.score)
        else:
            print (self.computerplayer.name,": ",self.computerplayer.score)
            print (self.player.name,": ",self.player.score)      

class Player:

    def __init__ (self, name, score = 0):
        self.name = name
        self.score = score          

class ComputerPlayer:

    def __init__ (self, name, score = 0):
        self.name = name
        self.score = score

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


game = Game()
game.start_game()