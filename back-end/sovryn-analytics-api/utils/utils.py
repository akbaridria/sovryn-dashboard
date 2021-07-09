
from database.database import database


class utils :
    def __init__(self) :
        pass

    def call_the_largest_swap() :
        _d = database()
        _r = _d.get_the_largest_swap()
        return _r