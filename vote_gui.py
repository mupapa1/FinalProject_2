import tkinter as tk
from tkinter import messagebox, simpledialog
from vote_tracker import VoteTracker

class VoteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vote Counter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.vote_tracker = VoteTracker(["Bianca", "Edward", "Felicia"])

        self.vote_menu()

    def vote_menu(self):
        self.clear_frame()
        tk.Label(self.root, text="VOTE MENU").pack()
        tk.Label(self.root, text="v: Vote\nx: Exit").pack()

        option = tk.StringVar()
        entry = tk.Entry(self.root, textvariable=option)
        entry.pack()

        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.process_vote(option.get().strip().lower()))
        submit_button.pack()

    def process_vote(self, option):
        if option == "v":
            voter_id = self.get_voter_id()
            if voter_id:
                self.candidate_menu(voter_id)
        elif option == "x":
            self.show_results()
        else:
            messagebox.showerror("Error", "Invalid option. Please enter 'v' to vote or 'x' to exit.", icon="error")

    def candidate_menu(self, voter_id):
        self.clear_frame()
        tk.Label(self.root, text="CANDIDATE MENU").pack()

        candidate_option = tk.IntVar()
        for i, candidate in enumerate(self.vote_tracker.candidates, 1):
            tk.Radiobutton(self.root, text=candidate.name, variable=candidate_option, value=i).pack(anchor="w")

        back_button = tk.Button(self.root, text="Back", command=self.vote_menu)
        back_button.pack()

        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.process_candidate_vote(voter_id, candidate_option.get()))
        submit_button.pack()

    def process_candidate_vote(self, voter_id, candidate_index):
        if candidate_index == 0:
            messagebox.showerror("Error", "Please select a candidate.", icon="error")
        else:
            try:
                self.vote_tracker.vote(candidate_index - 1, voter_id)
                messagebox.showinfo("Success", f"Voted {self.vote_tracker.candidates[candidate_index - 1].name}", icon="info")
                self.vote_menu()
            except ValueError as e:
                messagebox.showerror("Error", str(e), icon="error")

    def get_voter_id(self):
        voter_id = simpledialog.askstring("Voter ID", "Enter your unique identifier (5-digit number):")
        while voter_id is not None and (not voter_id.isdigit() or len(voter_id) != 5):
            voter_id = simpledialog.askstring("Voter ID", "Invalid identifier. Please enter a 5-digit number:")
        return voter_id

    def show_results(self):
        self.clear_frame()
        results = self.vote_tracker.get_results()
        tk.Label(self.root, text="RESULTS").pack()
        tk.Label(self.root, text=results).pack()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
