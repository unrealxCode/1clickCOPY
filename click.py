import pyperclip

def main():
    with open('text.txt', 'r') as file:
        text_to_copy = file.read().strip()
    pyperclip.copy(text_to_copy)
    print("Text copied to clipboard.")

if __name__ == "__main__":
    main()
