score_from_first_match = input()
score_from_second_match = input()
score_from_third_match = input()

home_goals1, away_goals1 = score_from_first_match[0], score_from_first_match[2]
home_goals2, away_goals2 = score_from_second_match[0], score_from_second_match[2]
home_goals3, away_goals3 = score_from_third_match[0], score_from_third_match[2]

wins = int(home_goals1 > away_goals1) + int(home_goals2 > away_goals2) + int(home_goals3 > away_goals3)
losses = int(home_goals1 < away_goals1) + int(home_goals2 < away_goals2) + int(home_goals3 < away_goals3)
draws = int(home_goals1 == away_goals1) + int(home_goals2 == away_goals2) + int(home_goals3 == away_goals3)

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")