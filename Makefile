# flags
CC = gcc
ASM = nasm
ASM_FLAGS = -f elf64


# All Targets
all: sic_vm

# link and build program
sic_vm: main.o
	@echo 'Building target'
	$(CC) -o sic_vm main.o
	@echo 'Done'
# compile each file
main.o: main.s
	$(ASM) $(ASM_FLAGS) main.s -o main.o

# Clean the build directory
clean:
	rm -f *.o sic_vm

# Run program
run:
	./sic_vm
