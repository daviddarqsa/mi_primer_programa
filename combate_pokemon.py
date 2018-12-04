
pokemon = input("¿contra que pokemon quieres combatir? (Bulbasaur / Charmander / Squirtle)").upper()


vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0


if pokemon == "Bulbasaur".upper():
    vida_enemigo = 100
    nombre_pokemon = "bulbasaur"
    ataque_pokemon = 30
elif pokemon == "Charmander".upper():
    vida_enemigo = 80
    nombre_pokemon = "charmander"
    ataque_pokemon = 40
elif pokemon == "Squirtle".upper():
    vida_enemigo = 90
    nombre_pokemon = "squirtle"
    ataque_pokemon = 35


while vida_pikachu > 0 and vida_enemigo > 0:
        ataque = input("elige ataque (bola voltio / placaje ), ten en cuenta que si un ataque esta escrito incorrectamente, no se usara.").upper()
        if ataque == ("bola voltio").upper():
            vida_enemigo -= 40
            print("has usado bola voltio, le has bajado 40 de vida")
        elif ataque == ("placaje").upper():
            vida_enemigo -= 30
            print("has usado placaje, le has bajado 30 de vida")
        print("la vida del {} es de {}".format(nombre_pokemon, vida_enemigo))

        vida_pikachu -= ataque_pokemon
        print("{} te hace un ataque de {} de daño, tu vida es de {}".format(nombre_pokemon, ataque_pokemon, vida_pikachu))


if vida_enemigo <= 0:
    print("has ganado!")
if vida_pikachu <= 0:
    print("has perdido!")

print("El combate ha terminado")








