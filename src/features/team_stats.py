import pandas as pd

def get_team_history(matches, team_name, match_date):
    """
    Returns all matches played by a team BEFORE a given date. It will return ONLY the results before thsi date because we don't know that result of the day's match yet.
    """

    history = matches[
        (
            (matches["home_team"] == team_name)
            |
            (matches["away_team"] == team_name)
        )
        &
        (matches["date"] < match_date)
    ]

    return history


    
def get_matches_played(matches, team_name, match_date):
    
    history = get_team_history(
        matches,
        team_name,
        match_date
    )

    return len(history)


def get_wins(matches, team_name, match_date):
    
    history = get_team_history(
        matches,
        team_name,
        match_date
    )

    wins = 0

    for _, match in history.iterrows():

        if (
            match["home_team"] == team_name
            and match["home_score"] > match["away_score"]
        ):
            wins += 1

        elif (
            match["away_team"] == team_name
            and match["away_score"] > match["home_score"]
        ):
            wins += 1

    return wins


# Average goals scored
def get_average_goals_scored(matches, team_name, match_date):
    
    history = get_team_history(matches, team_name, match_date)

    if len(history) == 0:
        return 0

    goals = 0

    for _, match in history.iterrows():

        if match["home_team"] == team_name:
            goals += match["home_score"]
        else:
            goals += match["away_score"]

    return goals / len(history)



# Average goals conceded
def get_average_goals_conceded(matches, team_name, match_date):
    
    history = get_team_history(matches, team_name, match_date)

    if len(history) == 0:
        return 0

    goals = 0

    for _, match in history.iterrows():

        if match["home_team"] == team_name:
            goals += match["away_score"]
        else:
            goals += match["home_score"]

    return goals / len(history)


# Win rate
def get_win_rate(matches, team_name, match_date):
    
    matches_played = get_matches_played(
        matches,
        team_name,
        match_date
    )

    if matches_played == 0:
        return 0

    wins = get_wins(
        matches,
        team_name,
        match_date
    )

    return wins / matches_played

