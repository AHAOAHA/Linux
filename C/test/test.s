	.file	"test.c"
	.text
	.section	.rodata
.LC0:
	.string	"hello\n"
.LC1:
	.string	"%s"
	.text
	.globl	main
	.type	main, @function
main:
.LFB5:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$1072, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	leaq	-1048(%rbp), %rax
	movq	%rax, %rdi
	call	pipe@PLT
	call	fork@PLT
	movl	%eax, -1068(%rbp)
	cmpl	$0, -1068(%rbp)
	jne	.L2
	movl	$10, -1072(%rbp)
	movl	-1048(%rbp), %eax
	movl	%eax, %edi
	call	close@PLT
	leaq	.LC0(%rip), %rax
	movq	%rax, -1056(%rbp)
	jmp	.L3
.L4:
	movq	-1056(%rbp), %rax
	movq	%rax, %rdi
	call	strlen@PLT
	movq	%rax, %rdx
	movl	-1044(%rbp), %eax
	movq	-1056(%rbp), %rcx
	movq	%rcx, %rsi
	movl	%eax, %edi
	call	write@PLT
	movl	$1, %edi
	call	sleep@PLT
.L3:
	movl	-1072(%rbp), %eax
	leal	-1(%rax), %edx
	movl	%edx, -1072(%rbp)
	testl	%eax, %eax
	jne	.L4
	movl	-1044(%rbp), %eax
	movl	%eax, %edi
	call	close@PLT
	movl	$0, %edi
	call	exit@PLT
.L2:
	movl	-1044(%rbp), %eax
	movl	%eax, %edi
	call	close@PLT
.L7:
	movl	-1048(%rbp), %eax
	leaq	-1040(%rbp), %rcx
	movl	$1023, %edx
	movq	%rcx, %rsi
	movl	%eax, %edi
	call	read@PLT
	movq	%rax, -1064(%rbp)
	leaq	-1040(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movq	$0, -1064(%rbp)
	cmpq	$0, -1064(%rbp)
	jne	.L11
	jmp	.L7
.L11:
	nop
	movl	-1068(%rbp), %eax
	cltq
	movq	%rax, %rdi
	call	wait@PLT
	movl	$0, %eax
	movq	-8(%rbp), %rsi
	xorq	%fs:40, %rsi
	je	.L9
	call	__stack_chk_fail@PLT
.L9:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE5:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.3.0-16ubuntu3) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
