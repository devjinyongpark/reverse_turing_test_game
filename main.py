from typing import Optional, Any
from Players import Player, UserPlayer, AIPlayer
import random 

def get_random_question():
        filename = 'questions.txt'
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            
            if lines:
                # random.choice selects a random element from a sequence
                return random.choice(lines).strip() # Use .strip() to remove extra newlines
            else:
                return None # Handle empty file case
        except FileNotFoundError:
            return "Error: File not found"
        
class ReverseTuringTestGame():
    """
    Class for an instance of the game. 
    Note: if there is a tie then just play another round without voting out a player. 

    === Preconditions ===
    - self.difficulty in ['Easy', 'Normal', 'Hard']
    - 2 < self.number_of_ai < 5
    - 1 <= self.curr_round <= number_of_ai + 1
    - No player can be named "Host" and no player can have the same name 
    - len(self.players) >= 3
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
        self.end_event()

    def end_event(self):
        pass

    def gameprint(self, name, content):
        line = "\n"
        if name == "":
            line += content
        else:
            line += f"{name}: {content}"
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
        # Round Indicator
        self.gameprint(f"========== Round {self.curr_round} ==========")
        self.gameprint(f"    Remaining Players: {len(self.players)}")

        # if it is the first round, Host explains the game instruction
        if self.curr_round == 1: 
            self.gameprint("Host","There is a human among us. We must eliminate them, and if you are the human SURRENDER!!!")

        # Host asks a question.
        question = get_random_question()
        self.gameprint("Host", question)

        #Each Players answer the question in a random order:
        random.shuffle(list(self.players.values()))
        for player in self.players.values(): 
            self.gameprint(player.name, player.response(self.gamelog))

        # Host: switch to the voting
        self.gameprint("Host", "Now, we've gathered all answers. \
                       Before voting, share your thought on who is a human.")

        #Before voting, Every Player say their reasoning.
        random.shuffle(list(self.players.values()))
        for player in self.players.values(): 
            self.gameprint(player.name, player.response(self.gamelog))

        # Host: Voting
        self.gameprint("Host", "Moment of Truth. \
                       Vote who do you think the most suspicious player as human.")

        # Each Player Vote anonymously.
        voted_players = {player: 0 for player in self.players}
        for player in self.players.values:
            target = player.vote(self.players.keys, self.gamelog)
            voted_players[target] += 1
        
        most_vote = max(voted_players.values)
        is_there_a_tie = list(voted_players.values).count(most_vote) > 1
        targets = [name for name in voted_players.keys() if voted_players[name] == most_vote]

        # Host: Shows who is the one got most vote. Reveal the identity.
        if is_there_a_tie and len(most_vote) == 2:
            self.gameprint("Host", f"There was a Tie between {targets[0]} and {targets[1]} with {most_vote} votes each.\nGame continues.")
        elif is_there_a_tie:
            self.gameprint("Host", f"There was a Tie between {', '.join(targets[:-1])} and {targets[-1]} with {most_vote} votes each.\nGame continues.")
        else:
            eliminated_player = self.players[targets[0]]
            self.gameprint("Host", f"{eliminated_player.name} got the most vote({most_vote}).")
            if isinstance(eliminated_player, UserPlayer):
                self.gameprint("Host", f"{eliminated_player.name} is Eliminated.\n{eliminated_player.name} was a human.")
                self.players.pop(eliminated_player.name)
            elif isinstance(eliminated_player, AIPlayer):
                self.gameprint("Host", f"{eliminated_player.name} is Eliminated.\n{eliminated_player.name} was an AI.")
                self.players.pop(eliminated_player.name)
            else:
                raise TypeError("Player has to be either UserPlayer or AIPlayer.")

        # TODO: If it is the user, game ends. change self.is_playing to False and change self.winner to 'AIs'
        if isinstance(target, UserPlayer): 
            self.playing = False 
            self.winner = 'AIs'
            
        else: 
            self.curr_round += 1 

        




if __name__ == "__main__":
    Game = ReverseTuringTestGame()
    Game.start()
