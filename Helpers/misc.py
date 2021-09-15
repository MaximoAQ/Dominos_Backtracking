def verify(pPair, pList):
    if(pPair in pList):
        return True
    else:
        pPair[0], pPair[1] = pPair[1], pPair[0]
        return pPair in pList