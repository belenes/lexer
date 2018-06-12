TT = [("<Tipo>","int"),
      ("<Tipo>","float")
      ("<If>","if")
      ("<For>","for")
      ("<While>","while")
      ("<>","")
      ("<>","")
      ("<>","")
      ("<>","")
      ("<>","")
      ("<>","")
      
      
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
