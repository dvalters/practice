from palindrome import is_palindrome

def test_yes_palindrome():
    # Set up
    input = "radar"
    # Act 
    result = is_palindrome(input)
    # Assert
    assert result is True


def test_no_palindrome():
    # Set up
    input = "palindrome"
    # Act
    result = is_palindrome(input)
    # Assert
    assert result is False