import random

class MarkovChain:
    def __init__(self):
        self.data = {}

    def add_text(self, text):
        words = text.split()
        for i in range(len(words) - 2):
            pair = (words[i], words[i + 1])
            follower = words[i + 2]
            if pair in self.data:
                self.data[pair].append(follower)
            else:
                self.data[pair] = [follower]

    def generate_text(self, length=20):
        word1, word2 = random.choice(list(self.data.keys()))
        result = [word1, word2]
        for i in range(length):
            pair = (word1, word2)
            if pair in self.data:
                followers = self.data[pair]
                next_word = random.choice(followers)
                result.append(next_word)
                word1, word2 = word2, next_word
            else:
                break
        return " ".join(result)

def generate_random_poem(poems):
    markov = MarkovChain()
    for poem in poems:
        markov.add_text(poem)
    return markov.generate_text()

if __name__ == '__main__':
    poems = ["This is the first line of my poem.\nThis is the second line of my poem
