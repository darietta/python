from person.person import Person
from product.product import Product
from transport.transport import Transport

def _test():
    import doctest 
    doctest.testmod()

if __name__ == "__main__":
    _test()