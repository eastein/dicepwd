class CharacterClass(object):

    def __init__(self, chars, minimum=0):
        """
        Create a character class. Pass in all characters that are valid.

        :param chars: the array of characters
        :param minimum: the number of instances of the character class that must appear in the password
        """
        self.chars = chars
        self.n = len(self.chars)
        self.minimum = minimum

    def pick(self, n):
        if n >= self.n:
            raise RuntimeError("I don't have that many characters.")

        return self.chars[n]
