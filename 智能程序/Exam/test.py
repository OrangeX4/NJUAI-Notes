class InfSequence:

    def __init__(self, start, end, step: int = 1):
        self._start = start
        self._end = end
        self._step: int = step
        self._current = start - step

    def __iter__(self):
        return self
    
    def __next__(self):
        self._current += self._step
        if self._step == 0 and self._start == self._end:
            raise StopIteration
        elif self._step == 0 and self._start != self._end:
            return self._current
        elif self._step > 0:
            if self._end == 'inf':
                return self._current
            elif self._end == '-inf':
                raise StopIteration
            elif self._current < self._end:
                return self._current
            else:
                raise StopIteration
        else:
            if self._end == '-inf':
                return self._current
            elif self._current > self._end:
                return self._current
            else:
                raise StopIteration


while True:
    exec(input())