# README

## How to Run

To run the program, use the following command:

```bash
$ python dlrm_s_pytorch.py --mini-batch-size=2 --data-size=4 --arch-embedding-size=6
This command signifies using 1 tables with dimensions of 6, conducting 2 iterations, and using 2 mini-batches per iteration.


Output Format(the output file will be saves as 001.txt) #STOP means end of a iteration
0x10000004 R
0x1000000c R
0x1000000c W
...
...
...
STOP 
0x10000004 R
0x1000000c R
0x1000000c W
...
...
...
STOP
