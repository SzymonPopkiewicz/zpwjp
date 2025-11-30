import pandas as pd
import warnings
def summary_stats(df):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        df = df.sort_values("Date")

        if df.empty:
            return pd.DataFrame(
                [
                    ("Mean return", None),
                    ("Volatility", None),
                    ("Min price", None),
                    ("Max price", None),
                    ("Full return", None)
                ],
                columns=["Metric", "Value"]
            )

        # Calculate full return safely
        first = df["Close"].iloc[0]
        last = df["Close"].iloc[-1]
        full_return = (last / first) - 1

        stats = {
            "Mean return": float(df["Return"].mean()),
            "Volatility": float(df["Return"].std()),
            "Min price": float(df["Close"].min()),
            "Max price": float(df["Close"].max()),
            "Full return": float(full_return)
        }

        return pd.DataFrame(
            [(k, v) for k, v in stats.items()],
            columns=["Metric", "Value"]
        )