'''
>>> dev_null | tuple
()

>>> cat([1, 2, 3], [4, 5, 6]) | list
[1, 2, 3, 4, 5, 6]
>>> [1, 2, 3] | cat | list
[1, 2, 3]

>>> cat([1, 2, 3]) | (-x for x in STDIN) | list
[-1, -2, -3]
>>> cat(x + 1 for x in (1, 2, 3)) | (x * x for x in STDIN) | list
[4, 9, 16]

>>> ['foo', 'bar', 'baz'] | grep('a[rz]') | list
['bar', 'baz']
>>> xrange(-10, 10) | grep(lambda x: x % 7 == 1) | list
[-6, 1, 8]

>>> ['foo', 'bar', 'quux'] | cut[-2:] | list
['oo', 'ar', 'ux']

>>> sum(xrange(100) | select[i] | tuple != (range(100)[i],) for i in xrange(-3, 4))
0
>>> sum(xrange(100) | select[i:j:k] | list != range(100)[i:j:k] for i in xrange(-3, 4) for j in xrange(-3, 4) for k in xrange(-3, 4) if k != 0)
0

>>> sort([4, 2, 1, 3]) | list
[1, 2, 3, 4]
>>> cat(['foo', 'bar', 'qaax']) | sort(key = lambda x: x[1:3]) | list
['qaax', 'bar', 'foo']
>>> print '-'.join(['foo', 'bar', 'quux'] | cat | sort)
bar-foo-quux

>>> cat([1, 2, 3, 3, 2, 1]) | uniq | list
[1, 2, 3, 2, 1]

>>> cat([1, 2, 3, 3, 2, 1]) | zuniq | list
[1, 2, 3]

>>> cat([1, 2, 3, 42]) | wc
4

>>> seq(5) | list
[1, 2, 3, 4, 5]
>>> seq(3.5, 6) | list
[3.5, 4.5, 5.5]
>>> seq(-10, 40, 100) | list
[-10, 30, 70]

>>> echo('punt') | list
['punt']

>>> sum(yes(6) | head(7))
42

>>> ('foo', 'bar', 'quux') | nl | list
[(1, 'foo'), (2, 'bar'), (3, 'quux')]
>>> ('foo', 'bar', 'quux') | nl1 | list
[(1, 'foo'), (2, 'bar'), (3, 'quux')]
>>> ('foo', 'bar', 'quux') | nl0 | list
[(0, 'foo'), (1, 'bar'), (2, 'quux')]

>>> wc(['foo', 'bar', 'quux'])
3
>>> cat(None for x in xrange(0, 7) for y in xrange(0, x) for z in xrange(y, x)) | wc
56

>>> tmp = []
>>> cat(tmp.__iadd__([x]) for x in xrange(5)) | slurp
>>> tmp
[0, 1, 2, 3, 4]
>>> del tmp

>>> xrange(7) | pipeline.split(3) | list
[(0, 1, 2), (3, 4, 5), (6,)]
'''

import itertools
import re
import sys
import types

class BrokenPipe(Exception):

	def __iter__(self):
		return self
	
	def next(self):
		raise self

class _singleton(object):
	def __repr__(self):
		return '%s.%s' % (self.__module__, self.__class__.__name__)

class STDIN(_singleton):

	__slots__ = []

	def __iter__(self):
		return self
	
	def next(self):
		frame = sys._getframe()
		try:
			while frame:
				try:
					iterator = frame.f_locals[STDIN]
				except KeyError:
					frame = frame.f_back
					continue
				return iterator.next()
		finally:
			frame = None
			iterator = None
		raise BrokenPipe()

	def __hash__(self):
		return hash(self.__class__)
	
	def __cmp__(self, other):
		return self.__class__ == other.__class__


STDIN = STDIN()

def _feed_iterator(iterator, stdin):
	if isinstance(iterator, types.GeneratorType):
		generator = iterator
	else:
		generator = (x for x in iterator)
	generator.gi_frame.f_locals[STDIN] = iter(stdin)
	return generator

def _chain(iterables):
	return (len(iterables) == 1 and iter or itertools.chain)(*iterables)

