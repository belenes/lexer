TT = [("Tipo",a_int),
      ("Tipo",a_float),
      ("If",a_if),
      ("For",a_for),
      ("While",a_while),
      ("(", a_ParAbierto),
      (")", a_ParCerrado),
      ("{", a_LLaAbierta),
      ("}", a_LLaCerrada),
      ("+", a_Mas),
      ("-", a_Menos),
      ("*", a_Por),
      ("/", a_Dividido),
      (",", a_Coma),
      (";", a_PuntoComa),
      (":=", a_PuntoIgual),
      ("<", a_Comparacion),
      (">", a_Comparacion),
      (">=", a_Comparacion),
      ("<=", a_Comparacion),
      ("!=",a_Comparacion),
      ("==", a_Comparacion),
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
        word = src[start: i+1]
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
        if state == 2:
            state = 0
            i+= 1

def calc_candidatos(word):
      candidatos = []
      tipo_token = clasi[0]

def es_aceptada(word):

    candidatos = []

    if len(candidatos)>0:
        return True
    else:
        return False

def a_ParAbierto(src):
    s = 1
    for c in src:
        if s == 1 and c=='(':
            s == 2
    return s == 2
def a_ParCerrado(src):
    s = 1
    for c in src:
        if s == 1 and c==')':
            s == 2
    return s == 2
def a_LLaAbierta(src):
    s = 1
    for c in src:
        if s==1 and c=='{':
            s == 2
    return s == 2
def a_LLaCerrada(src):
    s = 1
    for c in src:
        if s == 1 and c=='}':
        s=2
    return s==2
def a_Mas(src):
    s = 1
    for c in src:
        if s == 1 and c == '+':
        s = 2
    return s == 2
def a_Menos(src):
    s = 1
    for c in src:
        if s == 1 and c=='-':
        s = 2
    return s == 2
def a_Por(src):
    s = 1
    for c in src:
        if s == 1 and c == '*':
        s = 2
    return s == 2
def a_Dividido(src):
    s = 1
    for c in src:
        if s == 1 and c=='/':
        s = 2
    return s == 2
def a_Coma(src):
    s = 1
    for c in src:
        if s == 1 and c==',':
            s = 2
    return s == 2
def a_PuntoComa(src):
    s = 1
    for c in src:
        if s == 1 and c == ';':
            s = 2
    return s == 2
def a_PuntoIgual(src):
    s = 1
    for c in src:
        if s == 1 and c ==':=':
            s = 2
    return s == 2
def a_Comparacion(src):
    s = 1
    for c in src:
        if s == 1 and c == '<':
            s = 2
    return s == 2
def a_Comparacion(src):
    s = 1
    for c in src:
        if s == 1 and c == '>':
            s = 2
    return s == 2
 def a_Comparacion(src):
     s = 1
     for c in src:
         if s == 1 and c == '>=':
             s = 2
     return s == 2
def a_Comparacion(src):
    s = 1
    for c in src:
        if s == 1 and c == '<=':
            s = 2
    return s == 2
def a_Comparacion(src):
    s = 1
    for c in src:
        if s == 1 and c == '!=':
            s = 2
    return s == 2
def a_Comparacion(src):
    s = 1
    for c in src:
        if s == 1 and c == '==':
            s = 2
    return s == 2
def a_if(src):
    s=0
    for c in src:
        if s==0 and c=='i':
            s=1
        elif s==1 and c=='f':
            s=2
        else
            s=-1
            break
    return s==2
#esto no tengo ni idea si esta bien lo hice tratando de imitar el del if
def a_for(src):
    s = 0
    for c in src:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c=='o':
            s = 2
        elif s == 2 and c =='r':
            s = 3
        else
            s = -1
            break
    return s == 3
def a_Num(src):
    s=0
    for c in src:
        if s == 0 and c in src:
            s = 1
        if s == 1 and isnum(c)
        else
            s = -1
            break
        return s==1
