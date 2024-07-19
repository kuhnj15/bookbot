def main():
    path = "books/frankenstein.txt"
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print("complete")
    count = num_words(file_contents)

    # convert file to lower case
    file_contents.lower()

    # create empty letters dict
    letter_dict = create_dict()
    letter_dict = count_letters(letter_dict, file_contents)

    # print(count_letters(letter_dict,file_contents))

    letter_list = []
    for i in letter_dict:
        letter_list.append({"letter": i, "count": letter_dict[i]})

    letter_list.sort(reverse=True, key=sort_on)
    # print(letter_list)

    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document\n\n")
    
    # print(letter_list)

    for l in letter_list:
        print(f"The '{l['letter']}' character was found {l['count']} times")

    print("--- End report ---")
    

def num_words(text):
    words = text.split()
    count = len(words)
    return count

def create_dict():
    letter_dict = {}
    for i in range(97,123):
        c = chr(i)
        letter_dict[c] = 0
    return letter_dict

def count_letters(dict, text):
    for c in text:
        if c in dict:
            dict[c] += 1
    return dict

def sort_on(dict):
    return dict["count"]

    



main()
