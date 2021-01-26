#-- Andrew 13519036 --#

# pengimpor sejati
import time

# permutasi
def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

# mengecek kebenaran Cryptarithm
def isCrypto(angka, mapHuruf, kata, strip, waktu):
    i = 0
    ketemu = False
    while i < len(angka) and not ketemu:
        ruasKiri = 0
        ruasKanan = 0
        listKiri = []
        listKanan = []

        for j in range(len(mapHuruf)):
            mapHuruf[j][1] = int(angka[i][j])

        for j in range(len(kata)-1):
            for k in range(len(kata[j])):
                for l in range(len(mapHuruf)):
                    if mapHuruf[l][0] == kata[j][k]:
                        ruasKiri += mapHuruf[l][1]*(10**k)
                        break
            listKiri.append(ruasKiri)
            ruasKiri = 0

        for k in range(len(kata[len(kata)-1])):
            nolDepan = False
            for l in range(len(mapHuruf)):
                if mapHuruf[l][0] == kata[len(kata)-1][k]:
                    if k != len(kata[len(kata)-1])-1:
                        ruasKanan += mapHuruf[l][1]*(10**k)
                        break
                    else:
                        if mapHuruf[l][1] != 0:
                            ruasKanan += mapHuruf[l][1]*(10**k)
                            break
                        else:
                            nolDepan = True
                            break
            if nolDepan:
                ruasKanan = 0
                break
        listKanan.append(ruasKanan)

        if sum(listKiri) == sum(listKanan):
            print("\n")
            for ii in range(len(listKiri)):
                if ii != len(listKiri)-1:
                    print(str(listKiri[ii]))
                else:
                    print(str(listKiri[ii])+"+")
            print(strip[0])
            print(listKanan[0])

            print("\nWaktu komputasi: "+str(time.time()-waktu)+" detik.")
            print("Total tes yang dilakukan: "+str(i+1)+".")
            ketemu = True
        else:
            i += 1
    return ketemu

# balikkan kata perhuruf
def reverseKata(kata):
    for e in kata:
        e.reverse()
    return

# fungsi utama
def main(filename):
    waktu = time.time()

    angka = perms("0123456789")
    
    f = open("../test/"+filename, "r")

    lines = [line.strip() for line in f]

    for i in lines:
        print(i)

    huruf = []
    kata = []
    strip = []
    for e in lines:
        if e[0] != '-':
            if e[len(e)-1] != '+':
                kata.append(list(e))
            else:
                kata.append(list(e[:len(e)-1]))
        else:
            strip.append(e)
        listlines = list(e)
        for i in listlines:
            if (i not in huruf) and (i != '+') and (i != '-'):
                huruf.append(i)
    
    if len(huruf) > 10:
        print("\nJumlah huruf lebih dari 10.")
        return

    mapHuruf = [[0 for j in range(2)] for i in range(len(huruf))]
    for i in range(len(huruf)):
        mapHuruf[i][0] = huruf[i]

    reverseKata(kata)

    if not isCrypto(angka, mapHuruf, kata, strip, waktu):
        print("\nSolusi tidak ditemukan.")
        print("Waktu komputasi: "+str(time.time()-waktu)+" detik.")
    return

# program utama
print("Input \"#\" untuk keluar.")
filename = input("Silakan masukkan nama file: ")
while filename != "#":
    main(filename)
    filename = input("silakan masukkan nama file: ")
print("Terima kasih telah menggunakan program ini.")
