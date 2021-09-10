from tkinter.constants import FALSE
from Token import Token
import re
class Analizador:
    lexema = ''
    tokens =[]
    estado = 1
    fila = 1
    columna = 1
    generar = True

    tipos = Token("lexema",-1,-1,-1)

    def Scanner(self,entrada):
        self.estado =1
        self.lexema =''
        self.tokens = []
        self.fila =1 
        self.columna =1
        self.generar = False
        
        entrada = entrada +"&"
        actual = ''
        longitud = len(entrada)
        
        for i in range(longitud):
            actual = entrada[i]
            
            if actual=="&":
                print('Se completo el analisis')
                break
            if self.estado == 1:
                if actual.isalpha():
                    self.estado = 2
                    self.columna +=1
                    self.lexema += actual
                    continue
                if actual.isdigit():
                    self.estado = 3
                    self.columna +=1
                    self.lexema+=actual
                    continue
                if actual == '"':
                    self.estado = 4
                    self.columna +=1
                    self.lexema+=actual
                    continue
                      
                if actual =='#':
                    self.estado =5
                    self.lexema +=actual
                    
                if actual =='@':
                    self.estado = 6
                    self.lexema +=actual
                    
                if actual =='=':
                    self.lexema +=actual
                    self.columna +=1
                    self.agregarToken(self.tipos.IGUAL)
                    
                if actual ==',':
                    self.lexema +=actual
                    self.columna +=1
                    self.agregarToken(self.tipos.COMA)
                    
                if actual ==';':
                    self.lexema +=actual
                    self.columna +=1
                    self.agregarToken(self.tipos.PUNTO_COMA)
                    
                if actual =='{':
                    self.lexema +=actual
                    self.columna +=1
                    self.agregarToken(self.tipos.LLAVE_I)
                    
                if actual =='}':
                    self.lexema +=actual
                    self.columna +=1
                    self.agregarToken(self.tipos.LLAVE_D)
                    
                if actual =='[':
                    self.lexema +=actual
                    self.columna +=1
                    self.agregarToken(self.tipos.CORCHETE_I)
                    
                if actual ==']':
                    self.lexema +=actual
                    self.columna +=1
                    self.agregarToken(self.tipos.CORCHETE_D)
                    
                if actual == ' ':
                    self.columna+=1
                if actual == "\n":
                    self.fila +=1
                if actual =="\t":
                    self.columna+=5
                    

            elif self.estado ==2:
                if actual.isalpha():
                    self.estado = 2
                    self.columna +=1
                    self.lexema += actual
                    continue
                else:
                    if self.es_palabra_reservada(self.lexema):
                        self.agregarToken(self.tipos.PALABRA_RESERVADA)
                        if actual =='=':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.IGUAL)
                        if actual ==',':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.COMA)
                        if actual ==';':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.PUNTO_COMA)
                        
                    elif self.es_True_False(self.lexema):
                        self.agregarToken(self.tipos.BOOLEANOS)
                        if actual ==',':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.COMA)
                    else:
                        self.lexema += actual
                        self.agregarToken(self.tipos.DESCONOCIDO)
                        self.generar =False
                        
                        if actual =='=':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.IGUAL)
                        if actual ==',':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.COMA)
                        if actual ==';':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.PUNTO_COMA)
                 
            elif self.estado ==3:
                if actual.isdigit():
                    self.estado = 3
                    self.columna +=1
                    self.lexema+=actual
                    continue
                else:
                    if self.lexema.isdigit():
                        self.agregarToken(self.tipos.NUMERO)
                        if actual ==';':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.PUNTO_COMA)
                        if actual ==',':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.COMA)
                    else:
                        self.lexema +=actual
                        self.columna +=1
                        self.agregarToken(self.tipos.DESCONOCIDO)
                        self.generar = False
                        
                        if actual ==';':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.PUNTO_COMA)
                            
                        if actual ==',':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.COMA)
            
            elif self.estado ==4:
                if actual != '"':
                    self.estado = 4
                    self.columna +=1
                    self.lexema +=actual
                    continue
                elif actual=='"':
                    self.lexema += actual
                    self.columna +=1
                    self.agregarToken(self.tipos.CADENA)  
            
            elif self.estado ==5:
                if actual.isalpha() or actual.isdigit():
                    self.estado = 5
                    self.columna +=1
                    self.lexema += actual
                    continue
                else:
                    if self.esHex(self.lexema):
                        self.agregarToken(self.tipos.NUMERO_HEX)
                        if actual ==']':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.CORCHETE_D)                  
                    else:
                        self.agregarToken(self.tipos.DESCONOCIDO)
                        self.generar = False
                        
                        if actual ==']':
                            self.lexema +=actual
                            self.columna +=1
                            self.agregarToken(self.tipos.CORCHETE_D)
                        
            elif self.estado==6:
                if actual =="@":
                    self.lexema +=actual
                    self.columna+=1
                else:
                    if self.lexema=='@@@@':
                        self.agregarToken(self.tipos.SEPARADOR_IMAGEN)
                    else:
                        self.agregarToken(self.tipos.DESCONOCIDO)
                
                
    def agregarToken(self,tipo):
        self.lexema = self.lexema.lower()
        self.tokens.append(Token(self.lexema,tipo,self.fila,self.columna))
        self.lexema = ''
        self.estado =1

    def es_palabra_reservada(self,entrada):
        entrada = entrada.lower()
        valor = False
        reservadas = ['titulo','ancho','alto','filas','columnas','celdas','filtros','mirrorx','mirrory','doublemirror']
        if entrada in reservadas:
            valor =True
        return valor
    
    def es_True_False(self, entrada):
        entrada = entrada.lower()
        valor = False
        valores = ['true','false']
        if entrada in valores:
            valor = True    
        return valor
    
    def esHex(self,entrada):
        coincidencia = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', entrada)
        valor = False
        if coincidencia:
            valor = True
        else:
            valor = False
        return valor
    
    def imprimir(self):
        for x in self.tokens:
            if x.tipo != self.tipos.DESCONOCIDO:
                lex = x.getLexema()
                tipo = x.getTipo()
                fila = x.getFila()
                columna = x.getColumna()
                
                print(f'Lex: {lex} Tipo: {tipo} Fila: {fila} Columna: {columna}')
                
    def imprimirErrores(self):
        for x in self.tokens:
            if x.tipo == self.tipos.DESCONOCIDO:
                lex = x.getLexema()
                tipo = x.getTipo()
                fila = x.getFila()
                columna = x.getColumna()
                
                print(f'Lex: {lex} Tipo: {tipo} Fila: {fila} Columna: {columna}')
                
    def sePuedeGenerar(self):
        valor = True
        for x in self.tokens:
            if x.tipo == 15:
                valor =False
                return valor
        return valor       
                
                