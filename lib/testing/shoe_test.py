#!/usr/bin/env python3

from shoe import Shoe

import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand, size, and color passed to __init__, and values can be set to a new instance.'''
        stan_smith = Shoe("Adidas", 9, "white")  # Provide the color parameter
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9, "white")  # Provide the color parameter
        stan_smith.size = "not an integer"  # Set size to a non-integer value
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be an integer\n"

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9, "white")  # Provide the color parameter
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Your shoe is as good as new!\n")
    
    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9, "white")  # Provide the color parameter
        stan_smith.cobble()
        assert(stan_smith.condition == "New")