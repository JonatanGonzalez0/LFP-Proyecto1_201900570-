class Token:
    lexema_valido = ''
    tipo = 0
    fila =0
    columna = 0

    #ENUM
    PALABRA_RESERVADA = 1
    CADENA = 2
    NUMERO = 3
    TRUE = 4
    BOOLEANOS = 5
    NUMERO_HEX = 6
    IGUAL = 7
    PUNTO_COMA = 8
    LLAVE_I = 9
    LLAVE_D = 10
    CORCHETE_I = 11
    CORCHETE_D = 12
    COMA = 13
    SEPARADOR_IMAGEN = 14
    DESCONOCIDO = 15

    def __init__(self,lexema,tipo,fila,columna):
        self.lexema_valido = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        
    def getLexema(self):
        return self.lexema_valido
    
    def getFila(self):
        return str(self.fila)

    def getColumna(self):
        return str(self.columna)
    
    def getTipo(self):
        if self.tipo == self.PALABRA_RESERVADA:
            return 'PALABRA RESERVADA'
        elif self.tipo== self.CADENA:
            return 'CADENA'
        elif self.tipo== self.NUMERO:
            return 'NUMERO'
        elif self.tipo== self.BOOLEANOS:
            return 'BOOLEANO'
        elif self.tipo== self.NUMERO_HEX:
            return 'NUMERO COLOR HEX'
        elif self.tipo== self.IGUAL:
            return 'IGUAL'
        elif self.tipo== self.PUNTO_COMA:
            return 'PUNTO COMA'
        elif self.tipo== self.LLAVE_I:
            return 'LLAVE IZQUIERDA'
        elif self.tipo== self.LLAVE_D:
            return 'LLAVE DERECHA'
        elif self.tipo== self.CORCHETE_I:
            return 'CORCHETE IZQUIERDO'
        elif self.tipo== self.CORCHETE_D:
            return 'CORCHETE DERECHO'
        elif self.tipo== self.COMA:
            return 'COMA'
        elif self.tipo== self.SEPARADOR_IMAGEN:
            return 'SEPARADOR IMAGEN @@@@'
        elif self.tipo== self.DESCONOCIDO:
            return 'DESCONOCIDO ERROR'








