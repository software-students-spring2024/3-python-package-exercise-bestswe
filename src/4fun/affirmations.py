import random

def affirmations(mood):
    affirmation_dict = {
        "happy": [
            "Your joy is contagious.",
            "Happiness looks gorgeous on you.",
            "Continue to shine as you always do."
        ],
        "sad": [
            "It's okay to feel sad, growth comes from discomfort.",
            "This is temporary; your strength is permanent.",
            "You are more resilient than you realize."
        ]
    }
    
    if mood in affirmation_dict:
        return random.choice(affirmation_dict[mood])
    else:
        return "Mood not recognized. Please enter 'happy' or 'sad'."

# Example usage:
print(affirmations("happy"))
print(affirmations("sad"))
