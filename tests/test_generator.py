import unittest

from buzz import generator

def test_sample_single_word():
    i = ('foo', 'bar', 'foobar')
    word = generator.sample(i)
    assert word in i

def test_sample_multiple_word():
    i = ('foo', 'bar', 'foobar')
    words = generator.sample(i, 2)
    assert len(words) == 2
    assert words[0] in i
    assert words[1] in i
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5


