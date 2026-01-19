

class Usuario:
    def __init__(self, username, email, password):
        self.username = username,
        self.email = email,
        self.__password = password,
        self.lista_mascotas = [],
        self.signed_in = False

    def sing_in(self, email, password):
        if self.email == email and self.__password == password:
            self.signed_in = True
            return True
        return False

    def sing_out(self):
        self.signed_in = False

    '''
    def agregar_mascota(self, mascota: Mascota):
        self.lista_mascotas.append(mascota)
    '''
