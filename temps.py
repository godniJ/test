

# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals



import random

import sys



n = 1

iter_factor = 100000

if len(sys.argv) > 1:

    n = int(sys.argv[1])

n=random.randint(5, 30)

if n > 10000:

    print('\nLol !\n')

elif n > 50:

    print('\nGet a coffee, wait and enjoy ! :)\n')

elif n > 30:

    print('\nCheck your email :)\n')



print('\nParam: {n} / Iteration {iter}\n'.format(n=n, iter=iter_factor * n))



t = 0

for i in range(0, iter_factor * n):

    t = t + random.choice([-1, 1]) * random.randint(random.randint(-15, -5), random.randint(5, 15))



print(':)')