class Pipe(object):

	__slots__ = ['iterator']

	broken_pipe = BrokenPipe()

	def __init__(self, *iterables):
		object.__init__(self)
		if iterables:
			self.iterator = _chain(iterables)
		else:
			self.iterator = None

	def __call__(self, iterable):
		if self.iterator is None:
			return self.__class__(iterable)
		else:
			self.iterator = _feed_iterator(self.iterator, iterable)
			return self

	def __iter__(self):
		if self.iterator is None:
			return self.broken_pipe
		else:
			return self.iterator

	@staticmethod
	def _or(left, right):
		try:
			right.__call__
		except AttributeError:
			try:
				right_iter = iter(right)
			except TypeError:
				return NotImplemented
			else:
				return Pipe(_feed_iterator(right_iter, left))
		else:
			applied = right(left)
			if isinstance(right, type):
				return applied
			else:
				try:
					applied_iter = iter(applied)
				except TypeError:
					return applied
				else:
					return Pipe(applied)
	
	def leak(self):
		return self.iterator

	def __or__(left, right):
		return Pipe._or(left, right)
	
	def __ror__(right, left):
		return Pipe._or(left, right)

	def __repr__(self):
		if self.iterator is None:
			iterator_repr = ''
		else:
			iterator_repr = repr(self.iterator)
		return '%s.%s(%s)' % (self.__module__, self.__class__.__name__, iterator_repr)

class dev_null(_singleton, Pipe):

	def __init__(self):
		Pipe.__init__(self, ())

dev_null = dev_null()

class cat(Pipe):
	
	__slots__ = []

	def __call__(self, *iterables):
		iterable = _chain(iterables)
		if self.iterator is None:
			return self.__class__(iterable)
		else:
			return Pipe.__call__(self, iterable)

cat = cat()

class grep(Pipe):

	__slots__ = ['test']
	REPattern = type(re.compile(''))

	def __init__(self, test, *iterables):

		if isinstance(test, basestring):
			self.test = re.compile(test).search
		elif isinstance(test, grep.REPattern):
			self.test = test.search
		else:
			try:
				self.test = test.__call__
			except AttributeError:
				raise TypeError()
		if iterables:
			Pipe.__init__(self, itertools.ifilter(self.test, _chain(iterables)))
		else:
			Pipe.__init__(self)

	def __call__(self, iterable):
		if self.iterator is None:
			return self.__class__(self.test, iterable)
		else:
			return Pipe.__call__(self, iterable)
	
	def __repr__(self):
		return '%s.%s(%s%s)' % (self.__module__, self.__class__.__name__, repr(self.test), self.iterator and ', <iterator>' or '')

def _slice_repr(_slice):
	if not isinstance(_slice, slice):
		return repr(_slice)
	else:
		values = []
		for name in ['start', 'stop', 'step']:
			value = getattr(_slice, name)
			if value is not None:
				value = repr(value)
			values += value,
		(start, stop, step) = values
		if step is None:
			return '%s:%s' % (start or '', stop or '')
		else:
			return '%s:%s:%s' % (start or '', stop or '', step)

class _cut(Pipe):
	
	__slots__ = ['slice']

	def __init__(self, slice):
		Pipe.__init__(self)
		self.slice = slice

	def __call__(self, iterable):
		return Pipe(item[self.slice] for item in iterable)

	def __repr__(self):
		return '%s.%s[%s]' % (cut.__module__, cut.__class__.__name__, slice_repr(self.slice))

class cut(_singleton):

	__slots__ = []

	def __getitem__(self, slice):
		return _cut(slice)

cut = cut()

