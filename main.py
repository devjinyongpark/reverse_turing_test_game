class Player():
    name: str

    def __init__(self, name):
        self.name = name

    def response(self):
        raise NotImplementedError
    
    def vote(self, candidates):
        raise NotImplementedError

class AIPlayer(Player):
    name: str
    model: str

    def __init__(self, name):
        super().__init__(name)
        self.model = 'gpt-4o'
        raise NotImplementedError
    
    def response(self, chatlog: str):
        raise NotImplementedError

    def vote(self, candidates: list, chatlog: str):
        raise NotImplementedError


class UserPlayer(Player):
    def response(self):
        return input("Response: ")
    
    def vote(self, candidates: list[str]):
        """
        Print Candidate list
        Return one of the candidate name in the candidates.
        If it is not in the list, repeat again."""
        raise NotImplementedError

class ReverseTuringTestGame():
    """
    === Preconditions ===
    - self.difficulty in ['Easy', 'Normal', 'Hard']
    - 2 < self.number_of_ai < 5
    - 1 <= self.curr_round <= number_of_ai + 1
    """
    difficulty: str
    number_of_ai: int
    curr_round: int
    ai_profiles: str
    is_playing: bool
        
    def __init__(self):
        # Temporary
        self.difficulty = 'Normal'
        self.number_of_ai = 3
    
    def start(self):
        self.curr_round = 1
        self.is_playing = True

        while self.is_playing:
            self.proceed_round()


    def proceed_round(self):



if __name__ == "__main__":
    Game = ReverseTuringTestGame()
    Game.start()
