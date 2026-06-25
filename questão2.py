def descendentes(arvore):
    if not arvore[1]:
        return[]
    
    return [alguem for filho in arvore[1] for alguem in [filho[0]] + descendentes(filho)]

arv = ( "Maria", [ ("Joana", [ ("Lucio", []),
                               ("Jõao", [])
                             ]
                   ),
                   ("Pedro",[]),
                   ("Patricia", [ ("Marina", [ ("Marcelo", []),
                                               ("Tomás", [])
                                             ]
                                  )
                                ]
                   ),
                   ("Marcos",[])
                 ]
      )

resultado = descendentes(arv)
print(resultado)