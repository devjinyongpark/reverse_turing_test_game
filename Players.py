from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class Player():
    name: str

    def __init__(self, name):
        self.name = name

    def response(self, gamelog: str):
        raise NotImplementedError
    
    def vote(self, candidates, gamelog: str):
        raise NotImplementedError

class TooManyRedoError(Exception):
    pass

class AIPlayer(Player):
    name: str
    model: str

    def __init__(self, name):
        super().__init__(name)
        self.model = 'gpt-4o'
    
    def response(self, gamelog: str):
        response = client.responses.create(
            model = "gpt-4o",
            input = f"You are an AI playing Reverse Turing Test Game. \
                Your name is {self.name} \
                Responese to the lase round's question from the game host with few sentences. \
                Do not add your name at the start of the response. \
                Gamelog: \
                {gamelog}"
        )
        return response.output_text

    def vote(self, candidates: list, gamelog: str):
        redo_count = 0
        while True:
            response = client.responses.create(
                model = "gpt-4o",
                input = f"You are an AI playing Reverse Turing Test Game. \
                    Your name is {self.name} \
                    Vote the most suspicious player as a human based on the game log. \
                    You MUST ONLY output candidates name WITHOUT any explanations. \
                    Gamelog: \
                    {gamelog} \
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
    def response(self, gamelog: str):
        return input("Response: ")
    
    def vote(self, candidates: list[str], gamelog: str):
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