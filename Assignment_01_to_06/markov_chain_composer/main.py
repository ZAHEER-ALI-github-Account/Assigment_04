import random
import re

class MarkovChain:
    def __init__(self, order=2):
        self.order = order
        self.model = {}

    def _get_ngram(self, text):
        """Create a list of n-grams from the text."""
        words = re.findall(r'\w+', text.lower())
        ngrams = zip(*[words[i:] for i in range(self.order)])
        return [' '.join(ngram) for ngram in ngrams]

    def build_model(self, text):
        """Build a Markov Chain model from the provided text."""
        ngrams = self._get_ngram(text)
        for ngram in ngrams:
            words = ngram.split()
            context = ' '.join(words[:-1])  # Context: all words except the last one
            next_word = words[-1]  # The word after the context

            if context not in self.model:
                self.model[context] = []
            self.model[context].append(next_word)

    def generate_text(self, length=50, seed=None):
        """Generate text based on the Markov Chain model."""
        if not seed:
            seed = random.choice(list(self.model.keys()))  # Choose a random starting point
        output = seed.split()  # Start with the seed

        print(f"Starting with seed: {seed}")  # Debugging the seed

        for _ in range(length):
            context = ' '.join(output[-self.order:])  # Get the last `order` words as the context
            if context not in self.model:
                print("Context not found in model:", context)  # Debugging missing context
                break  # Exit if no valid context is found
            next_word = random.choice(self.model[context])  # Choose a next word from the possible options
            output.append(next_word)

        return ' '.join(output)

def main():
    text = """
    I don't know what you heard about me
    But a bitch can't get a dollar out of me
    No Cadillac, no perms you can't see
    Then I'm a motherfucking P-I-M-P
    I don't know what you heard about me
    But a bitch can't get a dollar out of me
    No Cadillac, no perms you can't see
    Then I'm a motherfucking P-I-M-P
    """
    
    # Create and train the model
    markov = MarkovChain(order=2)
    markov.build_model(text)

    # Try a different seed phrase to see what gets generated
    seed_phrase = "I don't know"
    
    # Generate text
    generated_text = markov.generate_text(length=50, seed=seed_phrase)
    print("\nGenerated Text:\n")
    print(generated_text)

if __name__ == '__main__':
    main()
