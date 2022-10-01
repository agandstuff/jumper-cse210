import random

class Jumper:
    """The parachuting guy. 
    
    The responsibility of Jumper is to keep track of the code word and amount of parachute left. 
    
    Attributes:
        _codeword (string): The hidden word to be guessed.
        _codes (list): List of possible codewords.
        _parachutes (int): The lives remaining, incorrect guesses reduces this, game ends when lives are gone.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._codeword = ""
        self._codes = [
                        "alpha", 
                        "bravo", 
                        "charlie", 
                        "delta", 
                        "echo", 
                        "foxtrot", 
                        "golf", 
                        "hotel", 
                        "india", 
                        "juliet", 
                        "kilo", 
                        "lima", 
                        "mike", 
                        "november", 
                        "oscar", 
                        "papa", 
                        "quebec", 
                        "romeo", 
                        "sierra", 
                        "tango", 
                        "uniform", 
                        "victor", 
                        "whiskey", 
                        "xray", 
                        "yankee", 
                        "zulu"]
        self._parachutes = 4
    
    def setCodeword(self):
        """Assigns and returns the current codeword.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._codeword = random.choice(self._codes)
        
    def wrongGuess(self):
        """If wrong guess occurs, this reduces the parachutes left.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._parachutes -= 1


    def isAlive(self):
        """Whether or not the codeword has been found.

        Args:
            self (Jumper): An instance of Jumper.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        if self._parachutes == 0:
            return False
        else:
            return True