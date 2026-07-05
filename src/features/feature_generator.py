from src.features.team_stats import (
    get_matches_played,
    get_wins,
    get_win_rate,
    get_average_goals_scored,
    get_average_goals_conceded,
)

def create_match_features(matches, match_row):
    features = {}

    features["home_matches"] = get_matches_played(
        matches,
        match_row["home_team"],
        match_row["date"]
    )

    features["away_matches"] = get_matches_played(
        matches,
        match_row["away_team"],
        match_row["date"]
    )

    features["home_wins"] = get_wins(
        matches,
        match_row["home_team"],
        match_row["date"]
    )

    features["away_wins"] = get_wins(
        matches,
        match_row["away_team"],
        match_row["date"]
    )

    features["home_win_rate"] = get_win_rate(
        matches,
        match_row["home_team"],
        match_row["date"]
    )

    features["away_win_rate"] = get_win_rate(
        matches,
        match_row["away_team"],
        match_row["date"]
    )

    features["home_avg_goals"] = get_average_goals_scored(
        matches,
        match_row["home_team"],
        match_row["date"]
    )

    features["away_avg_goals"] = get_average_goals_scored(
        matches,
        match_row["away_team"],
        match_row["date"]
    )

    features["home_avg_goals_conceded"] = get_average_goals_conceded(
        matches,
        match_row["home_team"],
        match_row["date"]
    )

    features["away_avg_goals_conceded"] = get_average_goals_conceded(
        matches,
        match_row["away_team"],
        match_row["date"]
    )

    features["neutral"] = int(match_row["neutral"])

    return features