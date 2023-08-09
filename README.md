# Cricket Simulation Project

## Overview

This project is a cricket simulation program that simulates a cricket match between two teams. The simulation involves player statistics, umpire decisions, and commentary to create a realistic match experience.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Demo Video](#demo-video)
- [Author](#author)
- [License](#license)

## Features

- Simulates a cricket match between two teams with batting, bowling, and fielding statistics.
- Includes player attributes such as batting, bowling, fielding, running, and experience.
- Uses random outcomes to determine runs scored and wickets taken during the match.
- Provides commentary for each ball, including runs scored and wickets taken.
- Ends the match based on the maximum number of overs or wickets reached.

## Requirements

- Python 3.x
- Git (for cloning the repository)

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/huzefakk/Cricket_tournament.git

## Video
link:https://drive.google.com/drive/folders/1KLJ8AzzyrvkWmaWymosUkXZudfS7Gecj?usp=sharing

## Methodology

This project simulates a cricket match using Python. The simulation includes two cricket teams, each with individual players possessing batting, bowling, fielding, running, and experience attributes. The goal of the simulation is to provide a realistic representation of a cricket match, where players' attributes influence the outcomes of balls and innings.

### Classes and Components

The simulation is implemented using the following classes and components:

1. `Player`: Represents a cricket player with attributes like batting, bowling, fielding, running, and experience.

2. `Team`: Represents a cricket team consisting of players. It includes attributes for the team's name, batting order, and match statistics.

3. `Field`: Defines field conditions for the match, including size, fan ratio, pitch conditions, and home advantage.

4. `Umpire`: Simulates an umpire overseeing the match, making decisions based on player attributes to predict ball outcomes.

5. `Commentator`: Provides commentary for the match events, such as wickets and runs scored.

6. `Match`: Represents a cricket match between two teams. It manages innings, players, overs, and match results.

### Simulation Flow

1. Players are created for both teams, each with unique attributes representing their skills.

2. Teams are initialized with players and batting orders. A field is also defined with specific conditions.

3. The match starts, and innings are simulated for both teams. The umpire predicts ball outcomes based on player attributes.

4. Commentary is provided for each ball, indicating whether runs were scored or a wicket fell.

5. Innings continue until the maximum overs are bowled or all wickets are taken.

6. The match ends, and the final scores and match result are displayed.

### Instructions to Run

1. Ensure you have Python installed on your machine.

2. Clone this repository to your local machine/ Copy paste the code in Jupyter
