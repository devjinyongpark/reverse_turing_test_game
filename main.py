from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import Optional, Any

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class Player():
    name: str

    def __init__(self, name):
        self.name = name

    def response(self):
        raise NotImplementedError
    
    def vote(self, candidates):
        raise NotImplementedError

class TooManyRedoError(Exception):
    pass

class AIPlayer(Player):
    name: str
    model: str

    def __init__(self, name):
        super().__init__(name)
        self.model = 'gpt-4o'
    
    def response(self, chatlog: str):
        response = client.responses.create(
            model = "gpt-4o",
            input = f"You are an AI playing Reverse Turing Test Game. \
                Your name is {self.name} \
                Responese to the lase round's question from the game host. \
                Chatlog: \
                {chatlog}"
        )
        return response.output_text

    def vote(self, candidates: list, chatlog: str):
        redo_count = 0
        while True:
            response = client.responses.create(
                model = "gpt-4o",
                input = f"You are an AI playing Reverse Turing Test Game. \
                    Your name is {self.name} \
                    Vote the most suspicious player as a human. \
                    You MUST ONLY output candidates name WITHOUT any explanations. \
                    Chatlog: \
                    {chatlog} \
                    Candidates: \
                    {', '.join(candidates)}"
            )
            target = response.output_text
            if target in candidates: 
                return target
            if redo_count > 10:
                raise TooManyRedoError
            redo_count += 1

class UserPlayer(Player):
    def response(self):
        return input("Response: ")
    
    def vote(self, candidates: list[str]):
        """
        Print Candidate list
        Return one of the candidate name in the candidates.
        If it is not in the list, repeat again."""
        print(candidates)
        vote = input("Vote for") 
        valid = False 
        while not valid: 
            if vote in candidates: 
                valid = True 
            else: 
                print("Not Valid")
                vote = input("Vote for")
        return vote 
        
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
        
    def __init__(self, difficulty='Normal', number_of_ai=3):
        # Temporary
        self.difficulty = difficulty
        self.number_of_ai = number_of_ai
        self.curr_round = 1
        self.players = {} 
        self.winner = None
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



if __name__ == "__main__":
    Game = ReverseTuringTestGame()
    Game.start()
