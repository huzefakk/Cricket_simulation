#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        """
        Initialize a cricket player with attributes.
        """
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience
        self.stamina = 100

class Team:
    def __init__(self, name, players):
        """
        Initialize a cricket team with players.
        """
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []  # Will be set later
        self.total_runs = 0
        self.total_wickets = 0
        self.current_batsman_index = 0

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """
        Initialize field conditions for a cricket match.
        """
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

class Umpire:
    def __init__(self, match):
        """
        Initialize an umpire to oversee the match.
        """
        self.match = match
        self.scores = {self.match.team1.name: 0, self.match.team2.name: 0}
        self.wickets = {self.match.team1.name: 0, self.match.team2.name: 0}
        self.overs = 0

    def is_innings_over(self):
        """
        Check if the current innings is over based on overs or wickets.
        """
        max_overs = 50  # Maximum overs per innings
        max_wickets = 10  # Maximum wickets per innings

        if self.overs >= max_overs or self.wickets[self.match.current_batting_team.name] >= max_wickets:
            return True
        else:
            return False

    def predict_outcome(self, batsman, bowler):
        """
        Simulate outcome of a ball based on player attributes.
        """
        batting_skill = batsman.batting * (1 - bowler.bowling)
        random_number = random.random()

        if random_number < 0.05:  # 5% chance of an exceptional delivery
            batting_skill *= 0.2

        if random_number < batting_skill:
            self.wickets[self.match.current_batting_team.name] += 1
            outcome = "OUT"
        else:
            outcome = "RUNS"
        return outcome



class Commentator:
    def provide_commentary(self, event):
        """
        Provide commentary based on the event of the match.
        """
        if event == "OUT":
            return "Wicket!"
        else:
            return "Runs scored!"

class Match:
    def __init__(self, team1, team2, field):
        """
        Initialize a cricket match between two teams.
        """
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.innings = 1
        self.current_batting_team = None
        self.current_bowling_team = None
        self.current_batsman = None
        self.current_bowler = None
        self.current_batsman_index = 0
        self.overs = 0
        self.umpire = Umpire(self)
        self.commentator = Commentator()
        self.scores = {
            team1.name: 0,
            team2.name: 0
        }

    def start_match(self):
        """
        Start the cricket match and set initial conditions.
        """
        self.current_batting_team = self.team1
        self.current_bowling_team = self.team2
        self.current_batsman_index = 0
        self.current_batsman = self.current_batting_team.batting_order[self.current_batsman_index]
        self.current_bowler = self.current_bowling_team.players[0]
        print(f"Match between {self.team1.name} and {self.team2.name} has started!")

    def change_innings(self):
        """
        Change innings and update match details.
        """
        self.overs = 0
        self.umpire.overs = 0
        self.umpire.scores = {
            self.team1.name: 0,
            self.team2.name: 0
        }
        self.umpire.wickets = {
            self.team1.name: 0,
            self.team2.name: 0
        }
        self.current_batsman_index = 0
        if self.innings == 1:
            self.innings = 2
            self.current_batting_team, self.current_bowling_team = self.team2, self.team1
        else:
            self.end_match()
            return
        self.current_batsman = self.current_batting_team.batting_order[self.current_batsman_index]
        self.current_bowler = self.current_bowling_team.players[0]
        print(f"Change of innings: {self.current_batting_team.name} is now batting.")

    def simulate_ball(self):
        """
        Simulate a ball and update match details based on outcome.
        """
        batsman = self.current_batsman
        bowler = self.current_bowler
        outcome = self.umpire.predict_outcome(batsman, bowler)  # Define outcome here
        commentary = self.commentator.provide_commentary(outcome)

        batsman_team = self.current_batting_team.name
        bowler_team = self.current_bowling_team.name

        print(f"{batsman.name} ({batsman_team}) facing {bowler.name} ({bowler_team}): {commentary}")

        if outcome == "RUNS":
            runs = random.randint(0, 6)
            print(f"{runs} runs scored.")
            self.umpire.scores[self.current_batting_team.name] += runs
        else:
            self.umpire.wickets[self.current_batting_team.name] += 1
            print("Wicket!")

        self.umpire.overs += 0.1
        if self.umpire.overs % 1 == 0:
            print(f"{self.umpire.overs:.1f} overs completed.")   
            
            
    def simulate_innings(self):
        """
        Simulate an innings with multiple balls.
        """
        while not self.umpire.is_innings_over():
            self.simulate_ball()
            if self.umpire.is_innings_over():
                break
            self.current_batsman_index += 1
            if self.current_batsman_index >= len(self.current_batting_team.batting_order):
                self.change_innings()
                break
        if self.umpire.is_innings_over() and self.innings == 2:
            self.end_match()

    def end_match(self):
        """
        End the cricket match and display match summary.
        """
        print("Match ended.")
        print(f"{self.team1.name} scored {self.umpire.scores[self.team1.name]} runs for {self.umpire.wickets[self.team1.name]} wickets in {self.umpire.overs:.1f} overs.")
        print(f"{self.team2.name} scored {self.umpire.scores[self.team2.name]} runs for {self.umpire.wickets[self.team2.name]} wickets.")

        if self.umpire.scores[self.team1.name] > self.umpire.scores[self.team2.name]:
            print(f"{self.team1.name} wins by {self.umpire.scores[self.team1.name] - self.umpire.scores[self.team2.name]} runs!")
        elif self.umpire.scores[self.team1.name] < self.umpire.scores[self.team2.name]:
            print(f"{self.team2.name} wins by {self.umpire.scores[self.team2.name] - self.umpire.scores[self.team1.name]} runs!")
        else:
            print("The match ended in a tie!")
            
# Create players for both teams
player1 = Player("Player 1", 0.7, 0.1, 0.9, 0.7, 0.8)
player2 = Player("Player 2", 0.6, 0.2, 0.85, 0.6, 0.7)
player3 = Player("Player 3", 0.5, 0.3, 0.8, 0.5, 0.6)
player4 = Player("Player 4", 0.4, 0.4, 0.75, 0.4, 0.5)
player5 = Player("Player 5", 0.3, 0.5, 0.7, 0.3, 0.4)
player6 = Player("Player 6", 0.6, 0.1, 0.85, 0.6, 0.7)
player7 = Player("Player 7", 0.5, 0.2, 0.8, 0.5, 0.6)
player8 = Player("Player 8", 0.4, 0.3, 0.75, 0.4, 0.5)
player9 = Player("Player 9", 0.3, 0.4, 0.7, 0.3, 0.4)
player10 = Player("Player 10", 0.2, 0.5, 0.65, 0.2, 0.3)

# Create teams
team1 = Team("Team A", [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10])
team2 = Team("Team B", [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10])

# Set batting order for each team (20-overs match)
team1.batting_order = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
team2.batting_order = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]

# Create a match with field details
field = Field("Large", 0.8, "Dry", 1.2)
match = Match(team1, team2, field)

# Start the match and simulate innings
match.start_match()
match.simulate_innings()
match.simulate_innings()

# End the match and display results
match.end_match()


# In[ ]:




