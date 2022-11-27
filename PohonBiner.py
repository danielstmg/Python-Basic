# Pembuat   : Daniel Sahat Parulian Situmeang
# Tanggal   : 29 November 2020
# Deskripsi : Tugas Daspro Pohon Biner

class PohonBiner:
    def __init__(self,A,L,R):
        self.A = A
        self.L = L
        self.R = R

def MakePB(A,L,R):
    return PohonBiner(A,L,R)

def Akar(P):
    return P.A

def Left(P):
    return P.L

def Right(P):
    return P.R

def IsTreeEmpty(P):
    if (P == None):
        return True
    else:
        return False

def IsOneElementPB(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))):
        return True
    else:
        return False

def IsUnerLeftPB(P):
    if (not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
        return True
    else:
        return False

def IsUnerRightPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))):
        return True
    else:
        return False

def IsExistLeftPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Left(P))):
        return True
    else:
        return False

def IsExistRightPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P))):
        return True
    else:
        return False

def IsBinerPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
        return True
    else:
        return False

def NbElement(P):
    if IsTreeEmpty(P):
        return 0
    else:
        return NbElement(Left(P)) + 1 + NbElement(Right(P))

def NbDaunPB(P):
    if IsOneElementPB(P):
        return 1
    elif IsBinerPB(P):
        return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
    elif IsUnerLeftPB(P):
        return NbDaunPB(Left(P))
    elif IsUnerRightPB(P):
        return NbDaunPB(Right(P))

def RepPrefixPB(P):
	if(IsOneElementPB(P)):
		return [Akar(P)]
	else:
		if(IsBinerPB(P)):
			return [Akar(P)] + RepPrefixPB(Left(P)) + RepPrefixPB(Right(P))
		elif(IsUnerLeftPB(P)):
			return [Akar(P)] + RepPrefixPB(Left(P))
		elif(IsUnerRightPB(P)):
			return [Akar(P)] + RepPrefixPB(Right(P))

P1 = MakePB(1,
			MakePB(
				2,
				None,
				None
			),
			MakePB(
				3,
				MakePB(
					4,
					None,
					MakePB(
						5,
						None,
						None
					)
				),
				None
			)
		)

P2 = MakePB(
		"^",
		MakePB(
			"*",
			MakePB(
				"+",
				MakePB(
					"2",
					None,
					None
				),
				MakePB(
					"5",
					None,
					None
				)
			),
			MakePB(
				"/",
				MakePB(
					"12",
					None,
					None
				),
				MakePB(
					"25",
					None,
					None
				)
			),
		),
		MakePB(
			"10",
			None,
			None
		)
	)

print(NbElement(P1))
print(NbDaunPB(P2))
print(RepPrefixPB(P1))
print(IsBinerPB(P1))
print(IsUnerLeftPB(P2))
print(IsUnerRightPB(P2))
