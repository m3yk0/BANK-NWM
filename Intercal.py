#Intercalação entre FUNCS e CONTROLES para evitar ImportError Name Circle dependence.

#transformar valor em decimal:
def decim_fc(valglobal):
	__val__ = str(round(valglobal))
	zeros = "1"
	for c, v in enumerate(__val__):
		zeros = zeros + "0"
	zeros = int(zeros)
	__val__ = int(__val__)
	__new__ = __val__ / zeros
	return __new__
	