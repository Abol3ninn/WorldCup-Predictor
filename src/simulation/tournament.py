import numpy as np
import pandas as pd

class TournamentSimulator:

    def __init__(self, model):
        self.model = model

    def predict_match(self, home_team, away_team, date, neutral=True):

        features = build_match_features(
            home_team,
            away_team,
            pd.Timestamp(date),
            neutral
        )

        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]

        labels = {
            0: "Away Win",
            1: "Draw",
            2: "Home Win"
        }

        result = labels[prediction]

        if result == "Home Win":
            winner = home_team

        elif result == "Away Win":
            winner = away_team

        else:
            # Knockout football cannot end in a draw.
            # Choose the side with the higher win probability.
            if probabilities[2] >= probabilities[0]:
                winner = home_team
            else:
                winner = away_team

        return {
            "home_team": home_team,
            "away_team": away_team,
            "winner": winner,
            "prediction": result,
            "home_probability": probabilities[2],
            "draw_probability": probabilities[1],
            "away_probability": probabilities[0]
        }

    def predict_round(self, matches, date):

        winners = []
        predictions = []

        for home, away in matches:

            result = self.predict_match(
                home,
                away,
                date
            )

            winners.append(result["winner"])
            predictions.append(result)

        return winners, pd.DataFrame(predictions)