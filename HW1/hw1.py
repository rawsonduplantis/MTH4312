ciphertext='NRUATW YAHJSE DIODII TLWCIJ DIOPRA DPANTO EOOPEG TNCWAS DOBYAP FRALLW HSQNHW DTDPIJ GENDEO BUWCEH LWKQGN LVEEYZ ZEOYOP XAGPIP DEHQOX GIKFSE YTDPOX DENGEZ AHAYOI PNWZNA SAOEOH ZOGQON AAPEEN YSWYDB TNZEHA SIZOEJ ZRZPRX FTPSEN PIOLNE XPKCTW YTZTFB PRAYCA MEPHEA YTDPSA EWKAUN DUEESE YCNJPP LNWWYO TSKYEG YOSDTD LTPSED TDZPNK CDACWW DCKYSP CUYEEZ MYDFMW YIJEEH WICPNY PWDPRA LSPSEK CDACOB YAPFRA LPLLRA YTHJCK XEOQRK XAOZUN NEKFTO TDAZFK FROPLR PSWYDE DMKCEI JSPPRE ZUO'
trimmed_ciphertext = ciphertext.replace(' ','')
print(trimmed_ciphertext)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def partition(letters, n):
    partition=[[], [], [], [], [], []]
    pos = 0
    for letter in letters:
        bucket = pos % n
        #print(f'{letter} of pos. {pos} going into bucket {bucket}')
        partition[bucket].append(letter)
        pos += 1
    return partition

partitioned_cipher = partition(trimmed_ciphertext, 6)

def frequencies(letters):
    letter_frequencies = [0]*26
    for letter in letters:
        letter_frequencies[alphabet.index(letter)] += 1

    return letter_frequencies

def distribution(frequencies):
    total = 0
    percentages = [0] * 26
    for frequency in frequencies:
        total += frequency

    for i in range(26):
        percentages[i] = round((frequencies[i] / total) * 100, 1)

    return percentages

def shift_alphabet(letters, shift):
    shifted_letters = []
    for letter in letters:
        shifted_position = (alphabet.index(letter) + shift) % 26
        #print(f'Shifting {letter} by {shift} to {alphabet[shifted_position]}')
        shifted_letters.append(alphabet[shifted_position])
    return shifted_letters

#for partition in partitioned_cipher:
    #print(alphabet)
    #print(frequencies(partition))
    #print(distribution(frequencies(partition)))

def partition_union(partitions):
    union = []
    for i in range(len(partitions[0])):
        ngram = ''
        for partition in partitions:
            try:
                #print(partition[i])
                ngram += partition[i]
            except:
                True
                #print('???')
        union.append(ngram)
        #print(ngram)
    return union

print(partition_union(partitioned_cipher))
# -11, 0, 4, -11, 0, 4
plaintext = partition_union([shift_alphabet(partitioned_cipher[0], 0), shift_alphabet(partitioned_cipher[1], 0), shift_alphabet(partitioned_cipher[2], 4), shift_alphabet(partitioned_cipher[3], -11), shift_alphabet(partitioned_cipher[4], 0), shift_alphabet(partitioned_cipher[5], 0)])

for i in range(len(plaintext)):
    if i % 7 == 0:
        print('\n')
        print(plaintext[i])
    else:
        print(plaintext[i])


'''
def trigrams(first_set, second_set, third_set):
    trigrams = []
    for i in range(len(first_set)):
        trigram = first_set[i] + second_set[i] + third_set[i]
        trigrams.append(trigram)
    return trigrams
'''
'''
thirdone, thirdtwo, thirdthree = [], [], []
pos = 0
for letter in ciphertext:
    if letter != ' ':
        pos += 1
        print(f'{pos} {letter}')
        match pos % 3:
            case 1: thirdone.append(letter)
            case 2: thirdtwo.append(letter)
            case 0: thirdthree.append(letter)
'''