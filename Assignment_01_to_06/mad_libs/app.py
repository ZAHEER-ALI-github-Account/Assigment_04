def mad_libs():
    # Get user inputs
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    
    # Create the story using f-strings
    story = f"Today, I went to {place} and saw a {adjective} {noun}. "
    story += f"It was so amazing that I decided to {verb}!"
    
    # Print the final story
    print("\nHere is your Mad Libs story:")
    print(story)

# Run the Mad Libs game
if __name__ == "__main__":
    mad_libs()
