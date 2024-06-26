import csv
from typing import List
from candidate import Candidate

class VoteTracker:
    def __init__(self, candidates: List[str]):
        """Initialize with a list of candidate names."""
        self.candidates = [Candidate(name) for name in candidates]
        self.voted_ids = set()

    def vote(self, candidate_index, voter_id):
        """Vote for a candidate with the given candidate index and voter ID."""
        if 0 <= candidate_index < len(self.candidates) and voter_id not in self.voted_ids:
            self.candidates[candidate_index].add_vote()
            self.voted_ids.add(voter_id)
            self.write_to_csv(candidate_index, voter_id)
        elif voter_id in self.voted_ids:
            raise ValueError("You have already voted.")
        else:
            raise ValueError("Invalid candidate index.")

    def get_results(self):
        """Get the voting results."""
        total_votes = sum(candidate.votes for candidate in self.candidates)
        results = [str(candidate) for candidate in self.candidates] + [f"Total - {total_votes}"]
        return ", ".join(results)

    def write_to_csv(self, candidate_index, voter_id):
        """Write the voting information to a CSV file."""
        with open('votes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, self.candidates[candidate_index].name])
