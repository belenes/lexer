TT = [("Tipo",a_int),
      ("Tipo",a_float),
      ("If",a_if),
      ("For",a_for),
      ("While",a_while),
      ("ParAbierto", a_ParAbierto),
      ("ParCerrado", a_ParCerrado),
      ("LLaAbierta", a_LLaAbierta),
      ("LLaCerrada", a_LLaCerrada),
      ("+", a_Mas),
      ("-", a_Menos),
      ("*", a_Por),
      ("/", a_Dividido),
      (",", a_Coma),
      (";", a_PuntoComa),
      (":=", a_PuntoIgual),
      ("Comparacion", a_Menor),
      ("Comparacion", a_Mayor),
      ("Comparacion", a_MayorIgual),
      ("Comparacion", a_MenorIgual),
      ("Comparacion",a_Distinto),
      ("Comparacion", a_IgualIagual),
      ("Numero", a_Num),
      ("Identificador", a_Id)
]

def lexer(src):
    tokens[]
    src = src + " "
    i = 0
    start = 0
    state = 0
    while i<len(src):
        c = src[i]
        w = src[start: i+1]
        if state == 0:
            if c.isspace():
                i+=1
                state = 0
            else:
                start = i
                state = 1
        if state == 1:
            if es_aceptada(w) or not c.isspace():
                i+=1
                state = 1
            else:
                i-=1
                state = 2

def es_aceptada(w):

    candidatos = []

    if len(candidatos)>0:
        return True
    else:
        return False 
