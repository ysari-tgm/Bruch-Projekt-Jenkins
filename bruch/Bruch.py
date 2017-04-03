from __future__ import division, print_function, unicode_literals


class Bruch(object):
    """
    Die Bruch Klasse

    __version__ = '1.0'

    __author__ = 'Sari Yunus'
    """

    def __init__(self, zaehler=0, nenner=1):
        """
        Dieser Konstruktor dient zum Initialisieren

        :param zaehler:
        :param nenner:
        :raises TypeError: "nicht korrekter Typ",
        :raises ZeroDivisionError: Divison durch 0
        """
        if type(zaehler) is Bruch:
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('Typ ist nicht korrekt:')
        elif type(nenner) is not int:
            raise TypeError('Typ ist nicht korrekt:')
        if nenner == 0:
            raise ZeroDivisionError('Division durch 0!')
        self.zaehler = zaehler
        self.nenner = nenner

    def __iter__(self):
        """
        Klasse wurde iterable gemacht
        """
        return (self.zaehler, self.nenner).__iter__()

    def __neg__(self):
        """
        Bruch Negation

        :return:  ein negierter Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __radd__(self, zaehler):
        """
        Additon:
        Entweder Zahl plus Bruch oder Bruch plus Bruch
        ruft die normale add Funktion auf


        :param zaehler: int oder Bruch
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        return self.__add__(zaehler)


    def __add__(self, zaehler):
        """
        Addition:
        Im Konstruktor wurde bestimmt, dass bei einer ganzzahligen Zahl automatisch eine 1 im Nenner steht.
        Das heißt dann, dass man von einem Bruch ausgehen kann.

        :param zaehler: int oder Bruch
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('nicht korrekte Typen:')
        else:
            b1 = Bruch(zaehler)
        return Bruch(self.nenner*b1.zaehler+self.zaehler*b1.nenner, self.nenner*b1.nenner)

    def __iadd__(self, other):
        """
        Eine Addition mit sich selbst

        :param other: Bruch
        :return: self
        """
        return self.__add__(other)
 
    def __rsub__(self, left):
        """
        Subtraktion:
        Entweder eine Zahl minus Bruch oder Bruch minus Bruch

        :param zaehler: int or Bruch
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        if type(left) == int:
            z2 = left
            nennerNeu = self.nenner
            zaehlerNeu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerNeu, nennerNeu)
        else:
            raise TypeError('nicht korrekte Typen:')


    def __sub__(self, zaehler):
        """
        Subtraktion:
        Im Konstruktor wurde bestimmt, dass bei einer ganzzahligen Zahl automatisch eine 1 im Nenner steht.
        Das heißt dann, dass man von einem Bruch ausgehen kann.

        :param zaehler: int oder Bruch
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('nicht korrekte Typen:')
        else:
            b1 = Bruch(zaehler)
        return Bruch(self.zaehler*b1.nenner-b1.zaehler*self.nenner, self.nenner*b1.nenner)

    def __isub__(self, other):
        """
        Eine Subtraktion mit sich selbst

        :param other: Bruch
        :return: self
        """
        return self.__sub__(other)

    def __rmul__(self, zaehler):
        """
        Multiplikation:
        Eine Zahl oder Bruch mal Bruch

        :param zaehler: int or Bruch
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        return self.__mul__(zaehler)

    
    def __mul__(self, zaehler):
        """
        mul

        :param zaehler: int oder Bruch
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('nicht korrekte Typen:')
        else:
            b1=Bruch(zaehler)
        z2 = b1.zaehler*self.zaehler
        n2 = b1.nenner*self.nenner
        return Bruch(z2, n2)

    def __imul__(self, other):
        """
        Eine Multiplikation mit sich selbst

        :param other: other Bruch
        :return: self
        """
        return self.__mul__(other)

    def __rtruediv__(self, left):
        """
        Divison:
        Eine Zahl oder Bruch

        :param zaehler: int oder Bruch
        :return: Bruch
        :raises TypeError: nicht korrekte Typen
        :raises ZeroDivisionError: Division durch 0
        """
        if type(left) is not Bruch and type(left) is not int:
            raise TypeError('nicht korrekte Typen:')
        elif self.zaehler == 0:
            raise ZeroDivisionError('Division durch 0!')
        else:
            b1 = Bruch(left)
            return Bruch(self.nenner * b1.zaehler, self.zaehler)

    def __truediv__(self, zaehler):
        """
        Division:
        Ganzzahlig oder Bruch

        :param zaehler: Bruch oder int
        :return: Bruch
        :raises TypeError: nicht korrekte Typen
        :raises ZeroDivisionError: Division durch 0
        """
        if type(zaehler) is not Bruch and type(zaehler) is not int:
            raise TypeError('nicht korrekte Typen:')
        b1 = Bruch(zaehler)
        if b1.zaehler == 0:
            raise ZeroDivisionError('Division durch 0!')
        return self.__mul__(Bruch(b1.nenner, b1.zaehler))

    def __pow__(self, exp):
        """
        Bruch

        :param int exp: Exponent
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        if type(exp) is int:
            return Bruch(self.zaehler ** exp, self.nenner ** exp)
        else:
            raise TypeError('nicht korrekte Typen')

    def __invert__(self):
        """
        Den Bruch invertieren

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __str__(self):
        """
        Override String Funktion

        :return str: Ausgabe
        """

        gcd = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler = self.zaehler/gcd
        self.nenner = self.nenner/gcd

        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler

        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)


    def __makeBruch(other):
        """
        Ein Bruch erstellen

        :param other: Bruch oder int
        :return: Bruch
        :raise TypeError: nicht korrekte Typen
        """
        if type(other) is Bruch:
            return other
        elif type(other) is int:
            b1 = Bruch(other, 1)
            return b1
        else:
            raise TypeError('nicht korrekte Typen')

    def __eq__(self, other):
        """
        Equal Funktion

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__()==other.__float__()


    def __ne__(self, other):
        """
        Nicht equal to Funktion

        :param other: anderer Bruch
        :return: boolean
        """
        return not self.__eq__(other)


    def __gt__(self, other):
        """
        Groesser als

        :param other: anderer Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.__float__()> other.__float__()

    def __lt__(self, other):
        """
        Kleiner als Funktion

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__() < other.__float__()


    def __ge__(self, other):
        """
        Groesser gleich Funktion

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__()>= other.__float__()


    def __le__(self, other):
        """
        Kleiner gleich Funktion

        :param other: anderer Bruch
        :return: boolean
        """
        return self.__float__()<= other.__float__()

    def __abs__(self):
        """
        Betrag vom Bruch Funktion

        :return: positiver Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __itruediv__(self, other):
        """
        Division mit sich selbst

        :param other: anderer Bruch
        :return: self
        """
        return self.__truediv__(other)

    def __float__(self):
        """
        Eine Override float() Funktion

        :return: float
        """
        return self.zaehler / self.nenner

    def __int__(self):
        """
        Eine Override int() Funktion

        :return: int
        """
        return int(self.__float__())

    def __complex__(self):
        """
        Eine Override complex() Funktion

        :return: complex
        """
        return complex(self.__float__())

    @classmethod
    def gcd(cls, x, y):
        """
        Euklidscher Algorithmus Funktion

        :param int x: erster Wert
        :param int y: zweiter Wert
        :return: groesster gemeinsamer Teiler
        """
        x, y = abs(x), abs(y)
        while y != 0:
            (x, y) = (y, x % y)
        return x