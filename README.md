# Python programs that calculate an approximation to the value of PI

Each of the following programs calculates an approximation to the value of PI
using a series as stated below:

|File 	               |Description                                                                                         |
|----------------------|----------------------------------------------------------------------------------------------------|
|pi_leibniz.py         |Uses the Leibniz series: 4/1 - 4/3 + 4/5 - 4/7 + ...                                                |
|pi_nilakantha.py 	   |Uses the Nilakantha series: 3 + 4/(2 * 3 * 4) - 4/(4 * 5 * 6) + 4/(6 * 7 * 8) - 4/(8 * 9 * 10) + ...|

Each program displays the result of the calculation, and also displays the value of the Python
**math.pi** constant so that you can compare it to the calculated value.

Near the top of each program is a constant called **NUM_TERMS** which specifies how many terms
are to be used in the series. The larger the value of this variable the closer the approximation 
will be to PI, but, of course, the longer the program will take to calculate the result.
