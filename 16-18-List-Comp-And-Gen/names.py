import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# title case names "Brad Pitt" --> "brad pitt"
print('The title case of the names:')
print([name.title() for name in NAMES])
print()

# reverse first and last name
print('Revered first and last names')
print([name.split()[-1] + ' ' + name.split()[0] for name in NAMES])
print()

def gen_pairs(names=NAMES):
    while True:
        firsts = [name.split()[0].title() for name in names]
        p1 = firsts.pop(random.randint(0, len(firsts)-1))
        p2 = random.choice(firsts)
        yield '{} teams up with {}'.format(p1, p2)


pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))
