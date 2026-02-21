
def potencias_factores(factores):
    potencias = {}
    for f in factores:
        if f not in potencias:
            potencias[f] = 1
        else:
            potencias[f] += 1
    return potencias