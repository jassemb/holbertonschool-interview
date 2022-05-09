## 0x03. Minimum Operations

<br>In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.<br>

<br>Prototype: def minOperations(n)<br>
Returns an integer<br>
If n is impossible to achieve, return 0<br>
Example:<br>

n = 9<br>
<br>
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH<br>
<br>
Number of operations: 6<br>