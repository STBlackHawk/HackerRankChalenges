#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HackerRank: ComplexNumbers

@author: blackhawk
"""
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.denum = real**2 + imaginary**2
        
    def __add__(self, no):
        r = self.real+no.real
        i = self.imaginary + no.imaginary
        return(Complex(r,i))
        
    def __sub__(self, no):
        r = self.real - no.real
        i = self.imaginary - no.imaginary
        return (Complex(r,i))
        
    def __mul__(self, no):
        r = (self.real*no.real -self.imaginary*no.imaginary)
        i = (self.real*no.imaginary+no.real*self.imaginary)
        return (Complex(r,i))

    def __truediv__(self, no):
        r = (self.real*no.real +self.imaginary*no.imaginary)/no.denum
        i = (no.real*self.imaginary-self.real*no.imaginary)/no.denum
        return Complex(r,i)

    def mod(self):
        return (Complex(math.sqrt(self.denum),0))

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
