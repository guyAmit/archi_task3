extern printf
extern scanf
extern malloc
extern free
global main


%define MAX_PHYSICAL_MEMORY 4096

section .bss
  sic_vm_memory_pointer_pointer:   				resq 1
  size:     				resq 1
  input: resq 1

section .data
	input_string: db  "%d",10,0
  out_string: db "%d ",0
  out_string1: db "%d %d %d",10,0
  newline: db 10
section .text
main:
	nop
  enter 0, 0 ; prepare a frame

  mov rax, MAX_PHYSICAL_MEMORY
  mov rbx, 8
  mul rbx

  mov [size], rax
  mov rdi,rax
  call malloc
  mov [sic_vm_memory_pointer_pointer], rax

  mov r13, qword[sic_vm_memory_pointer_pointer]
  xor r14,r14

  input_loop:
    mov rdi, input_string
    mov rsi, input
    mov rax,0
    call scanf

    mov r15, qword[input]
    mov [r13+r14], r15
    xor r15,r15

    add r14,8
    cmp qword[size], r14
    jne input_loop
  end_input_loop:

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; loop memory loop code go's here
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
start_mem_loop:
 mov r13, qword[sic_vm_memory_pointer_pointer]
 xor r14,r14

 mem_loop:
   cmp qword[r13+r14],0
   jne if_statment
   cmp qword[r13+r14+8],0
   jne if_statment
   cmp qword[r13+r14+16],0
   jne if_statment
   je end_mem_loop

   if_statment:
   ;;if(M[M[i]]-=M[M[i+1]]<0)
   mov r10, qword[r13+r14+8]
   mov r10, qword[r13+r10*8] ;;r10 = M[M[i+1]]

   xor r15,r15
   mov r11, qword[r13+r14]
   mov r15, qword [r13+r11*8]
   sub r15 , r10
   mov qword[r13+r11*8], r15 ;;M[M[i]]-=M[M[i+1]]

   cmp r15,0
   jl less_than_zero
   jmp greater_than_zero

   less_than_zero:
    mov rax,qword[r13+r14+16]
    mov rbx, 8
    mul rbx
    mov r14,rax ;;changed instruction register
    jmp mem_loop

   greater_than_zero:
      add r14, 8*3
      jmp mem_loop
 end_mem_loop:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; loop memory loop code end's here
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

  mov r13, qword[sic_vm_memory_pointer_pointer]
  xor r14, r14
  output_loop:
    mov rdi, out_string
    mov rsi,qword[r13+r14]
    mov rax,0
    call printf

    add r14,8
    cmp qword[size], r14
    jne output_loop
  end_output_loop:

  mov rdi, newline
  call printf

  mov rdi, qword[sic_vm_memory_pointer_pointer]
  call free

  leave		; dump the top frame
  ret ; return from main
