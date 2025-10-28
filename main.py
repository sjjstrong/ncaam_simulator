import random

################################################################################
#   CBB Game Result Simulator
#
#   Notes
#
#   Adjust ratios so that result isn't as concrete. Switching the home team
#   made it go from a 7:8 ratio to a 15:0 ratio.
#
################################################################################


def simulate_game(team1_stats, team2_stats, rivalry):
    """
    Simulates a basketball game using the given stats for two teams.

    :param team1_stats: Dictionary of stats for Team 1.
    :param team2_stats: Dictionary of stats for Team 2.
    :return: Simulated scores for Team 1 and Team 2.
    """

    weights = {
        "assist_turnover_ratio": 1,
        "effective_fg_pct": 3,
        "fg_pct_defense": 3,
        "rebound_margin": 0.2, #could lower or raise
        "offensive_rebounds": 0.2, #could lower
        "three_point_pct": 5,
        "turnover_margin": .05, #could lower or remove completely
    }

    def calculate_score(stats):
        """Calculate a score based on stats and weights."""
        score = 0
        for stat, weight in weights.items():
            score += (stats[stat] * weight * random.uniform(0.95, 1.05))
        return score

    # Calculate base scores
    team1_base_score = calculate_score(team1_stats)
    team2_base_score = calculate_score(team2_stats)

    # Add randomness to simulate variability in performance
    if rivalry == False:
        team1_random_factor = random.uniform(0.80, 1.2)
        team2_random_factor = random.uniform(0.80, 1.2)
    else:
        team1_random_factor = random.uniform(0.65, 1.35)
        team2_random_factor = random.uniform(0.65, 1.35)

    home = random.uniform(1.01, 1.03)
    away = random.uniform(0.97, 0.99)

    team1_final_score = round(team1_base_score * away * team1_random_factor * 2.5)  # Set home and away team here
    team2_final_score = round(team2_base_score * home * team2_random_factor * 2.5)

    return team1_final_score, team2_final_score


if __name__ == "__main__":

    rivalry = False

    # Team stats

    team1_stats = {
        "assist_turnover_ratio": 1.21,
        "effective_fg_pct": 0.551,
        "fg_pct_defense": (1 - .40131),
        "rebound_margin": 2.0,
        "offensive_rebounds": 9.29,
        "three_point_pct": 0.3736,
        "turnover_margin": 0.3,
    }

    team2_stats = {
        "assist_turnover_ratio": 1.23,
        "effective_fg_pct": 0.516,
        "fg_pct_defense": (1 - 0.39668),
        "rebound_margin": 11.0,
        "offensive_rebounds": 13.81,
        "three_point_pct": 0.3142,
        "turnover_margin": -1.9,
    }

    # Simulate 100 games
    num_games = 1000
    team1_wins = 0
    team2_wins = 0
    team1_margin = 0
    team2_margin = 0

    for _ in range(num_games):
        team1_score, team2_score = simulate_game(team1_stats, team2_stats, rivalry)

        if team1_score > team2_score:
            team1_margin += (team1_score - team2_score)
        if team1_score < team2_score:
            team2_margin += (team2_score - team1_score)


        if team1_score > team2_score:
            team1_wins += 1
        elif team2_score > team1_score:
            team2_wins += 1

    # Calculate average margin of victory
    team1_avg_margin = team1_margin / num_games
    team2_avg_margin = team2_margin / num_games
    avg_margin  = (team1_avg_margin + team2_avg_margin)/2

    # Results
    print(f"Number of Games Simulated: {num_games}")
    print(f"Team 1 (Ohio St.) Wins: {team1_wins}   Average Margin of Victory: {team1_avg_margin:.2f}")
    print(f"Team 2 (Illinois) Wins: {team2_wins}    Average Margin of Victory: {team2_avg_margin:.2f}")
    print(f'Average Overall Margin of Victory: {avg_margin:.2f}')
