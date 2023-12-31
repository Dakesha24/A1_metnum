# Mendefinisikan fungsi
def f(x):
    return x**2-2*x-8
# Mendifinisikan fungsi derivatif
def g(x):
    return 2*x-2
# Mendefinisikan fungsi metode newtonRaphson
def newtonRaphson(x0,e,N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('dibagi 0 error')
            break
        #loop iterasi
        x1 = x0 - f(x0)/g(x0)
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag==1:
        print('\nakar yang dibutuhkan : %0.8f' % x1)
    else:
        print('\ntidak konvergen')

# convert inputan ke tipe data float
x0 = input('Perkiraan: ')
x0 = float(x0)
e = input('Perkiraan Error: ')
e = float(e)
# convert inputan ke tipe data int
N = input('Jumlah Step: ')
N = int(N)

newtonRaphson(x0,e,N)
