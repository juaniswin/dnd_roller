#4 side die
print ('four side')
from random import *
print (randint(1,4))

#6 side die
print ('six side')
from random import *
print (randint(1,6))

#8 side die
print ('eight side')
from random import *
print (randint(1,8))

#10 side die
print ('ten side')
from random import *
print (randint(1,10))

#12 side die
print ('twelve side')
from random import *
print (randint(1,12))

#20 side die
print ('twenty side')
from random import *
print (randint(1,20))

#10s interval die
print ('tens to hundred')
from random import *
items = [10,20,30,40,50,60,70,80,90,100]
x = sample(items,  1)
print (x[0])
