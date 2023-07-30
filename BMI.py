#!/usr/bin/env python
print("""         ______ ___  ___ _____       ______             _                        
         | ___ \|  \/  ||_   _|      | ___ \           | |                       
         | |_/ /| .  . |  | | ______ | |_/ / ___   ___ | |__   _ __    ___  _ __ 
         | ___ \| |\/| |  | ||______||    / / _ \ / __|| '_ \ | '_ \  / _ \| '__|
         | |_/ /| |  | | _| |_       | |\ \|  __/| (__ | | | || | | ||  __/| |   
         \____/ \_|  |_/ \___/       \_| \_|\___| \___||_| |_||_| |_| \___||_|   
         
Herzlich Willkommen zum BMI-Rechner von Al3xxx84!""")
print("")
print("""Die Informationen dieses Programms dürfen auf keinen Fall als Ersatz für professionelle Beratung oder Behandlung durch ausgebildete und anerkannte Ärzte angesehen werden. Der Inhalt von BMI-Rechner kann und darf nicht verwendet werden, um eigenständig Diagnosen zu stellen oder Behandlungen anzufangen.""")
print("")
print("Mithilfe des Body-Mass-Index (BMI) beurteilen Mediziner, ob jemand Normalgewicht, Unter- oder Übergewicht hat. Der BMI drückt aus, in welchem Verhältnis das Körpergewicht eines Menschen zu seiner Größe steht.Der Body-Mass-Index hat große Bedeutung als Indikator für Übergewicht und Fettleibigkeit. Grundsätzlich ist seine Aussagekraft aber in verschiedener Hinsicht eingeschränkt.Sehr muskulöse Menschen (Bodybuilder) haben z.B. oft auch einen höheren BMI, sind aber nicht zu dick.")
print("")

Gewicht = input("Bitte Gewicht in Kilogramm angeben:")
Größe = input("Bitte Körpergröße in Metern angeben, z.B. 1.75: ")
Quadrat = float(Größe) * float(Größe)
BMI = float(Gewicht) / float(Quadrat)
print("")

print("Ihr BMI beträgt: " + str(BMI))

if BMI < 18.5:
    print("""Sie haben Untergewicht.
    
Untergewicht kann viele Ursachen haben. Manchmal liegt ein niedriges Körpergewicht schlicht in der Familie.In anderen Fällen stecken etwa Stress, Erkrankungen oder Essstörungen dahinter. Medizinisch relevant wird zu geringes Gewicht, wenn damit Mangelerscheinungen verbunden sind.""")

elif BMI <24.9:
    print("Sehr gut, sie haben Normalgewicht!")

elif BMI < 29.9:
    print("""Sie haben übergewicht!
    
In den sogenannten Industrienationen ist Übergewicht ein wachsendes Gesundheitsproblem. In Deutschland ist bereits mehr als die Hälfte aller Erwachsenen übergewichtig. Auch viele Kinder bringen übermäßig viele Kilos auf die Waage. Übergewicht verursacht unterschiedliche Beschwerden und begünstigt die Entwicklung chronischer Krankheiten.""")

elif BMI < 34.9:
    print("""Sie sind krankhaft fettleibig (Adipositas Grad I)!
    
Von Adipositas spricht man bei starkem Übergewicht, das schädlich für die Gesundheit ist. Adipositas ist eine chronische Krankheit, die mit eingeschränkter Lebensqualität und hohem Risiko für Folgeerkrankungen einhergeht. Betroffene leiden nicht nur unter den körperlichen Folgen, sondern auch unter Stigmatisierung durch die Umwelt. """)

elif BMI < 39.9:
    print("""Sie sind krankhaft fettleibig (Adipositas Grad II)!
    
Von Adipositas spricht man bei starkem Übergewicht, das schädlich für die Gesundheit ist. Adipositas ist eine chronische Krankheit, die mit eingeschränkter Lebensqualität und hohem Risiko für Folgeerkrankungen einhergeht. Betroffene leiden nicht nur unter den körperlichen Folgen, sondern auch unter Stigmatisierung durch die Umwelt. """)

elif BMI > 40:
    print("""Sie sind extrem fettleibig (Adipositas permagna)!
    
Unter Adipositas permagna (lat. permagnus = riesig, sehr groß) versteht man die schwerste Form der Adipositas. Menschen mit Adipositas permagna sind stark übergewichtig und riskieren schwere gesundheitliche Folgen, wenn die Krankheit längere Zeit besteht und sie keine Gewichtsnormalisierung erreichen.
    
Bitte suchen Sie sich schnellstmöglich medizinische Hilfe.""")

else:
    print("Error!")

print("")
print("Vielen Dank für die Benutzung des BMI-Rechners von Al3XXX84")
print("")

input("Zum Beenden bitte belibige Taste drücken")
