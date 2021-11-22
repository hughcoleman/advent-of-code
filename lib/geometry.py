import itertools

class Point:
    """ Represents a single point, in any dimension. """

    def __init__(self, *args):
        # this allows for a more flexible argument format to the constructor,
        # parsing both Point(1, 2, 3) and Point((1, 2, 3))
        coordinates = args[0]
        if len(args) > 1:
            coordinates = tuple(args)

        # ...but the implementation above still has an edge-case in the case of
        # a 1-d Point (just use an int!)
        if type(coordinates) is int:
            coordinates = (coordinates,)

        self.coordinates = tuple(coordinates)
        self.dimension = len(coordinates)

    def __str__(self):
        return "Point({})".format(", ".join(str(p) for p in self.coordinates))

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]

    @property
    def z(self):
        return self.coordinates[2]

    def neighbours(self, distance=1):
        deltas = itertools.product([-1, 0, 1], repeat=self.dimension)
        for delta in deltas:
            if 0 < sum(abs(axis) for axis in delta) <= distance:
                yield Point(
                    tuple(c1 + c2 for c1, c2 in zip(self.coordinates, delta))
                )

    def __add__(self, addend):
        """Add two points together (pairing up coordinates by axis) and return
        their sum."""
        augend = self

        if augend.dimension != addend.dimension:
            raise ValueError("points are in different dimensions")

        return Point(
            tuple(
                c1 + c2
                for c1, c2 in zip(augend.coordinates, addend.coordinates)
            )
        )

    def __eq__(self, comparand):
        """ Compare two points and determine equality. """
        comparator = self

        if comparator.dimension != comparand.dimension:
            raise ValueError("points are in different dimensions")

        return all(
            c1 == c2
            for c1, c2 in zip(comparator.coordinates, comparand.coordinates)
        )

    def __hash__(self):
        return hash(self.coordinates)

    @staticmethod
    def distance(p1, p2):
        """ Calculate the floating-point distance between two points. """
        if p1.dimension != p2.dimension:
            raise ValueError("points are in different dimensions")

        return math.sqrt(
            sum(
                pow(c1 - c2, 2)
                for c1, c2 in zip(p1.coordinates, p2.coordinates)
            )
        )

    @staticmethod
    def manhattan(p1, p2):
        """ Calculate the Manhattan distance between two points. """
        if p1.dimension != p2.dimension:
            raise ValueError("points are in different dimensions")

        return sum(
            abs(c1 - c2) for c1, c2 in zip(p1.coordinates, p2.coordinates)
        )

Point.NORTH = Point((1, 0))
Point.SOUTH = Point((-1, 0))
Point.EAST = Point((0, 1))
Point.WEST = Point((0, -1))

Point.UP = Point((1, 0))
Point.DOWN = Point((-1, 0))
Point.LEFT = Point((0, -1))
Point.RIGHT = Point((0, 1))
