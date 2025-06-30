def scenario_simulation(df, scenario):
    factor = {"best": 1.1, "worst": 0.9}.get(scenario, 1)
    df["Scenario Adjusted"] = df["Planned"] * factor
    return df
