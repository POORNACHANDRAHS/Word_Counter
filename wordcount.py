def count_words(text):
    """
    Function to count the number of words in a given text.
    
    Parameters:
    text (str): The input text provided by the user.
    
    Returns:
    int: The number of words in the input text.
    """
    # Split the text by whitespace to get individual words
    words = text.split()
    # Return the number of words
    return len(words)

def main():
    """
    Main function to handle user input and output the word count.
    """
    print("Welcome to the Word Counter program!")
    
    # Prompt the user to enter a sentence or paragraph
    text = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling: Check if the input is empty
    if not text:
        print("Error: You entered an empty string. Please provide valid text.")
        return
    
    # Count the number of words in the input text
    word_count = count_words(text)
    
    # Output the word count to the console
    print(f"The number of words in the given text is: {word_count}")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
