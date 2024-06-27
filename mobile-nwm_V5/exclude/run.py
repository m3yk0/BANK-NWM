import argparse
import sys
import subprocess

# Obtem diretório atual:
actual_folder = sys.argv[0]
# Cria objeto argparse:
parser = argparse.ArgumentParser(prog=actual_folder, description='Faça operações com o registro bancário NWM via linha de comando.')
# Variável que pega o nome do progama:
call_prog_name = "%(prog)s"
#Adiciona argumentos:
parser.add_argument('/DEL_SECT', type=str, default='', help='help: /DEL_SECT -sect Sect_Name')
parser.add_argument('-section', type=str, default='none', help='O argumento: "-section section_name" se refe á:'
		' contas={SECTION: {classe: {person: [money, exp]}}}, defines the section of the '
		f'Contas variable, to be mentioned. \nExemplo de uso: "python run.py /DEL_SECT -section reino da folha".')
# Captura os argumentos:
args = parser.parse_args()
print(F"{args.section=}")
parser.print_help()
print(parser)


def execute_instruction(instruction):
    try:
        subprocess.run(instruction, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar a instrução: {e}")

def main():
    parser = argparse.ArgumentParser(description="Processa argumentos da linha de comando")
    parser.add_argument("instrucoes", nargs="+", help="Instruções separadas por '&&'")

    args = parser.parse_args()

    for instrucao in args.instrucoes:
        execute_instruction(instrucao)

