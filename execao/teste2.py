try:
    f = open('execao/letras.txt', 'r')
    f.write('lorum ipsum')
    f.close()
except:
    print('algo nao deu certo')