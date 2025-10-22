def pangram(text):
    text = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for ch in alpha:
        if ch not in text:
            print("Not a pangram")
            return
    print("Pangram")

sentence = input("Enter a sentence: ")
pangram(sentence)