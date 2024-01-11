#!/usr/bin/python3
def find_best_score(scores):
    if not scores or len(scores) == 0:
        return None
    return max(scores, key=scores.get)
