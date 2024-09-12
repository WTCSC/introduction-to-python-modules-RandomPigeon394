def count_chars(text):
    """
    Count the number of characters in a text
    """
    return(len(text))

def count_words(text):
    """
    Count the number of words in a text
    """
    return len(text.split())
def count_sentences(text):
    """
    Count the number of sentences in a text
    """
    return text.count(".") + text.count("?") + text.count("!")