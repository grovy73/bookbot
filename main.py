def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_count = count_chars(file_contents.lower())
        print(char_count)

def count_words(text) -> int:
    return len(text.split(" "))

def count_chars(text):
    res = {}
    for c in text:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res;

if __name__ == "__main__":
    main()
