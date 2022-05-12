from __future__ import annotations
from functools import reduce
from itertools import chain, combinations
from typing import Iterable


def powerset(iter: Iterable, contain_empty: bool = False) -> Iterable:
    '''
    calculate powerset
    '''
    s = list(iter)
    if contain_empty:
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    else:
        return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

# ALC-Elim
# It only support unique role name 'r' and '∃r.', '∀r.'


class Concept:
    '''
    Construct a ALC concept by ¬, ⊓, ⊔, ∃r., ∀r., ⊤, ⊥
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

    def __repr__(self):
        return str(self)

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
                return Concept('unary', op=self.op, value=self.value.NNF())
        elif (self.type == 'binary'):
            return Concept('binary', op=self.op, left=self.left.NNF(), right=self.right.NNF())
        else:
            raise Exception('Unknown concept type')

    def __eq__(self, other):
        if (self.type != other.type):
            return False
        if (self.type == 'atom'):
            return self.constant == other.constant
        elif (self.type == 'unary'):
            return self.op == other.op and self.value == other.value
        elif (self.type == 'binary'):
            return self.op == other.op and self.left == other.left and self.right == other.right
        else:
            raise Exception('Unknown concept type')

    def __hash__(self):
        return hash(str(self))

    def subconcepts(self) -> set[Concept]:
        '''
        return all subconcepts of the concept
        '''
        if (self.type == 'atom'):
            return {self}
        elif (self.type == 'unary'):
            return {self} | self.value.subconcepts()
        elif (self.type == 'binary'):
            return {self} | self.left.subconcepts() | self.right.subconcepts()
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

    @staticmethod
    def imply(left: str | Concept, right: str | Concept):
        '''
        return concept of cup(lnot(left), right) form
        '''
        return Concept.cup(Concept.lnot(left), right)


class ALC_Elim:
    '''
    ALC-Elim
    '''

    def __init__(self, A0: str | Concept, TBox: list[Concept]):
        '''
        1. Combine TBox with form reduce(lambda x, y: Concept.cap(x, y), TBox of form of "cup(lnot(C), D)").NNF()
        2. Calculate subconcepts sub and all types of TBox to Gamma[0]
        '''
        if (isinstance(A0, str)):
            self.A0 = Concept.atom(A0)
        else:
            self.A0 = A0
        self.TBox = TBox
        self.CT = reduce(lambda x, y: Concept.cap(x, y), TBox).NNF()
        self.sub = self.CT.subconcepts()
        self.Gamma = [[]]
        for tau in powerset(self.sub):
            tau = set(tau)
            if self.is_type(tau):
                self.Gamma[0].append(tau)
        i = 0
        while i == 0 or len(self.Gamma[i]) != len(self.Gamma[i - 1]):
            i = i + 1
            self.Gamma.append([tau for tau in self.Gamma[i - 1] if not self.is_bad(tau, self.Gamma[i - 1])])
        self.i = i
        self.tau = None
        for tau in self.Gamma[i]:
            if self.A0 in tau:
                self.tau = tau

    def __str__(self) -> str:
        s = ''
        for i in range(len(self.Gamma)):
            s += 'Gamma[' + str(i) + '] = ' + str(self.Gamma[i]) + '\n'
        return s

    def __repr__(self) -> str:
        return str(self)

    def is_type(self, tau: set[Concept]) -> bool:
        '''
        return True if tau is type of CT
        '''
        # (iv)
        if (self.CT not in tau):
            return False
        # (i)
        for A in tau:
            lnot_A = Concept.lnot(A).NNF()
            if lnot_A in tau and lnot_A in self.sub:
                return False
        # (ii)
        for A in tau:
            if A.type == 'binary' and A.op == '⊓' and (A.left not in tau or A.right not in tau):
                return False
        # (iii)
        for A in tau:
            if A.type == 'binary' and A.op == '⊔' and A.left not in tau and A.right not in tau:
                return False
        return True

    def is_bad(self, tau: set[Concept], Gamma: list[set[Concept]]) -> bool:
        '''
        return True if tau is bad type of CT
        '''
        for A in tau:
            if A.type == 'unary' and A.op == '∃r.':
                S = {A.value} | set(
                    (C.value for C in tau if C.type == 'unary' and C.op == '∀r.'))
                is_bad = True
                for _type in Gamma:
                    if (S <= _type):
                        is_bad = False
                        break
                if is_bad:
                    return True
        return False


# unfold the function
lnot, cap, cup, exists, forall, imply = Concept.lnot, Concept.cap, Concept.cup, Concept.exists, Concept.forall, Concept.imply
# result = ALC_Elim('B', [imply('B', exists('B')), imply('⊤', 'B'), imply(forall('B'), exists('B'))])
# result = ALC_Elim('B', [imply('B', exists('B')), 'B', imply(forall('B'), exists('B'))])
# result = ALC_Elim('C', [imply('C', forall(forall(lnot('B')))), imply(lnot('A'), 'B'), imply('A', lnot('B')), imply('⊤', lnot(forall('A')))])
result = ALC_Elim('C', [imply('C', forall(forall(lnot('B')))), imply(lnot('A'), 'B'), imply('A', lnot('B')), lnot(forall('A'))])
print('$C_{\mathcal{T}}$ = ' + str(result.CT))
print('$\operatorname{sub}(\mathcal{T})$ = ' + str(result.sub))
print('$i$ = ' + str(len(result.Gamma) - 1))
print('There is ' + str(len(result.Gamma[0])) + ' types in $\Gamma_0$')
for i in range(len(result.Gamma)):
    print(f'$\Gamma_{i}$ = ' + str(result.Gamma[i]))
print('$\\tau$ = ' + str(result.tau))