from lettuce import step
from lettuce import world
from fizzbuzz import fizz_buzz


@step('the number (\d+)')
def the_number(step, num):
    world.number = int(num)


@step('I call fizzbuzz')
def call_fizzbuzz(step):
    world.fb = fizz_buzz(world.number)


@step('I see the output (\w+)')
def compare(step, expected):
    assert world.fb == expected, "Got %s" % expected
