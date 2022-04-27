from graph import Graph
import sys

def main():
    args = sys.argv[1:]
    input_path = output_path = ''

    for i in range(0, len(args), 2):
        if args[i] == '-i' or args[i] == '--input':
            input_path = args[i + 1]
        elif args[i] == '-o' or args[i] == '--output':
            output_path = args[i + 1]
        else:
            print(f'Error: Argumento "{args[i]}" inválido')
            exit(1)
    
    if input_path == '' or output_path == '':
        print('Error: Faltan argumentos, por favor ingrese -i o --input y -o o --output')
        exit(1)

    # Importa el archivo a procesar
    input_file = open(input_path, "r") 
    text = ''
    if input_file:
        text = input_file.read()
    print(text.split('\n'))

if __name__ == "__main__":
    main()