grades = []

while True:
    try:
        inp = input("INSIRA A NOTA (ou 'fim'): ").strip().lower()

        if inp == "fim":
            break

        note = float(inp)
        if 0 <= note <= 10:
            grades.append(note)
        else:
            raise ValueError("Nota inválida! (deve ser entre 0 e 10)")

    except ValueError as e:
        print(f"Erro: {e}")

if grades:
    media = sum(grades) / len(grades)
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota inserida.")