# -*- coding: utf-8 -*-
from django.template import Library

register = Library()


def get_before(value, arg):
	arg = int(arg)
	l_lim = arg - 5
	if l_lim < 1:
		l_lim = 1
	return range(l_lim, arg)


def get_after(value, arg):
	arg = int(arg)
	r_lim = arg + 5
	if r_lim > len(value):
		r_lim = len(value)+1
	return range(arg+1, r_lim)


register.filter('get_before', get_before)
register.filter('get_after', get_after)
