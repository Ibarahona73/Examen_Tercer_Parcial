#Primer ejercicio
#Ivan Barahona
#201930010221 Examen de tercer parcial


import csv

# Clase Persona
class Persona:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.salario = float(salario)
        self.deducciones = float(deducciones)
        self.genero = genero

    def __repr__(self):
        return f"{self.nombre}, {self.apellido}, {self.edad} años, {self.salario} salario, {self.deducciones} deducciones, {self.genero}"

# Clase GestorCSV
class GestorCSV:
    def __init__(self):
        self.personas = []

    def leer_archivo(self, archivo):
        # Leer el archivo CSV y crear instancias de Persona
        with open(archivo, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera línea (encabezados)
            for row in reader:
                persona = Persona(*row)  # Desempaquetar la lista de valores en los atributos de la clase Persona
                self.personas.append(persona)

    def persona_mayor_edad(self):
        # Encontrar la persona con mayor edad
        mayor = self.personas[0]
        for persona in self.personas[1:]:
            if persona.edad > mayor.edad:
                mayor = persona
        return mayor

    def persona_menor_edad(self):
        # Encontrar la persona con menor edad
        menor = self.personas[0]
        for persona in self.personas[1:]:
            if persona.edad < menor.edad:
                menor = persona
        return menor

    def contar_generos(self):
        # Contar el número de hombres y mujeres
        hombres = mujeres = 0
        for persona in self.personas:
            if persona.genero == 'Masculino':
                hombres += 1
            elif persona.genero == 'Femenino':
                mujeres += 1
        return {'Hombres': hombres, 'Mujeres': mujeres}

    def promedio_salario(self):
        # Calcular el promedio de salario
        total_salario = sum([persona.salario for persona in self.personas])
        return total_salario / len(self.personas)

    def persona_mas_deducciones(self):
        # Encontrar la persona con más deducciones
        max_deducciones = self.personas[0]
        for persona in self.personas[1:]:
            if persona.deducciones > max_deducciones.deducciones:
                max_deducciones = persona
        return max_deducciones

    def persona_mayor_salario(self):
        # Encontrar la persona con mayor salario
        max_salario = self.personas[0]
        for persona in self.personas[1:]:
            if persona.salario > max_salario.salario:
                max_salario = persona
        return max_salario

# Implementación del programa
def main():
    gestor = GestorCSV()
    gestor.leer_archivo('datos.csv')

    # Encontrar la persona con la mayor edad
    print("Persona con mayor edad:", gestor.persona_mayor_edad())

    # Encontrar la persona con la menor edad
    print("Persona con menor edad:", gestor.persona_menor_edad())

    # Contar el número de mujeres y hombres
    generos = gestor.contar_generos()
    print("Número de hombres:", generos['Hombres'])
    print("Número de mujeres:", generos['Mujeres'])

    # Calcular el promedio de salario
    print("Promedio de salario:", gestor.promedio_salario())

    # Identificar a la persona con más deducciones
    print("Persona con más deducciones:", gestor.persona_mas_deducciones())

    # Identificar a la persona que gana más
    print("Persona que gana más:", gestor.persona_mayor_salario())

if __name__ == "__main__":
    main()

#Copyright 2024 Ivan Barahona