# BANK-NWM
Sistema bancário e financeiro para o N.W.M-RPG. 


"""
READ-ME:
    \nVersão: {versao}
    
    \nv 1.2.3 = controles: adicionado classes dentro de cada seção.
    
    \nv 1.2.1 = código "Funcs", separado do código "Banco". Uso por import
    v 1.2.0 = código "controles" separado do codigo "Banco" (uso por import)
    v 1.1.9 = var mundial lideres
    v 1.1.8 = var mundial reinantes
    v 1.1.7 = data_reg virou var global
    v 1.1.6 = Operação numero 3 desligada.
    v 1.1.5 = Ao invés de reinos, as contas são separadas pelo nome "seções".
    v 1.1.4 = def valores adicionado taxa silic
    v 1.1.3 = def valores adicionado meta silic
    v 1.1.2 = def individuos e registros reformados
    v 1.1.1 = def reinos
    v 1.1.0 = Adicionado "reinos" em contas
    v 1.0.0 = Escolher registro antigo, como um principal (ctrl+z)
    v 0.2.9 = Agora não é mais possível um indivíduo negativado, realziar transferências bancárias.
    v 0.2.8 = Bug de seleção de indivpiduos, corrigido
    v 0.2.7 = Melhorias (nomes, váriaveis, contas.copy, etc)
    v 0.2.6 = Corrigido bugs de Backup
    v 0.2.5 = Melhorias (money de INT foi para FLOAT (2 casas) e EXP 1 casa), nome de vars mudados para sem acentos, algumas instruções PEP8 seguidas.
    v 0.2.4 = Corrigido bugs na operacao 3
    v 0.2.3 = Bloqueio de operacoes
    v 0.2.2 = def confirm()
    v 0.2.1 = def ver registros antigos
    v 0.2.0 = histórico de funções escolhidas pelo usuário
    v 0.1.9 = Func. individuos()
    v 0.1.8 = corrigindo func 'alternativa()'
    v 0.1.7 = correção de bugs
    v 0.1.6 = voltado base 0.1.4 + incrementos de função 'alternativa()' em cada funcao 
    v 0.1.5 = cada alternativa = funcão
    v 0.1.4 = correção de português
    -
    v 0.1.1 = Opção 6 foi fechada (opc 1 já cumpria tal funcão)
    v 0.1.2 = programa aninhado em def main() 
    v 0.1.3 = def confirm_input()

    vars. constantes são em MAIUSCULO
    vars. function em minusculo
    classes em Titled (sem underlines)
    >>> Todo código de operação é separado em 2 comentários:
    #-- CÓDIGO --# == área do código
    #-- FLAG --# == área da finalização bem-sucedida do código.
        Em flag, sempre deve haver:
        del váriaveis usadas na operação
        end = z = True == representa que a operação foi finalizada 
        # end = TRUE == finalizado com sucesso
        # end = FALSE == finalizado com falha entre a operação
        # end = NONE = Operação em estado aberto/não finalizada.
        historico.append([f"Concluído funcão {i}, para o registro {dic_reg}, as {data_atual}",
                                      "desc: DESCRIÇÃO DA FUNÇÃO."])
"""
