
class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def matches(self, player):
        return self._matcher.matches(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class All:
    def __init__(self):
        self.retrn = True
    
    def matches(self, player):
        return self.retrn

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False


class QueryBuilder:
    def __init__(self, stack=All()):
        self.stack_object = stack

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self.stack_object))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.stack_object))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.stack_object))

    def oneOf(self, *matchers):
        return QueryBuilder(And(Or(*matchers), self.stack_object))

    def build(self):
        return self.stack_object