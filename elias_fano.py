import hashlib
import math

def elias_fano(file): #το file ειναι ηδη ταξινομημενο#
    size = len(file)
    max = file[size - 1]
    first_bits = []
    l_bits = math.log2(max/size) # to l = lg(m/n)
    bitfile = bytearray(len(file)) 
    for i in range(0,len(file - 1)):
        bitfile[i] = file[i] #Βαζω τις τιμες του file σε bytearray
    l_list = bytearray(math.ceil(size*math.log2(max/size))) #arxikopoiw thn lista L
    u_list = bytearray(math.ceil(size + (max/2**math.log2(max/size)))) #στον U αρχικοποιούνται όλα με 0 αρα μένει να βάλω τα 1 
    lbgetter = 0b00000001  #Παιρνει το τελευταιο bit
    for i in range(0,len(bitfile)): #για καθε ενα απο τα στοιχεια που θελουμε να αποθηκευσουμε
        bit_value = bitfile[i] #Χρησιμοποιω μεταβλητη για να μην το χαλασω 
        for k in range(0,math.ceil((math.log2(max/size)))): #για καθε ενα απο τα τελευταια log2(max/size) bits
            last_bit = bit_value & lbgetter 
            l_list[i+k] = last_bit
            bit_value = bit_value >> 1  
        first_bits[i] = bit_value #οτι μενει απο το κοψιμο των τελευταιων bits είναι αυτο που αποθηκευεται στον U, το σωζουμε
    for i in range(0,len(first_bits)):
        u_list[i + first_bits[i]] = 0b1 #αυτο τωρα φτιάχνει τον U ετσι ωστε να μπαινουν τα 1 στις σωστες θέσεις i+k
    m = hashlib.sha256()
    m.update(l_list)
    m.update(u_list)
    digest = m.hexdigest()
    print(l_bits)
    print(l_list)
    print(u_list)
    print(digest)