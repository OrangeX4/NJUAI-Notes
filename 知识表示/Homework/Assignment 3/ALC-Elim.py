from __future__ import annotations

# ALC-Elim


class Concept:
    '''
    Construct a ALC concept by ¬, ⊓, ⊔, ∃r., ∀r.
    '''

    def __init__(self, type: str, *, constant: str = None, op: str = None, value: str | Concept = None, left: str | Concept = None, right: str | Concept = None):
        '''
        Construct a ALC concept
        type: 'atom', 'unary', 'binary'
        '''
        self.type = type
        if (type == 'atom'):
            self.constant = constant
        elif (type == 'unary'):
            self.op = op
            if (isinstance(value, str)):
                self.value = Concept.atom(value)
            else:
                self.value = value
        elif (type == 'binary'):
            self.op = op
            if (isinstance(left, str)):
                self.left = Concept.atom(left)
            else:
                self.left = left
            if (isinstance(right, str)):
                self.right = Concept.atom(right)
            else:
                self.right = right
        else:
            raise Exception('Unknown concept type')

    def __str__(self):
        if (self.type == 'atom'):
            return self.constant
        elif (self.type == 'unary'):
            return self.op + str(self.value)
        elif (self.type == 'binary'):
            return '(' + str(self.left) + self.op + str(self.right) + ')'

    def NNF(self):
        '''
        lnot(lnot(x)) = x
        lnot(cap(x, y)) = cup(lnot(x), lnot(y))
        lnot(cup(x, y)) = cap(lnot(x), lnot(y))
        lnot(exists(x)) = forall(lnot(x))
        lnot(forall(x)) = exists(lnot(x))
        return NNF of the concept
        '''
        if (self.type == 'atom'):
            return self
        elif (self.type == 'unary'):
            if (self.op == '¬'):
                if (self.value.type == 'atom'):
                    return self
                elif (self.value.type == 'unary' and self.value.op == '¬'):
                    # lnot(lnot(x)) = x
                    return self.value.value
                elif (self.value.type == 'binary' and self.value.op in ['⊓', '⊔']):
                    # lnot(cap(x, y)) = cup(lnot(x), lnot(y))
                    # lnot(cup(x, y)) = cap(lnot(x), lnot(y))
                    return Concept('binary', op='⊔' if self.value.op == '⊓' else '⊓', left=Concept.lnot(self.value.left).NNF(), right=Concept.lnot(self.value.right).NNF())
                elif (self.value.type == 'unary' and self.value.op in ['∃r.', '∀r.']):
                    # lnot(exists(x)) = forall(lnot(x))
                    # lnot(forall(x)) = exists(lnot(x))
                    return Concept('unary', op='∀r.' if self.value.op == '∃r.' else '∃r.', value=Concept.lnot(self.value.value).NNF())
                else:
                    raise Exception('Unknown concept type')
            else:
                return Concept('unary', op = self.op, value = self.value.NNF())
        elif (self.type == 'binary'):
            return Concept('binary', op = self.op, left = self.left.NNF(), right = self.right.NNF())
        else:
            raise Exception('Unknown concept type')

    @staticmethod
    def atom(constant: str):
        return Concept('atom', constant=constant)

    @staticmethod
    def lnot(value: str | Concept):
        '''
        return concept of ¬ form
        '''
        return Concept('unary', op='¬', value=value)

    @staticmethod
    def cap(left: str | Concept, right: str | Concept):
        '''
        return concept of ⊓ form
        '''
        return Concept('binary', op='⊓', left=left, right=right)

    @staticmethod
    def cup(left: str | Concept, right: str | Concept):
        '''
        return concept of ⊔ form
        '''
        return Concept('binary', op='⊔', left=left, right=right)

    @staticmethod
    def exists(value: str | Concept):
        '''
        return concept of ∃r. form
        '''
        return Concept('unary', op='∃r.', value=value)

    @staticmethod
    def forall(value: str | Concept):
        '''
        return concept of ∀r. form
        '''
        return Concept('unary', op='∀r.', value=value)

# unfold the function
lnot, cap, cup, exists, forall = Concept.lnot, Concept.cap, Concept.cup, Concept.exists, Concept.forall
print(lnot(cap(lnot('A'), lnot(lnot('B')))).NNF())
