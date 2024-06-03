ALLOWED_LETTERS = "abcdefghijklmnopqrstuwvxyzæøåäö"

def main():
    gen_report("books/frankenstein.txt")





def count_words(text) -> int:
    return len(text.split(" "))

def count_chars(text):
    res = {}
    for c in text:
        if c not in ALLOWED_LETTERS: continue

        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res;

def gen_report(path):
    with open(path) as f:
        print("\t--- MY REPORT ---")
        file_contents = f.read()
        char_count = count_chars(file_contents.lower())
        sorted_keys = sorted(char_count.keys(), key=lambda k: char_count[k], reverse=True)
        for k in sorted_keys:
            print(f"   The letter '{k}' was found {char_count[k]} time(s)")


if __name__ == "__main__":
    main()
