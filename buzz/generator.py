from __future__ import print_function
import random

buzz = ('continous testing', 'continous intergration', 'continous deployment', ' continous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly','seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')


def sample(i, n=1):
    result = random.sample(i, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase =  ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs), sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == '__main__':
    print(generate_buzz())