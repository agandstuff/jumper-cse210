class Guesser:
    """The user who is guessing letters to find the code word. 
    
    Attributes:
        _guess(list): the list holding the current guess of the user.
        
    """


    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._guess = []

        
    def resetGuess(self, codeword):
        for l in codeword:  
            self._guess.append("_")
        

    def newLetterGuess(self, index, letter):
        """Updates the current shown guess.

        Args:
            self (Guesser): An instance of Guesser.
            letter (str): The inputed letter from the terminal.
        """

        for i in index:
            self._guess[i] = letter
