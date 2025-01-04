

def main():
    book_to_read = "books/frankenstein.txt"
    print(f"--- Begin report of {book_to_read} ---\n")
    with open (book_to_read) as book:
        book_contents = book.read()
        word_count(book_contents)
        character_count(book_contents)

def word_count(book):
    words = book.split()
    print(f"{len(words)} word were found in the document\n")

def character_count(book):
    book_lowered = book.lower()
    letter_count = {}
    sorted_count = []
    for c in book_lowered:
        if c.isalpha():
            if c not in letter_count:
                letter_count[c]=1
            letter_count[c] += 1
    for cha in letter_count:
        sorted_count.append({"cha": cha,"count":int(letter_count[cha])})
    def sort_on(dict):
        return dict["count"]
    sorted_count.sort(reverse = True, key = sort_on)
    for count in sorted_count:
        print(f"The '{count["cha"]}' character was found {count["count"]} times")
 

main()