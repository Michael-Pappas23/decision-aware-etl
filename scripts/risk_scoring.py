def calculate_decision_risk(missing_values, negative_inventory_count):

    score = 100

    score -= missing_values * 10
    score -= negative_inventory_count * 20

    if score < 0:
        score = 0

    return score