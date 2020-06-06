from madlib_clin import __version__
from madlib_clin.mad_lib import game_instructions
from madlib_clin.mad_lib import pull_template
from madlib_clin.mad_lib import pull_keys
def test_version():
    assert __version__ == '0.1.0'
def test_game_instructions_test():
    actual = game_instructions()
    expected = """***Welcome to mad libs***
      ***********************************
      ***********************************
      **********************************"""
    assert actual == expected
def test_game_pull_keys_test():
  with open("madlib_clin/template.txt") as template:
    actual = pull_template()
    expected = """Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.
"""
    assert actual == expected
def test_pull_keys():
    actual = pull_keys()
    expected = ['Adjective', 'Adjective', 'A First Name', 'Past Tense Verb', 'A First Name', 'Adjective', 'Adjective', 'Plural Noun', 'Large Animal', 'Small Animal', "A Girl's Name", 'Adjective', 'Plural Noun', 'Adjective', 'Plural Noun', 'Number 1-50', "First Name's", 'Number', 'Plural Noun', 'Number', 'Plural Noun']
    assert actual == expected