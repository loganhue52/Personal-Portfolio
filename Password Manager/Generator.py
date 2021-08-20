from random import randint
import random
class Generator:
    def __init__(self):
        #defining the object
        self.caps = 1
        self.lows = 5
        self.n = 1
        self.s = 1
        self.passRaw = ""
        self.sadd = 0

    def generate(self):
        #basically just took my original generator and converted it to be a class
        #i like it better
        for i in range(self.caps):
            self.passRaw += chr(randint(65,90))
        for i in range(self.lows):
            self.passRaw += chr(randint(97,122))
        for i in range(self.n):
            self.passRaw += chr(randint(48,57))
        while self.s != 0:
            self.sadd = randint(33,64)
            if self.sadd == 33 \
            or self.sadd == 35 \
            or self.sadd == 36 \
            or self.sadd == 37 \
            or self.sadd == 38 \
            or self.sadd == 40 \
            or self.sadd == 41 \
            or self.sadd == 42 \
            or self.sadd == 64:
                self.passRaw += chr(self.sadd)
                self.s -= 1
        self.password = ''.join(random.sample(self.passRaw, len(self.passRaw)))
        return str(self.password)

    # def __str__(self):
    #     return f'Generated password: {self.password}'