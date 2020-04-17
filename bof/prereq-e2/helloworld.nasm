
section .text
   global _start
	
_start:	            
	mov eax, 4
	mov ebx, 1
	mov ecx, msg
	mov edx, len
	int 0x80

	mov eax, 1
	mov ebx, 20
	int 0x80

section	.data
	msg db 'Hello, world!', 0xa  
	len equ $ - msg     
