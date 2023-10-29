import sys
from functools import total_ordering


@total_ordering
class Accommodation:
    name: str
    _city: str
    __price: int

    def __init__(self, name: str, price: int, city: str = "Debrecen"):
        self.name = name
        self.__price = price
        self._city = city

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, value: int) -> None:
        self.__price = value

    @property
    def city(self) -> str:
        return self._city

    def __repr__(self) -> str:
        return f"{self.name}, {self.price}, {self.city}"

    def __str__(self) -> str:
        return f"{self.name} ({self.city}): {self.price} Ft"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Accommodation) and \
            (self.name, self.city, self.price) == \
        (other.name, other.city, other.price)

    def __lt__(self, other):
        if self.city != other.city:
            return self.city < other.city
        if self.price != other.price:
            return self.price < other.price
        return self.name < other.name

    @staticmethod
    def acc_per_city(cities: list, city: str) -> int:
        return len([x for x in cities if x.city == city])


class Hotels(Accommodation):
    _stars: int

    def __init__(self, name: str, city: str, price: int, stars: int):
        super().__init__(name, price, city)
        self._stars = stars

    @property
    def stars(self) -> int:
        return self._stars

    @stars.setter
    def stars(self, value) -> None:
        if 1 <= value <= 5:
            self._stars = value
        else:
            raise ValueError("A csillagok száma 1-től 5-ig terjedhet")

    def __repr__(self) -> str:
        return super().__repr__() + f"{self.stars} *"

    def __str__(self) -> str:
        return super().__str__() + f" {self.stars}"
