import random

def generate_sentence():
    article = random.choice(["The", "A"])
    adjective = random.choice(["red", "big", "happy", "strange"])
    noun = random.choice(["cat", "dog", "banana", "tree"])
    verb = random.choice(["jumped", "ate", "ran", "slept"])
    adverb = random.choice(["quickly", "loudly", "happily", "silently"])
    
    sentence = f"{article} {adjective} {noun} {verb} {adverb}."
    return sentence

if __name__ == "__main__":
    sentence = generate_sentence()
    print(sentence)