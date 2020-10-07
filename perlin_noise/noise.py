import random

random_seed = []
for i in range(16):
    random_seed.append(random.randint(0, 100) / 100)

def perlin_noise(count, seeds):
    arr = []
    scaling_factor = 1
    pitch = 16
    total = 0
    factor_total = 0
    for i in range(count):
        noise = 0
        factor_total += scaling_factor
        for j in range(0, 16+1, pitch):
            x =  j % 16
            noise += seeds[x] * scaling_factor

        scaling_factor /= 2
        pitch = int( pitch // 2 )
        total += noise
    return total / factor_total

ye = perlin_noise(3, random_seed)
print(ye)



