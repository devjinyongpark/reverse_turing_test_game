from typing import Optional, Any
from Players import Player, UserPlayer, AIPlayer

        
class ReverseTuringTestGame():
    """
    Class for an instance of the game. 
    Note: if there is a tie then just play another round without voting out a player. 

    === Preconditions ===
    - self.difficulty in ['Easy', 'Normal', 'Hard']
    - 2 < self.number_of_ai < 5
    - 1 <= self.curr_round <= number_of_ai + 1
    """
    difficulty: str
    number_of_ai: int
    curr_round: int 
    players: dict[str, Player]
    is_playing: bool
    winner: Optional[str]
    gamelog: str
        
    def __init__(self, difficulty='Normal', number_of_ai=3):
        # Temporary
        self.difficulty = difficulty
        self.number_of_ai = number_of_ai
        self.curr_round = 1
        self.players = {} 
        self.winner = None
        self.gamelog = ""
        human_name  = input("Enter Your Name:")
        human = UserPlayer(human_name)
        self.players[human_name] = human
        for i in range(self.number_of_ai): 
            name = input("Enter Name for AI")
            name2 = AIPlayer(name) 
            self.players[name] = name2 

    def start(self):
        self.curr_round = 1
        self.is_playing = True

        while self.is_playing:
            self.proceed_round()

    def gameprint(self, name, content):
        line = f"{name}: {content}"
        print(line)
        self.gamelog += line

    def proceed_round(self):
        """
        Process
        - if it is the first round, Host explains the game instruction
        - Host asks a question.
        - Each Players answer the question in a random order:
        - Host: switch to the voting
        - Before voting, Every Player say their reasoning.
        - Each Player Vote anonymously.
        - Host: Shows who is the one got most vote. Reveal the identity.
        - If it is the user, game ends. change self.is_playing to False and change self.winner to 'AIs'
        """
        # TODO: if it is the first round, Host explains the game instruction

        # TODO: Host asks a question.

        # TODO: Each Players answer the question in a random order:

        # Host: switch to the voting
        self.gameprint("Host", "Now, we've gathered all answers. \
                       Before voting, share your thought on who is a human.")

        # TODO: Before voting, Every Player say their reasoning.

        # Host: Voting
        self.gameprint("Host", "Moment of Truth. \
                       Vote who do you think the most suspicious player as human.")

        # TODO: Each Player Vote anonymously.

        # TODO: Host: Shows who is the one got most vote. Reveal the identity.
        
        # TODO: If it is the user, game ends. change self.is_playing to False and change self.winner to 'AIs'
        




if __name__ == "__main__":
    Game = ReverseTuringTestGame()
    Game.start()
