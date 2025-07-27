from validador_cpf import validacpf 
from cpf_generator import CPF 

cpf = CPF.generate()
cpf_formatted = CPF.format(cpf)
cpf_validator = validacpf(cpf_formatted)

print("#" * 20)

print("CPF gerado:", cpf_formatted)
print(cpf_validator.validador())

print("#" * 20)