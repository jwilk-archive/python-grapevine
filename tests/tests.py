# encoding=UTF-8

# Copyright © 2015 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from tools import (
    assert_equal,
    assert_false,
    assert_is_instance,
    assert_list_equal,
    assert_raises,
    assert_regex,
    assert_true,
    SkipTest,
)

import grapevine as g

def test_broken_pipe():
    bp = g.BrokenPipe()
    with assert_raises(g.BrokenPipe):
        for x in bp:
            assert_true(False, msg='pipe is not broken')

class test_stdin:

    def test_iter(self):
        lst = g.cat([37, 42]) | (-x for x in g.STDIN) | list
        assert_list_equal(lst, [-37, -42])

    def test_broken_pipe(self):
        with assert_raises(g.BrokenPipe):
            for x in g.STDIN:
                assert_true(False, msg='pipe is not broken')

    def test_hashable(self):
        d = {}
        d[g.STDIN] = 42
        assert_equal(d[g.STDIN], 42)

    def test_eq(self):
        assert_false(g.STDIN == 42)

    def test_ne(self):
        assert_true(g.STDIN != 42)

    def test_repr(self):
        assert_equal(repr(g.STDIN), 'grapevine.STDIN')

class test_dev_null:

    def test_iter(self):
        for x in g.dev_null:
            assert_true(False, msg='dev_null not empty')

    def test_repr(self):
        assert_equal(repr(g.dev_null), 'grapevine.dev_null')

class test_cat:

    def test_0(self):
        pipe = [37, 42] | g.cat
        assert_list_equal(list(pipe), [37, 42])

    def test_1(self):
        pipe = g.cat([37, 42])
        assert_list_equal(list(pipe), [37, 42])

    def test_2(self):
        pipe = g.cat([17], [23, 37])
        assert_list_equal(list(pipe), [17, 23, 37])

    def test_repr(self):
        assert_equal(repr(g.cat), 'grapevine.cat()')
        pipe = g.cat([37, 42])
        assert_regex(repr(pipe), r'\Agrapevine[.]cat[(]<[^>]+>[)]\Z')

class test_grep:

    def test_0(self):
        pipe = ['eggs', 'spam', 'ham'] | g.grep('[ph]am')
        assert_list_equal(list(pipe), ['spam', 'ham'])

    def test_1(self):
        pipe = g.grep('[ph]am', ['eggs', 'spam', 'ham'])
        assert_list_equal(list(pipe), ['spam', 'ham'])

    def test_2(self):
        pipe = g.grep('[ph]am', ['eggs'], ['spam', 'ham'])
        assert_list_equal(list(pipe), ['spam', 'ham'])

    def test_cb(self):
        pipe = [17, 37, 42] | g.grep(lambda n: n % 7 != 2)
        assert_list_equal(list(pipe), [17, 42])

    def test_repr(self):
        pipe = g.grep('[ph]am')
        assert_regex(repr(pipe), r'\Agrapevine[.]grep[(]<[^>]+>[)]\Z')
        pipe = g.grep('[ph]am', ['eggs', 'spam', 'ham'])
        assert_regex(repr(pipe), r'\Agrapevine[.]grep[(]<[^>]+>, <[^>]+>[)]\Z')

class test_cut:

    def test_0(self):
        pipe = ['eggs', 'spam', 'ham'] | g.cut[1]
        assert_list_equal(list(pipe), ['g', 'p', 'a'])

    def test_1(self):
        pipe = g.cut[1](['eggs', 'spam', 'ham'])
        assert_list_equal(list(pipe), ['g', 'p', 'a'])

    def test_2(self):
        pipe = g.cut[1](['eggs'], ['spam', 'ham'])
        assert_list_equal(list(pipe), ['g', 'p', 'a'])

    def test_slicing(self):
        class s(object):
            def __getitem__(self, k):
                return k
        s = s()
        def t(text, slc, xtext, xrepr):
            pipe = g.cut[slc]
            assert_equal(repr(pipe), 'grapevine.cut[{0}]'.format(xrepr))
            pipe = [text] | pipe
            assert_list_equal(list(pipe), [xtext])
        t('spam', s[0], 's', '0')
        t('spam', s[1], 'p', '1')
        t('spam', s[-1], 'm', '-1')
        t('spam', s[:], 'spam', ':')
        t('spam', s[::], 'spam', ':')
        t('spam', s[:0], '', ':0')
        t('spam', s[:2], 'sp', ':2')
        t('spam', s[:-1], 'spa', ':-1')
        t('spam', s[0:], 'spam', '0:')
        t('spam', s[1:], 'pam', '1:')
        t('spam', s[-2:], 'am', '-2:')
        t('spam', s[::1], 'spam', '::1')
        t('spam', s[::-1], 'maps', '::-1')
        t('spam', s[1:-1:2], 'p', '1:-1:2')

