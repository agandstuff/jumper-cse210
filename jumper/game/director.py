from game.terminal import Terminal
from game.jumper import Jumper
from game.guesser import Guesser


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _jumper (Jumper): The parachuting guy.
        _playGame (boolean): Whether or not to keep playing.
        _guesser (Guesser): The game's guesser - user playing.
        _terminal: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal = Terminal()
        self._jumper = Jumper()
        self._guesser = Guesser()
        self._playGame = True
        
        
    def startGame(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal.write_text(r"""
            Our jumper needs your help! Guess the codeword to help him land safely.
            
                    ___
                   /___\
                   \   /
                    \ /
                     O
                    /|\
                    / \


                

                ^^^^^^^^^^^        
                """)

        self._jumper.setCodeword()
        self._guesser.resetGuess(self._jumper._codeword)

        self._terminal.write_text(" ".join(self._guesser._guess))

        while self._playGame:
            self._getInput()
            self._outputs()
            self._updateGame()

    def _getInput(self):
        """Gets the users guess.

        Args:
            self (Director): An instance of Director.
        """
        codeword = self._jumper._codeword
        newLetter = self._terminal.read_text("Guess a letter [a-z]: ")
        newLetter.lower()

        if newLetter in codeword:
            letterIndex = []
            for l in range(len(codeword)):
                if codeword[l] == newLetter:
                    letterIndex.append(l)
                
            self._guesser.newLetterGuess(letterIndex, newLetter)
        else:
            self._jumper.wrongGuess()


    def _updateGame(self):
        """Compares users guess to code word and checks parachute level.

        Args:
            self (Director): An instance of Director.
        """
        if ("".join(self._guesser._guess)) == self._jumper._codeword:
            self._terminal.write_text("Congratulations! The jumper landed safely.")
            self._terminal.write_text(r"""
   
                    \O/
                     |    ____ 
                    / \ /    | \
                ^^^^^^^^^^^^^^^^^        
                """)
            self._playGame = False
        elif self._jumper.isAlive() == False:
            self._terminal.write_text("Oh no! All out of parachutes...")
            self._playGame = False
        
    def _outputs(self):
        """Prints users guesses and jumper rendering.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal.write_text("\n")
        self._terminal.write_text(" ".join(self._guesser._guess))

        match self._jumper._parachutes:
            case 4:
                self._terminal.write_text(r"""
                    ___
                   /___\
                   \   /
                    \ /
                     O
                    /|\
                    / \


                

                ^^^^^^^^^^^        
                """)
            case 3:
                self._terminal.write_text(r"""
                   /___\
                   \   /
                    \ /
                     O
                    /|\
                    / \

                

                ^^^^^^^^^^^        
                """)
            case 2:
                self._terminal.write_text(r"""
                   \   /
                    \ /
                     O
                    /|\
                    / \

                
                ^^^^^^^^^^^        
                """)

            case 1:
                self._terminal.write_text(r"""
                    \ /
                 ! ! O ! !
                    /|\
                    / \

                ^^^^^^^^^^^        
                """)

            case 0:
                self._terminal.write_text(r"""
                            ___
                           / -- \
                  }--;-(x) | -- |
                ^^^^^^^^^^^^^^^^^^  
                """)
            case _:
                self._terminal.write_text(r"""
                    ___
                   /___\
                   \   /
                    \ /
                     O
                    /|\
                    / \


                

                ^^^^^^^^^^^        
                """)