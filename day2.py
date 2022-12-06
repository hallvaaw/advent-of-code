import pandas as pd

data = pd.read_csv("puzzle_input_day2.txt", header = None, sep = " ")


# Match conditions
wins = [["A", "Y"], ["B", "Z"], ["C", "X"]]
draws = [["A", "X"], ["B", "Y"], ["C", "Z"]]
losses = [["A", "Z"], ["B", "X"], ["C", "Y"]]

def get_match_score(opponent, you):
    """Get the score from each match"""
    match_score = []
    match_score.extend([opponent, you])
    if match_score in wins:
        return 6
    elif match_score in draws:
        return 3
    else:
        return 0
            
def get_hand_score(hand):
    """Get the score from the hand"""
    if hand == "X":
        return 1
    elif hand == "Y":
        return 2
    else:
        return 3


# data['hand_scores'] = data["return_hands"].map(get_hand_score)
# data['match_scores'] = data[1].map(get_match_score)
# print(data['hand_scores'].sum() + data['match_scores'].sum())

# Part Two

def get_hand_score(hand):
    """Get the score from the hand"""
    if hand == "A":
        return 1
    elif hand == "B":
        return 2
    else:
        return 3

def return_hand(hand, match_outcome):
    """Hand to be returned determined by match outcome"""
    if match_outcome == "X":
        if hand == "A":
            return "C"
        elif hand == "B":
            return "A"
        elif hand == "C":
            return "B"
    elif match_outcome == "Y":
        if hand == "A":
            return "A"
        elif hand == "B":
            return "B"
        elif hand == "C":
            return "C"
    else:
        if hand == "A":
            return "B"
        elif hand == "B":
            return "C"
        elif hand == "C":
            return "A"

def get_match_scores(match):
    """Get the score from each match"""
    if match == "Z":
        return 6
    elif match == "Y":
        return 3
    else:
        return 0

data['return_hands'] = data.apply(lambda row: return_hand(row[0], row[1]), axis = 1)
data['hand_scores'] = data["return_hands"].map(get_hand_score)
data['match_scores'] = data[1].map(get_match_score)

print(data['hand_scores'].sum() + data['match_scores'].sum())
