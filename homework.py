
import faker

from math import pi

radii = [*range(0, 20, 2)]

rad_to_space = list(map(lambda x: pi * pow(x, 2), radii))


fake = faker.Faker()

cards = [fake.credit_card_number() for _ in range(100)]

cards.sort(key=lambda x: str(x)[-4:])


word = list(input('Type in word(english one): '))

def ording(lst:list) -> list:
    for i in range(len(lst)):
        lst[i] = ord(lst[i].lower()) - 96

ording(word)

suits = ['\u2660', '\u2665', '\u2666', '\u2663']

values = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [(x,y) for x in suits for y in values]

def fix(objectt:str, instruction) -> str:
    return instruction(objectt)

def замена_лампочки(a):
    return 'заменена лампочка'

def склейка_вазы(a):
    return 'склеена' + a

def починка_замка(a):
    return 'cмазн замок'

def мировая(a):
    return a + 'помирились'
    
deck.sort(key=lambda x:x[1])

deck.sort(key=lambda x:x[0])
