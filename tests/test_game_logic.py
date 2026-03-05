from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_inverted_hint_message_bug():
    # Bug: "Too High" returned message "Go HIGHER!" instead of "Go LOWER!"
    # A guess of 60 when secret is 50 is too high — player should go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint, got: {message}"

def test_string_vs_int_comparison_bug():
    # Bug: secret was cast to str on even attempts, causing lexicographic comparison.
    # e.g. str comparison "9" > "40" is True (since "9" > "4"), so check_guess(9, 40)
    # wrongly returned "Too High". With int comparison it must return "Too Low".
    outcome, _ = check_guess(9, 40)
    assert outcome == "Too Low", f"Expected 'Too Low', got: {outcome}"
