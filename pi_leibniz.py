"""
    Copyright 2020 Philip Mortimer
    
    This file is part of Philip Mortimer Example Programs.
    
    Philip Mortimer Example Programs is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.
    
    Philip Mortimer Example Programs is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Philip Mortimer Example Programs.  If not, see 
    <https://www.gnu.org/licenses/>.
"""


NUM_TERMS = int(1e6)

import math

def calc_pi_leibniz(num_terms):
    """
    num_terms:   number of terms in the series 
       
    Calculates an approximation to PI using the 
    Leibniz series:
                   
       4/1 - 4/3 + 4/5 - 4/7 + ...

    The greater the number of terms in the series the closer the
    approximation is to PI.
    """  
    assert (num_terms >= 1),"must be at least 1 term"
    
    pi = 0
    numerator = 4
    for n in range(1, num_terms*2+1, 2):
        pi += numerator / n
        numerator = -numerator
    return pi


def test_pi_leibniz(num_terms):
    pi = calc_pi_leibniz(num_terms)

    print("Leibniz series with {} terms gives:\n\t\tpi={}".format(
            num_terms, pi))

    print("\nPython math.pi is:\n\t\tpi={}".format(math.pi))     


if __name__ == '__main__':
    test_pi_leibniz(NUM_TERMS)