class test_select:

    def test_0(self):
        pipe = ['eggs', 'spam', 'ham'] | g.select[1]
        assert_list_equal(list(pipe), ['spam'])

    def test_1(self):
        pipe = g.select[1](['eggs', 'spam', 'ham'])
        assert_list_equal(list(pipe), ['spam'])

    def test_2(self):
        raise SkipTest('not implemented yet')
        pipe = g.select[1](['eggs'], ['spam', 'ham'])
        assert_list_equal(list(pipe), ['spam'])

    def test_slicing(self):
        class s(object):
            def __getitem__(self, k):
                return k
        s = s()
        def t(text, slc, xtext, xrepr):
            pipe = g.select[slc]
            assert_equal(repr(pipe), 'grapevine.select[{0}]'.format(xrepr))
            pipe = list(text) | pipe
            assert_equal(''.join(pipe), xtext)
        t('spam', s[0], 's', '0:1')
        t('spam', s[1], 'p', '1:2')
        t('spam', s[-1], 'm', '-1:')
        t('spam', s[:], 'spam', ':')
        t('spam', s[::], 'spam', ':')
        t('spam', s[:0], '', ':0')
        t('spam', s[:2], 'sp', ':2')
        t('spam', s[:-1], 'spa', ':-1')
        t('spam', s[0:], 'spam', '0:')
        t('spam', s[1:], 'pam', '1:')
        t('spam', s[-2:], 'am', '-2:')
        t('spam', s[::1], 'spam', '::1')
        t('spam', s[::-1], 'maps', '::-1')
        t('spam', s[1:-1:2], 'p', '1:-1:2')

class test_head:

    def test_positive(self):
        pipe = ['eggs', 'spam', 'ham'] | g.head(2)
        assert_list_equal(list(pipe), ['eggs', 'spam'])

    def test_positive_overflow(self):
        pipe = ['eggs', 'spam', 'ham'] | g.head(4)
        assert_list_equal(list(pipe), ['eggs', 'spam', 'ham'])

    def test_zero(self):
        pipe = ['eggs', 'spam', 'ham'] | g.head(0)
        assert_list_equal(list(pipe), [])

    def test_negative(self):
        pipe = ['eggs', 'spam', 'ham'] | g.head(-2)
        assert_list_equal(list(pipe), ['eggs'])

    def test_negative_overflow(self):
        pipe = ['eggs', 'spam', 'ham'] | g.head(-4)
        assert_list_equal(list(pipe), [])

class test_tail:

    def test_positive(self):
        # FIXME?
        pipe = ['eggs', 'spam', 'ham'] | g.tail(+2)
        assert_list_equal(list(pipe), ['spam', 'ham'])

    def test_positive_overflow(self):
        pipe = ['eggs', 'spam', 'ham'] | g.tail(+4)
        assert_list_equal(list(pipe), [])

    def test_zero(self):
        # FIXME?
        pipe = ['eggs', 'spam', 'ham'] | g.tail(-0)
        assert_list_equal(list(pipe), ['eggs', 'spam', 'ham'])

    def test_negative(self):
        pipe = ['eggs', 'spam', 'ham'] | g.tail(-2)
        assert_list_equal(list(pipe), ['spam', 'ham'])

    def test_negative_overflow(self):
        pipe = ['eggs', 'spam', 'ham'] | g.tail(-4)
        assert_list_equal(list(pipe), ['eggs', 'spam', 'ham'])

# vim:ts=4 sts=4 sw=4 et
