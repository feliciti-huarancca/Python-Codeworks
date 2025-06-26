

def magic_hat():
    print('🪄  Reaches into his magic hat')
    yield 'A white Rabbit appears!!'
    print('🪄  Reaches into his coin perse')
    yield 'A shiny gold coin drops out'
    print('🪄  Reaches into his mysterios box')
    yield 'A body in half'

hat = magic_hat()
print(next(hat))
print(next(hat))
#print(next(hat))