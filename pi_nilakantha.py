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

def calc_pi_nilakantha(num_terms):
    """
    num_terms:   number of terms in the series 
       
    Calculates an approximation to PI using the 
    Nilakantha series:
                   
        3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + ...

    The greater the number of terms in the series the closer the
    approximation is to PI.
    """  
    assert (num_terms >= 1),"must be at least 1 term"
    
    # Initialise pi to the 1st term in the series.
    pi = 3 
    
    # Process the remaining terms.
    numerator = 4
    for n in range(2, num_terms*2-1, 2):
        pi += numerator / (n * (n+1) * (n+2))
        numerator = -numerator
    return pi


def test_pi_nilakantha(num_terms):
    pi = calc_pi_nilakantha(num_terms)

    print("Nilakantha series with {} terms gives:\n\t\tpi={}".format(
            num_terms, pi))

    print("\nPython math.pi is:\n\t\tpi={}".format(math.pi))     


if __name__ == '__main__':
    test_pi_nilakantha(NUM_TERMS)

    
