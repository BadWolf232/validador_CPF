import re 


class validacpf:
    def __init__(self, cpf):
        self.cpf = cpf
    
    def quantidade_de_digitos(self):
        cpf_quantidade = self._so_numero(self.cpf)
        if len(cpf_quantidade) == 11:
            return True
        else:
            return ("Cpf inválido, deve conter 11 dígitos.")
        
    @staticmethod
    def _so_numero(cpf):
        return re.sub('[^0-9]', '', cpf) 

    def validador(self):
        cpf = self._so_numero(self.cpf)
        if not self.quantidade_de_digitos():
            return False
  
        def calculo_digitos(multiplicador):
            total = 0 
            for n in cpf:
                if multiplicador >= 2:
                    total += int(n) * multiplicador
                    multiplicador -= 1
            resto = total % 11 
            if resto < 2:
                 return 0 
            else:
                return 11 - resto
        
        
        if str(cpf[9]) != str(calculo_digitos(10)):
            return ("CPF inválido, o primeiro dígito verificador não confere.")
        
        
        if str(cpf[10]) != str(calculo_digitos(11)):
            return ("CPF inválido, o segundo dígito verificador não confere.")
        
        return ("CPF válido!")


       


    


