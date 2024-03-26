import pytest
from unittest.mock import patch
from src.just4fun import fun  # Update the import path according to your project structure


with patch('builtins.input', return_value='exit'):
    from src.just4fun import fun

# For 8 Ball Functions
    
def test_response_for_valid_input():
    # Magic_8_ball returns a known response for valid inputs.
    valid_responses = [
        "It is certain.", "As I see it, yes.", "Reply hazy, try again.", "Don't count on it.",
        "It is decidedly so.", "Most likely.", "Ask again later.", "My reply is no.",
        "Yes, definitely.", "Outlook good.", "Better not tell you now.", "Outlook not so good.",
        "Without a doubt.", "Yes.", "Very doubtful.", "The universe says yes.",
        "Yes – in due time.", "Yes, but don't hold your breath.", "You will have to wait.", "I have my doubts.", "The signs suggest no.",
        "The answer lies within yourself.", "Only time will tell.", "The answer is hidden in plain sight."
    ]
    for count in range(1, 5):  # Testing for the first four questions
        response = fun.magic_8_ball(count)
        assert response in valid_responses, f"Response '{response}' was not in the list of known responses."

def test_tired_response():
    # The function returns the "tired" response at 5 questions
    response = fun.magic_8_ball(5) 
    expected_response = "Phew, I'm tired. Let's take a break!"
    assert response == expected_response, f"Expected '{expected_response}', but got '{response}'."

# Tests for Affirmations Function
def test_affirmation_for_happy_mood():
    happy_responses = [
        "Your joy is contagious.",
        "Happiness looks gorgeous on you.",
        "Continue to shine as you always do."
    ]
    response = fun.affirmations("happy")
    assert response in happy_responses, f"Response '{response}' was not in the list of happy affirmations."

def test_affirmation_for_sad_mood():
    sad_responses = [
        "It's okay to feel sad, growth comes from discomfort.",
        "This is temporary; your strength is permanent.",
        "You are more resilient than you realize."
    ]
    response = fun.affirmations("sad")
    assert response in sad_responses, f"Response '{response}' was not in the list of sad affirmations."

def test_affirmation_for_unrecognized_mood():
    response = fun.affirmations("angry")  # Example of an unrecognized mood
    expected_response = "Mood not recognized. Please enter 'happy' or 'sad'."
    assert response == expected_response, f"Expected '{expected_response}', but got '{response}'."