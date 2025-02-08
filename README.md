# Ternary-Addition-Turing-Machine

This project uses [JFLAP](https://www.jflap.org/), an software for simulating automata and machines, to build a Turing machine that adds ternarny numbers. 

In this directory is the machine and programs to run and create tests. 

From a high level, this program works by marking corresponding least significant digits, adding them to a carryover digit—the current most significant digit—of the output, and distributing that carryover for the next operation until all input digits are marked. A more precise explanation is below. 

This project is from Binghamton University's CS 373, Formal Language & Automata Theory.

# Table of contents
- [Files](#files)
- [Requirements](#requirements)
- [How To Use](#how-to-use)
- [Specifics](#specifics)

# Files

1. `ternarny.jff` is the JFLAP file with the Turing machine.

2. `generate_test.py` is a Python script to generate an input of two random ternargy numbers of length 100-120 in the form `number1#number2`, stored in `test_cases.txt`, and the expected sum in `expected_cases.txt`.

3. `validate_test.py` compares the text in `expected_cases.txt` to the output in `result.txt`, returning if the results match, and if not, shows the expected vs. the actual result. 

4. `test_cases.txt` holds the generated input, file does not need to be edited, but the content needs to be fully copied (using Ctrl/Cmd + A to get the entire text).

5. `expected_cases.txt` holds the expected answer, file does not need to be edited. 

6. `results.txt` is where to paste the copied row content from JFLAP after running. The entire row of input/output/result needs to be copied, and can be selected by simply clicking the table row on JFLAP. 

# Requirements

To test this program, you need to have [JFLAP](https://www.jflap.org/) installed. 

To create and check test cases, you need to have python installed. 

# How to use

1. Open JFLAP, select `File` -> `Open`, find this directory and open `ternary.jff`. Select `Input` -> `Multiple Run (Transducer)`, and a three column table should open. 
    - Note that it may be difficult for JFLAP to locate directories on your system. You can copy/move `ternary.jff` to where your JFLAP file is, as `ternary.jff` does not depend on other files in the directory, it just needs to be run. 

2. Then, in this directory, run...
    ```
    $ python3 generate_test.py
    ```
    or your system's equivalent. This populates the `test_cases.txt` and `expected_cases.txt` with the input and expected output for two ternary numbers of length 100-120.

3. Open `test_cases.txt` and copy (Ctrl/Cmd + A) the entire text, and paste that text into the input column of any row on your JFLAP table, and select `Run Inputs`.
    - Double clicking the text will only select half of the input and stops at the `#`
    - If the run results in `Reject`, it is likely that the full input text was not copied
    - If the input is correctly running, you will receive a popup asking you to continue generating configurations, which you will need to confirm a few times.

4. To test the result, click on the row (which will select all columns) and copy the content. Open `results.txt`, paste the results, and save the file.
    - The content should be in the form `input output result`

5. To test your results against the expected result, run...
    ```
    $ python3 validate_test.py
    ```
    To check the validity of this program, change a digit in `results.txt`. To continue testing, go back to step 2, or, come up with your own test cases.  

# Specifics

1. From states q0 to q45, an $ is added to the first position to indicate the start, the input is shifted to the right by one, and an # and 0 are added at the end to mark the start of the output and be the first carryover digit. 
    - If there is no # or there are multiple #s in the input, then the input is rejected
    - We shift the input and add a placeholder to the start because we assume the definition of a tape that can only expand rightward

2. At q5, the tape is rewinded to the start position, $.

3. At q9, marked digits (replaced with an a) are looped through until an unmarked digit is found in either the first or second number.
    - If there are no unmarked digits, we move to q12, where we move past any leaading 0s then return the tape to the right of the head at q42 or q43.
    - If an unmarked digit is found, we rewind the tape to $ at q10 and move to step 4.

4. At q13, we move right until we find the rightmost unmarked digit in the first number, i.e. the least significant digit.
    - If none is found, this value is treated as a 0. Depending on that value, we mark the digit with an a and we move to state q15(0), q16(1), or q17(2).  

5. At q18, q25, or q24, we loop through the second number until we reach the start of the output, which is the current most significant digit and the carryover from the last calculation. Then, at q19, q26, or q28, our least significant value from the first numbers is added to our carryover, which is either 0 or 1.

6. At q20, we move to the left from the output and are now at the rightmost digit of the second number, where we move left until we find an unmarked digit. Following the same protocol of using three paths for each possible value, we add these values to our carryover.

7. At q32, the carryover, a digit from 0-5, is distributed to a new carryover digit with the following conversions: 0 = 00; 1 = 01; 2 = 02; 3 = 10; 4 = 11; 5 = 12.

8. At q39, q40, and q41, the output is shifted to the right by 1 to make space for the new carryover digit.

9. At q5, the process restarts at step 2. 

