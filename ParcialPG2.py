class Persona:
    def __init__(self, nombre, apellido, direccion, telefono, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad
        self.email = email

    

class Empleado(Persona):
    def __init__(self, nombre, apellido, direccion, telefono, edad, email, salario, jefe, añoExperiencia):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self.salario = salario
        self.jefe = jefe
        self.añoExperiencia = añoExperiencia
        self.cargo = self.calcular_cargo()

    
    def calcular_cargo(self):
        if self.salario >= 5000000 and self.añoExperiencia >= 5 and 25 <= self.edad <= 45:
            return "Senior"
        elif 900000 <= self.salario <= 1200000 and 1 <= self.añoExperiencia <= 2 and 18 <= self.edad <= 22:
            return "Junior"
        else:
            return "Intermedio"  
    def __str__(self):
        return (f"\nDetalles del Empleado:\n"
                f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"Dirección: {self.direccion}\n"
                f"Teléfono: {self.telefono}\n"
                f"Edad: {self.edad}\n"
                f"Email: {self.email}\n"
                f"Salario: ${self.salario}\n"
                f"Jefe Inmediato: {self.jefe}\n"
                f"Años de Experiencia: {self.añoExperiencia}\n"
                f"Cargo: {self.cargo}")

def obtener_datos():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    edad = int(input("Ingrese la edad: "))
    email = input("Ingrese el email: ")
    salario = float(input("Ingrese el salario: "))
    jefe = input("Ingrese el jefe inmediato: ")
    añoExperiencia = int(input("Ingrese los años de experiencia: "))
    return nombre, apellido, direccion, telefono, edad, email, salario, jefe, añoExperiencia

nombre, apellido, direccion, telefono, edad, email, salario, jefe, añoExperiencia = obtener_datos()

empleado = Empleado(nombre, apellido, direccion, telefono, edad, email, salario, jefe, añoExperiencia)

print(empleado)
