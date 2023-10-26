class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    def __str__(self):
        return f"Nombre: {self.nombre}, Telefono: {self.telefono}, Correo: {self.correo}"
    

class Libreta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contactos = {}

    def add(self, contacto):
        if contacto.nombre not in self.contactos:
            self.contactos[contacto.nombre] = contacto
            return True
        return False

    def __str__(self):
        cad = f"Nombre: {self.nombre}, Contactos: \n"
        for nombre, contacto in self.contactos.items():
            cad += str(contacto) + "\n"
        return cad

    def __len__(self):
        return len(self.contactos)

    def delete(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            return True
        return False

    def update(self, contacto):
        if contacto.nombre in self.contactos:
            self.contactos[contacto.nombre] = contacto
            return True
        return False

    def find(self, nombre):
        return self.contactos.get(nombre, None)
