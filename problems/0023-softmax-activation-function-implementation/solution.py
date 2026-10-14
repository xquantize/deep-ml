import math

def softmax(scores: list[float]) -> list[float]:
    if not scores:
        return []
    
    max_score = max(scores)
    exp_scores = [math.exp(score - max_score) for score in scores]
    sum_exp = sum(exp_scores)
    
    return [score / sum_exp for score in exp_scores]
