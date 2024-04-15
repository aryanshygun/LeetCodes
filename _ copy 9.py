
def randomcolor():
    import random
    
    rgba_seq = []
    for i in range(10):
        r_random = float("{:.5f}".format(random.random()))
        g_random = float("{:.5f}".format(random.random()))
        b_random = float("{:.5f}".format(random.random()))
        rgba_seq.append([r_random, g_random, b_random, 1])
    return random.choice(rgba_seq)


print(randomcolor())
print(randomcolor())