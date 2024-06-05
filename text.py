def kalimat(text):

    kalimat = 0
    for char in text:
        if char.isupper():
            kalimat += 1
    return kalimat
