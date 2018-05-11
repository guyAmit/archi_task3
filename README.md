# Caspl task3 - self modifing code using sic-single instruction code


homework 3 in the caspl course at ben Gurion university. in this project
we will build two virtual machines:
  1) asm-nasm virtual machine for running sic code from stream
  2) sic virtual machine for running sic codes

the purpose of this project is to build a asm-nasm virtual machine for sic that
will run a series of sic-based virtual machines, s.t. the last virtual machine will run a sic
that calculate the Fibonacci series.

## Getting Started

for running the asm-nasm virtual machine use
```
make run or for running with input:  ./sic_vm <input_file.sic
```
for running the sic virtual machine
```
 cat sic.sic sic.sic ... input_file.sic | ./sic_vm  
```

## Currently Supporting

* **the asm-nsam virtual machine**
* **the sic-based virtual machine is Currently in planning**

## Prerequisites

This project was built on Linux operating system only.
and it will support only Linux operating systems.

## Versioning

current version : 1.0.0

## Authors

* **Guy Amit** - [guyAmit](https://github.com/guyAmit)
* **Omri Eitan** -[omrieitan](https://github.com/omrieitan)

## License
M.I.T License in separate file
