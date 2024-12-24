rating=input("Enter the ratings separate with comma :")
ratings=list(map(int,rating.split(",")))
def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    percentage= (positive_count / len(ratings)) * 100
    return  f"Positive Feedback: {percentage}%"
print(calculate_positive_feedback_percentage(ratings))