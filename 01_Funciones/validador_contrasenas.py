# Validador de contraseñas
# Reglas: mínimo 8 chars, al menos 1 número, al menos 1 mayúscula
def validador_contrasena():
    def tiene_longitud_minima(password):
        return len(password) >=8
        

    def tiene_numero(password):
        for caracter in password:

            if caracter.isdigit():

                return True

        return False

    def tiene_mayuscula(password):

        for caracter in password:

            if caracter.isupper():

                return True

        return False


    def es_password_segura(password):
        # Combina las tres validaciones...
        return tiene_longitud_minima(password) and tiene_numero(password) and tiene_mayuscula(password)

    pw = input ("Introduce una contraseña ")

    if es_password_segura(pw):
        print("✅ ¡Contraseña segura!")
    else:
        print("❌ Contraseña insegura. Problemas:")
        if not tiene_longitud_minima(pw):
            print(f"  - Muy corta ({len(pw)} chars, mínimo 8)")
        if not tiene_numero(pw):
            print("  - Falta al menos un número")
        if not tiene_mayuscula(pw):
            print("  - Falta al menos una mayúscula")

