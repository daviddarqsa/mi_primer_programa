
apetece_helado_input = input("te apetece un helado? (si / no): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("te he dicho SI / NO, no se que me has dicho pero lo cuento como NO")
    apetece_helado = False

tiene_dinero_input = input("tienes dinero para un helado? (si / no): ").upper()
esta_el_senor_helados_input = input("esta el señor de los helados? (si / no): ").upper()
esta_tu_tia_input = input("estas con tu tia (si / no)").upper()

apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("pues comete uno")
else:
    print("pues no te lo comas")

