
def get_book_words(book_text):
    return len(book_text.split())

def get_book_characters(book_text):
    characters = {}
    lower_case_book_text = book_text.lower()
    for character in lower_case_book_text:
        if character not in characters:
            characters[character] = lower_case_book_text.count(character)

    return characters

def get_dict_report(characters_dict):
    report = []
    for character in characters_dict:
        character_num = {"char": character, "num": characters_dict[character]}
        report.append(character_num)

    return sorted(report, key=lambda x: x["num"], reverse=True)
