from nose.tools import *
from ex48 import lexicon
from ex48.parser import *


wordlist = lexicon.scan('now go and bear run north and the south')
wordlist2 = lexicon.scan('the run bear south')
wordlist3 = lexicon.scan('run north, and eat the princess')
wordlist4 = lexicon.scan('down north')
wordlist5 = lexicon.scan('barthelonya barthelomeu, shuperu')
extra = lexicon.scan('now bear go to the north princess. ')


def test_peek():
    result = peek(wordlist)
    result2 = peek(wordlist2)
    result3 = peek(wordlist3)
    result4 = peek(wordlist4)
    result5 = peek(wordlist5)

    assert_equal(result, 'stop')
    assert_equal(result2, 'stop')
    assert_equal(result3, 'verb')
    assert_equal(result4, 'direction')
    assert_equal(result5, 'error')


def test_parse_verb():
    native_result = parse_verb([('stop', 'now'), ('verb', 'run'),('direction', 'down')])
    result = parse_verb(wordlist)
    assert_equal(result, ('verb', 'go'))
    assert_equal(native_result, ('verb', 'run'))


def test_parse_subject():
    native_result = parse_subject([('stop', 'and'), ('verb', 'run'), ('direction', 'north')])
    result = parse_subject(wordlist)
    assert_equal(result, ('noun', 'bear'))
    assert_equal(native_result, ('noun', 'player'))


def test_parse_object():
    parse_verb(wordlist)
    native_result = parse_object([('noun', 'bear'), ('direction', 'down')])
    result = parse_object(wordlist)
    assert_equal(result, ('direction', 'north'))
    assert_equal(native_result, ('noun', 'bear'))


def test_parse_sentence():
    native_result = parse_sentence([('stop', 'now'), ('verb', 'fuck'), ('stop', 'the'),
                    ('noun', 'princess'), ('stop', 'the'), ('noun', 'princess')])

    assert_equal(native_result, 'player fuck princess')

    result = parse_sentence(extra)
    assert_equal(result, 'bear go north')


def test_exceptions():

    assert_raises(ParserError, parse_subject, wordlist4)
    assert_raises(ParserError, parse_verb, wordlist5)
    assert_raises(ParserError, parse_object, wordlist5)
    assert_raises(ParserError, peek, '')
