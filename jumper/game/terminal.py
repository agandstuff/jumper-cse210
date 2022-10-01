class Terminal:
    """A service that handles terminal operations.
    
    The responsibility of Terminal is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (Terminal): An instance of Terminal.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (Terminal): An instance of Terminal.
            text (string): The text to display.
        """
        print(text)