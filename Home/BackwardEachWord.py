"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.
"""


def backward_string_by_word(text: str) -> str:
    word = ""
    spacer = ""
    new_sentence = []
    last = ""
    for i in text:
        if i.isalnum():
            word += i
            last = "word"
            if spacer.isspace():
                new_sentence.append(spacer)
                spacer = ""
        elif i == " ":
            spacer += i
            last = "space"
            if word.isalnum():
                new_sentence.append(word)
                word = ""
    if last == "word":
        new_sentence.append(word)
    elif last == "space":
        new_sentence.append(spacer)
    print(new_sentence)
    new_new_sentence = []
    for i in new_sentence:
        new_new_sentence.append("".join(list(reversed(i))))
    print("".join(new_new_sentence))
    return "".join(new_new_sentence)


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
