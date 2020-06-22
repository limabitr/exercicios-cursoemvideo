#  https://wiki.python.org.br/CoresNoTerminal


""" Padrão ANSI - padrão de normalização internacional
escape sequence: \033[m

How To
\033[style;text;backm

Example: \033[0;33;44m
"""
# ---------------------------------------------------------------------------
# styles: códigos de unidade
"""
0 - none
1 - Bold
4 - Underline
7 - Negative - back se torna text e vice versa
"""
# -----------------------------------------------------------------------
# Dicionário de cores

cores = {  # text colours: 30 a 37

    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'limpa': '\033[m',
    'preto e branco': '\033[7;30;m',

    # cores em negrito

    'branco em negrito': '\033[1;30m',
    'vermelho em negrito': '\033[1;31m',
    'verde em negrito': '\033[1;32m',
    'amarelo em negrito': '\033[1;33m',
    'azul em negrito': '\033[1;34m',
    'roxo em negrito': '\033[1;35m',
    'ciano em negrito': '\033[1;36m',

    # back colours: códigos de 40 a 47

    'fundo branco': '\033[0;30;40m',
    'fundo vermelho': '\033[0;30;41m',
    'fundo verde': '\033[0;30;42m',
    'fundo amarelo': '\033[0;30;43m',
    'fundo azul': '\033[0;30;44m',
    'fundo roxo': '\033[0;30;45m',
    'fundo ciano': '\033[0;30;46m',
    'fundo cinza': '\033[0;30;47m'
}
print('{}Olá mundo{}'.format(cores['branco em negrito'], cores['limpa']))
print(f'\033[1;30;46m{"Olá, mundo!":=^30}\033[m')
