# Based on this challenge
# https://www.reddit.com/r/dailyprogrammer/comments/46zm8m/20160222_challenge_255_easy_playing_with_light/

def light_bulb(num):
    bulb = [0]*num
    return bulb

def change(lista, ini, fim):
    if ini > fim:
        fim, ini = ini, fim

    for i, value in enumerate(lista):
        if i >= ini and i <= fim:
            if value==0:
                lista[i]=1
            if value==1:
                lista[i]=0
    return lista

bulb = light_bulb(10)

change(bulb,3,6)
change(bulb,0,4)
change(bulb,7,3)
change(bulb,9,9)

print "========"
print 'Lights on: {}'.format(sum(bulb))
print "========"
