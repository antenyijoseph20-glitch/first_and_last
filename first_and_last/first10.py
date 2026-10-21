def manual_palindrome(text):
    text = text.replace(" ", "").lower()

    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return text == reversed_text
