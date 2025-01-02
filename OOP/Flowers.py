class Flower:
    def __init__ (self, name = 'Lavender', petals = 1, price = 1000):
        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, jina):
        self._name = jina

    def set_petals(self, number):
        self._petals = number

    def set_price(self, bei):
        self._price = bei

    def get_name(self):
        print(self._name)
        return self._name
    
    def get_petals(self):
        print(self._petals)
        return self._petals
    
    def get_price(self):
        print(self._price)
        return self._price
    
if __name__ == '__main__':

    first_flower = Flower()
    first_flower.set_name("Rosemary")
    first_flower.set_petals(10)
    first_flower.set_price(2000)
    first_flower.get_name()
    first_flower.get_petals()
    first_flower.get_price()