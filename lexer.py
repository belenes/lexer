TT = [("<Tipo>","a_int"),
      ("<Tipo>","a_float")
      ("<If>","a_if")
      ("<For>","a_for")
      ("<While>","a_while")
      ("<ParAbierto>","a_(")
      ("<ParCerrado>","a_)")
      ("<LLaAbierta>","a_{")
      ("<LLaCerrada>","a_}")
      ("<+>","a_+")
      ("<->","a_-")
      ("<*>","a_*")
      ("</>","a_/")
      ("<,>","a_,")
      ("<;>","a_;")
      
      
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
        if state == 2:
            state = 0
            i+= 1 
          
      
def calc_candidatos(w):
      candidatos = []
      tipo_token = clasi[0]
        
      
      
def es_aceptada(w):

    candidatos = []

    if len(candidatos)>0:
        return True
    else:
        return False 
