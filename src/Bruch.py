"""
Bruch!

@author: Michael Weinberger
"""
class Bruch:

    """
    Initialisieren eines Bruch-Objekts

    Default-Bruch = 1

    Absicherung Div/0 eingefuegt inkl. Fehler
    Doppelbrueche hinzugefuegt
    Fehlerfall bei falschem Datentyp

    :param zaehler int
    :param nenner int
    """
    def __init__(self, zaehler=1, nenner=1):
        if type(zaehler) is int and type(nenner) is int:

            if nenner != 0:
                self.zaehler = zaehler
                self.nenner = nenner
            else:
                raise ZeroDivisionError('Division durch 0! Die Welt bricht zusammen!')

        elif type(zaehler) is Bruch:

            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner

        else:
            raise TypeError('Falscher Datentyp!')

    """
    Bruch als Integer
    """
    def __int__(self):
        return int(self.zaehler / self.nenner)

    """
    Bruch als Gleitkomma
    """
    def __float__(self):
        return float(self.zaehler / self.nenner)

    """
    Bruch hoch x
    """
    def __pow__(self, hoch):
        if type(hoch) is int:

            return Bruch(self.zaehler ** hoch, self.nenner ** hoch)

        else:
            raise TypeError('Falscher Datentyp!')

    """
    Bruch invertieren
    Kehrwert bilden
    """
    def __invert__(self):
        return Bruch(self.nenner, self.zaehler)

    """
    Absolutwert
    """
    def __abs__(self):
        absz = abs(self.zaehler)
        absn = abs(self.nenner)
        return Bruch(absz, absn)

    """
    Iterator
    """
    def __iter__(self):
        return (self.zaehler, self.nenner).__iter__()

    """
    String mit Repraesentation des Objekts
    """
    def __str__(self):
        return str(self.zaehler) + '/' + str(self.nenner)

    """
    Sind zwei Brueche gleich?
    Vergleich des Gleitkommawerts
    """
    def __eq__(self, other):
        if type(other) is Bruch:

            if self.zaehler / self.nenner == other.zaehler / other.nenner:
                return True

            else:
                return False

        else:
            raise TypeError('Falscher Datentyp!')

    """
    Zwei Brueche ungleich
    Negieren des Outputs von equals
    """
    def __ne__(self, other):
        return not self.__eq__(other)

    """
    Kleiner als
    """
    def __lt__(self, other):
        return self.zaehler * other.nenner < other.zaehler * self.nenner

    """
    Kleiner gleich
    """
    def __le__(self, other):
        return self.zaehler * other.nenner <= other.zaehler * self.nenner

    """
    Groesser als
    """
    def __gt__(self, other):
        return self.zaehler * other.nenner > other.zaehler * self.nenner

    """
    Groesser gleich
    """
    def __ge__(self, other):
        return self.zaehler * other.nenner >= other.zaehler * self.nenner

    """
    'Python calls __radd__ only when the object on the right side of the + is your class instance,
    but the object on the left is not an instance of your class.'
    """
    def __radd__(self, other):
        return float(self) + float(other)

    """
    Bruch addieren
    """
    def __add__(self, other):
        if type(other) is Bruch:
            return Bruch(self.zaehler + other.zaehler, self.nenner)

        elif type(other) is int:
            return Bruch(self.zaehler + other, self.nenner)
        else:
            raise TypeError('Falscher Datentyp!')

    """
    Bruch subtrahieren
    """
    def __sub__(self, other):
        if type(other) is Bruch:
            return Bruch(self.zaehler - other.zaehler, self.nenner)

        elif type(other) is int:
            return Bruch(self.zaehler - other, self.nenner)

        else:
            raise TypeError('Falscher Datentyp!')

    """
    Bruch multiplizieren
    """
    def __mul__(self, other):
        if type(other) is Bruch:
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

        elif type(other) is int:
            return Bruch(self.zaehler * other, self.nenner)

        else:
            raise TypeError('Falscher Datentyp!')

    """
    Ueberschreibt +=
    """
    def __iadd__(self, other):
            return self.__add__(other)

    """
    Ueberschreibt -=
    """
    def __isub__(self, other):
        return self.__sub__(other)

    """
    Alternative Methode zur Multiplikation
    """
    def __rmul__(self, other):
        return float(self) * float(other)

    """
    Ueberschreibt *=
    """
    def __imul__(self, other):
        return self * other

    """
    Ueberschreibt /=
    """
    def __itruediv__(self, other):
        return self / other

    """
    Alternative Methode zum Subtrahieren
    """
    def __rsub__(self, other):
        return Bruch(self.nenner, other * self.nenner - self.zaehler)

    """
    Alternative Gleitkommadivison
    """
    def __rtruediv__(self, other):
        if type(other) is int:
            z2 = other * self.nenner

            if self.zaehler == 0:
                raise ZeroDivisionError('Division durch 0! Die Welt bricht zusammen!')

        else:
            raise TypeError('Falscher Datentyp!')

        return Bruch(z2, self.zaehler)

    """
    Gleitkommadivision
    """
    def __truediv__(self,zaehler):
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler

            if z2 == 0:
                raise ZeroDivisionError('Division durch 0! Die Welt bricht zusammen!')

        elif type(zaehler) is int:
            z2, n2 = zaehler, 1

            if z2 == 0:
                raise ZeroDivisionError('Division durch 0! Die Welt bricht zusammen!')

        else:
            raise TypeError('Falscher Datentyp!')

        return self.__mul__(Bruch(n2, z2))