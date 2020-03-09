# computerSecurity2ndSemster2020
this is solutions to tasks in computer security course - shobra faculty of engineering 

**Task 1** is uploaded with the source code in [_assignment 1_](https://github.com/andrew-anter/cryptography2ndSemster2020/tree/master/Assignment1) folder<br/>

**How to run \'task1\'** <br/>

- shift cipher <br/>
  - encrypt : `python main.py shift encrypt inputFile.txt outputFile.txt key` <br/>
  - decrypt : `python main.py shift decrypt inputFile.txt outputFile.txt key` <br/>
- affine cipher <br/>
  - encrypt : `python main.py affine encrypt inputFile.txt outputFile.txt key1 key2` <br/>
  - decrypt : `python main.py affine decrypt inputFile.txt outputFile.txt key1 key2` <br/>
  *note : key1 must be coprime to 26*<br/>
- vigenere cipher <br/>
  - encrypt : `python main.py vigenere encrypt inputFile.txt outputFile.txt key1 key2` <br/>
  - decrypt : `python main.py vigenere decrypt inputFile.txt outputFile.txt key1 key2` <br/>
