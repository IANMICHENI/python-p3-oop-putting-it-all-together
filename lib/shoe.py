#!/usr/bin/env python3
# lib/shoe.py
class Shoe:
    def __init__(self, brand, size,color):
        self.brand = brand
        self.size = size
        self.color = color
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