class _select(Pipe):
	
	__slots__ = ['slice']

	def __init__(self, slice_):
		Pipe.__init__(self)
		if isinstance(slice_, int):
			if slice_ == -1:
				slice_ = slice(-1, None)
			else:
				slice_ = slice(slice_, slice_ + 1)
		[][slice_]
		self.slice = slice_

	def _select(self, iterable):

		def _step_select(step, iterable):
		
			def _iter(step, iterable):
				i = len = 0
				for item in iterable:
					len += 1
					if i == 0:
						yield item
					i += 1
					if i == step:
						i = 0
				yield len
		
			result = list(_iter(step, iterable))
			return result.pop(), result

		slice = self.slice
		start, stop, step = (slice.start or 0, slice.stop, slice.step or 1)
		if step >= 0 and start >= 0:
			iterator = iter(iterable)
			if stop is None or stop >= 0:
				return itertools.islice(iterator, start, stop, step)
			iterator = itertools.islice(iterator, start, None)
			length, result = _step_select(step, iterator)
			del result[max(0, stop + length + step - 1) // step:]
			return result
		else:
			# FIXME: do it more efficiently
			if isinstance(iterable, (list, tuple, basestring)):
				return iterable[slice]
			else:
				return tuple(iterable)[slice]

	def __call__(self, iterable):
		return Pipe(self._select(iterable))

	def __repr__(self):
		return '%s.%s[%s]' % (select.__module__, select.__class__.__name__, _slice_repr(self.slice))

class select(_singleton):

	__slots__ = []

	def __getitem__(self, slice):
		return _select(slice)

select = select()

def head(n):
	return select[:n]

def tail(n):
	if n < 0:
		return select[n:]
	elif n >= 0:
		return select[max(0, n - 1):]
	else:
		raise TypeError()

class sort(Pipe):

	__slots__ = ['key', 'cmp', 'reverse']

	def __init__(self, *iterables, **kwargs):
		def _sort(iterables, key, cmp, reverse):
			sorted_ = sorted(_chain(iterables), key = key, cmp = cmp, reverse = reverse)
			for item in sorted_:
				yield item
		self.key = kwargs.get('key')
		self.cmp = kwargs.get('cmp')
		self.reverse = kwargs.get('reverse', False)
		if iterables:
			Pipe.__init__(self, _sort(iterables, self.key, self.cmp, self.reverse))
		else:
			Pipe.__init__(self)

	def __call__(self, iterable):
		if self.iterator is None:
			return self.__class__(iterable, key = self.key, cmp = self.cmp, reverse = self.reverse)
		else:
			return Pipe.__call__(self, iterable)

class uniq(Pipe):

	@classmethod
	def _uniq(self, iterable):
		prev = first = 1
		for item in iterable:
			if not first and item == prev:
				continue
			yield item
			prev = item
			first = 0
	
	def __init__(self, *iterables):
		if iterables:
			Pipe.__init__(self, self._uniq(_chain(iterables)))
		else:
			Pipe.__init__(self)

class zuniq(uniq):

	@classmethod
	def _uniq(self, iterable):
		set_ = set()
		for item in iterable:
			if item in set_:
				continue
			set_.add(item)
			yield item

uniq = uniq()
zuniq = zuniq()

def echo(object):
	return Pipe((object,))

def yes(object):
	return Pipe(itertools.repeat(object))

class nl(Pipe):

	__slots__ = []
	start = 0

	def __init__(self, *iterables):
		if iterables:
			iterator = enumerate(_chain((xrange(self.start),) + iterables))
			for i in xrange(self.start):
				iterator.next()
			Pipe.__init__(self, iterator)
		else:
			Pipe.__init__(self)

class nl1(nl):
	start = 1

nl0 = nl()
nl1 = nl1()
nl = nl1

def wc(iterable):
	try:
		return len(iterable)
	except TypeError:
		pass
	i = 0
	for item in iterable:
		i += 1
	return i

def slurp(iterable):
	for x in iterable:
		pass

def seq(x, y = None, z = None):

	def _seq(first, step, last):
		while first <= last:
			yield first
			first += step

	if z is None:
		step = 1
		if y is None:
			first, last = 1, x
		else:
			first, last = x, y
	else:
		first, step, last = x, y, z
	return Pipe(_seq(first, step, last))

class leak(object):

	def __new__(self, object):
		try:
			leak = object.leak
		except AttributeError:
			return object
		else:
			return leak()

class split(Pipe):

	__slots__ = ['n']

	def __init__(self, n):
		if n >= 1:
			self.n = n
		else:
			raise TypeError()
	
	def _split(self, iterable):
		iterator = iter(iterable)
		while 1:
			tup = tuple(itertools.islice(iterator, self.n))
			if tup:
				yield tup
			else:
				return

	def __call__(self, iterable):
		return Pipe(self._split(iterable))

# vim:ts=4 sw=4 noet
