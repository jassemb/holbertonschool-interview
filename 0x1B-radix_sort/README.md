## 0x1B. Radix Sort


### Applications of Radix Sort: 

In a typical computer, which is a sequential random-access machine, where the records are keyed by multiple fields radix sort is used.</br> For eg., you want to sort on three keys month, day and year. You could compare two records on year, then on a tie on month and finally on the date. Alternatively, sorting the data three times using Radix sort first on the date, then on month, and finally on year could be used.</br>
It was used in card sorting machines with 80 columns, and in each column, the machine could punch a hole only in 12 places. The sorter </br>was then programmed to sort the cards, depending upon which place the card had been punched. This was then used by the operator to </br>collect the cards which had the 1st row punched, followed by the 2nd row, and so on.</br>
Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort? </br>

If we have log2n bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide range of input </br>numbers. The constant factors hidden in asymptotic notation are higher for Radix Sort and Quick-Sort uses hardware caches more </br>effectively. Also, Radix sort uses counting sort as a subroutine and counting sort takes extra space to sort numbers.</br>