#! python3

class Publication:
    def __init__(self, id, points, share, is_monograph):
        self.id = id
        self.points = points
        self.share = share
        self.ratio = points / share
        self.is_monograph = is_monograph

    def __eq__(self, other):
        return self.ratio == other.ratio

    def __ne__(self, other):
        return self.ratio != other.ratio

    def __lt__(self, other):
        return self.ratio < other.ratio

    def __le__(self, other):
        return self.ratio <= other.ratio

    def __gt__(self, other):
        return self.ratio > other.ratio

    def __ge__(self, other):
        return self.ratio >= other.ratio
