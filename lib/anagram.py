class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, words):
        matches = []

        for candidate in words:
            # Exclude identical words
            if candidate.lower() == self.word.lower():
                continue

            # Check if sorted letters match
            if sorted(candidate) == self.sorted_word:
                matches.append(candidate)

        return matches

