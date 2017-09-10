class InsufficientEntropyError(Exception):

    """
    Used when the EntropyPool has insufficient entropy to supply the amount of random data requested.
    """


class EntropyDrop(object):

    def __init__(self, n, max_n):
        """
        Creates a drop of entropy to be placed into an entropy pool. Data is given as an integer, n >= 0 and < max_n.

        :param n: the entropy data. The instantiator of EntropyDrop asserts that n is uniformly distributed.
        :param max_n: integer 1 larger than the largest possible value n could be
        """
        self.n = n
        self.max_n = max_n


class EntropyPool(object):

    def __init__(self, entropy_source=None):
        """
        Create a new entropy pool.

        :param entropy_source: if set, should be a callable that when called returns an EntropyDrop object. If this
            is supplied, it will be called as many times as required when entropy if required for a pool operation
            but insufficient entropy is available.
        """
        self.n = 0
        self.max_n = 1
        self.entropy_source = entropy_source

    def fill(self, entropy_drop):
        """
        Adds the entropy from entropy_drop into the entropy pool.

        :param entropy_drop: the EntropyDrop instance
        :return: None
        """
        self.max_n *= entropy_drop.max_n
        self.n *= entropy_drop.max_n
        self.n += entropy_drop.n

    def pour(self, max_n):
        """
        Use data from the entropy pool to get a random integer between 0 and max_n-1, inclusive
        :param max_n:
        :return: a random integer between 0 and max_n-1, inclusive
        """
        self.ensure_entropy_sufficient(max_n)

        r = self.n % max_n
        self.n //= max_n
        self.max_n //= max_n
        return r

    def ensure_entropy_sufficient(self, max_n):
        if max_n <= self.max_n:
            return

        if self.entropy_source is None:
            raise InsufficientEntropyError("Requested max_n is larger than available entropy stored.")
        else:
            while max_n > self.max_n:
                self.fill(self.entropy_source())
