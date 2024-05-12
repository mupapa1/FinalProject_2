class Candidate:
    def __init__(self, name: str):
        """Initialize a Candidate object with a name and votes count."""
        self.name = name
        self.votes = 0

    def add_vote(self):
        """Increment the votes count for the candidate by one."""
        self.votes += 1

    def __str__(self):
        """Return a string representation of the candidate."""
        return f"{self.name} - {self.votes}"
