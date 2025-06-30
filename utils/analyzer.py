from agents.standard import standard_features as standard
from agents.plus import plus_features as plus
from agents.premium import premium_features as premium

def analyze_excel(df, agent_type: str):
    if agent_type == "standard":
        return standard.calculate_variance(df)
    elif agent_type == "plus":
        return plus.generate_burn_curve(df)
    elif agent_type == "premium":
        return premium.scenario_simulation(df, "best")
    else:
        raise ValueError("Unknown agent type")
