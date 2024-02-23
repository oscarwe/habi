def get_input_array(length):
    """
    Solicita al usuario ingresar un array de longitud ya establecida
    """
    print("Use 0 para marcar el final de un bloque")
    my_array = []
    for i in range(length):
        while True:
            number = int(input(f"Número {i + 1}: "))
            if number < 0 or number > 9:
                print("El número debe estar en el rango de 1 a 9")
            else:
                my_array.append(number)
                break
    return my_array

def sort_and_print_sequences(array):
    """
    Ordena los números en cada bloque del array y los imprime como secuencias.
    """
    sequences = []
    block = []
    for num in array:
        if num == 0:
            sequences.append(''.join(sorted(block))) if block else sequences.append('X')
            block = []
        else:
            block.append(str(num))
    if block:
        sequences.append(''.join(sorted(block))) if block else sequences.append('X')
    print(' '.join(sequences))

def main():
    length = int(input("Ingrese la longitud del arreglo: "))
    if length > 0:
        my_array = get_input_array(length)
        if my_array:
            sort_and_print_sequences(my_array)
    else:
        print('Longitud no valida')

if __name__ == "__main__":
    main()