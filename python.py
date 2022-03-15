#return a list of random words, each word must have at least one vowel and one consonant in random order
def random_words_vowel_consonant(n):
    import random
    words = []
    for i in range(int(n)):
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        word = []
        for i in range(random.randint(1,6)):
            word.append(random.choice(vowels))
        for i in range(random.randint(1,6)):
            word.append(random.choice(consonants))
        random.shuffle(word)
        words.append(''.join(word))
    return words
#make a random sentence generator
def random_sentence(n):
    import random
    words = random_words_vowel_consonant(n)
    sentence = ' '.join(words)
    sentence = sentence[0].upper() + sentence[1:] + '.'
    return sentence
import string
import tkinter as tk
from tkinter import ttk
#put the above functions into a tkinter window
def ensure(entry):
    #if there is no input make the output 1 otherwise make the output the input
    output = 0
    if len(entry) == 0:
        output="1"
    elif int(entry) > 1000:
        output = "1000"
    else:
        output=(entry)
    return output
def main():
    getout=str('')
    root = tk.Tk()
    root.title("Random Sentence Generator")
    root.geometry("300x300")
    root.resizable(False, False)
    label = ttk.Label(root, text="How many words?")
    label.pack()
    entry = ttk.Entry(root)
    entry.pack()
    #a button that generates a random sentence and displays it in the tkinter window
    def generate():
        getout=str(random_sentence(ensure(entry.get())))
        text.delete("1.0", tk.END)
        text.insert(tk.END, getout)
    button = ttk.Button(root, text="Generate", command=generate)
    button.pack()
    #a text box with text saying "hello world" in it
    text = tk.Text(root, height=12, width=30)
    #text.insert(tk.END, generate)
    text.pack()
    root.mainloop()
main()