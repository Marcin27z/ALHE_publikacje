#! python3

class Publication:
    def __init__(self, points, share):
        self.points = points
        self.share = share
    
    def ratio(self):
        return self.points/self.share
    
    def __eq__(self, other):
        return self.ratio() == other.ratio()

    def __ne__(self, other):
        return self.ratio() != other.ratio()

    def __lt__(self, other):
        return self.ratio() < other.ratio()
    
    def __le__(self, other):
        return self.ratio() <= other.ratio()
    
    def __gt__(self, other):
        return self.ratio() > other.ratio()

    def __ge__(self, other):
        return self.ratio() >= other.ratio()
