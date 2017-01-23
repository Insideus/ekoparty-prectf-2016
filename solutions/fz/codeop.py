class Checker(object):

    def __init__(self):
        self.password = [
            919161, 1859495, 985017, 1377995, 1659485, 1068148, 1599708,
            738095, 525756, 1332298, 1274390, 1926028, 1462800, 157737,
            1144861, 460670, 411631, 1531994, 1992766, 197800, 349871,
            2033064, 852423, 23667, 1211575, 1771461, 1727029, 86621, 805407,
            616682, 279968, 675489
        ]

    def checkpass(self, password):
        from random import shuffle
        from random import randint

        result = []
        indices = [i for i in range(len(password))]
        shuffle(indices)

        for i in indices:
            letter = (i ^ 19) << 16
            letter += (ord(password[i]) ^ 55) << 8
            letter += randint(1, 255)
            result.append(letter)

        return self.password == result

    def bruteforce(self):
        import string
        answer = ["?"] * len(self.password)
        for right in self.password:
            for idx in xrange(len(self.password)):
                for letter_ord in xrange(255):
                    for i in xrange(1, 255):
                        n = (idx ^ 19) << 16
                        n += (letter_ord ^ 55) << 8
                        n += i
                        if n == right:
                            answer[idx] = chr(letter_ord)

        return "".join(answer)

if __name__ == "__main__":
    checker = Checker()
    print "Key is", checker.bruteforce()
