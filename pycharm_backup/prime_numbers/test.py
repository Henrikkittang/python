
# En = -B/n^2
# B = 2.18 * 10^-18

# E = h*f ------ f = E/h
# h = 6.62 * 10^-34
# c = lambda * f ----- lambda = c/f


B = 2.18 * 10**(-18)
h = 6.63 * 10**(-34)
c = 3 * 10**8


def E_(n):
    return (-1) * (B/(n**2))


def delta_E(E_n, E_m):
    return E_n - E_m


def frequency(E):
    return E/h


def wavelength(f):
    return c/f


cont = "y"
while cont == "y":
    start = int(input("start: "))
    end = int(input("end: "))

    E_dif = delta_E(E_(start), E_(end))
    freq = frequency(E_dif)
    wavelen = wavelength(freq)

    E_dif *= 10**18
    freq *= 10**(-15)
    wavelen *= 10**9

    print(round(E_dif, 3), " aJ")
    print(round(freq, 3), " PHz")
    print(round(wavelen, 3), " nm")


    print()
    cont = input("Again? ")
    
