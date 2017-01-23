
class opc(object):
    def __init__():
        self.password = [919161, 1859495, 985017, 1377995, 1659485, 1068148, 1599708, 738095, 525756, 1332298, 1274390, 1926028, 1462800, 157737, 1144861, 460670, 411631, 1531994, 1992766, 197800, 349871, 2033064, 852423, 23667, 1211575, 1771461, 1727029, 86621, 805407, 616682, 279968, 675489]
    
    def checkpass(self, mi_cadena):
        from random import shuffle
        from random import randint
        mi_lista = []
        indices_mi_cadena = [x for x in range(len(mi_cadena))]
        shuffle(indices_mi_cadena)
        for indice in indices_mi_cadena:
            indice_xoreado = (indice ^ 19) << 16
            indice_xoreado += (ord(mi_cadena[indice]) ^ 55) << 8
            indice_xoreado += randint(1, 255)
            mi_lista.append(indice_xoreado)
        return mi_lista == self.password
        

