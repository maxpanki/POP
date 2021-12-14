




class Data:

    #Student [Id, Imie, Nazwisko, TypStudiow, NiedostepneTerminy, OpiekunId]
    STUDENCI [
        [1, "Karol", "Krajewski", "Inż", [["23-02-2022 11-12"]], 4],
        [2, "Aureliusz", "Malinowski", "Inż", [["15-02-2022 10-12"]], 31],
        [3, "Ida", "Zakrzewska", "Inż", [["14-02-2022 10-13"]], 36],
        [4, "Maciej", "Wróblewski", "Inż", [], 39],
        [5, "Dorian", "Brzeziński", "Inż", [["14-02-2022 10-12"], ["17-02-2022 14-15"]], 16],
        [6, "Zofia", "Mazur", "Inż",[["25-02-2022 13-15"]], 19],
        [7, "Oktawian", "Andrzejewski", "Inż", [["21-02-2022 11-12"]], 6],
        [8, "Dorota", "Szewczyk", "Inż", [["25-02-2022 10-13"]], 26],
        [9, "Przemysław", "Błaszczyk", "Inż", [], 23],
        [10, "Korneliusz", "Sobczak", "Inż", [["17-02-2022 11-15"]], 24],
        [11, "Gustaw", "Zakrzewski", "Inż", [["18-02-2022 10-11"]], 7],
        [12, "Alan", "Laskowski", "Inż", [["14-02-2022 11-12"]], 18],
        [13, "Ryszard", "Ostrowski", "Inż", [["25-02-2022 12-13"]], 30],
        [14, "Albert", "Szczepański", "Inż", [], 17],
        [15, "Emil","Zieliński", "Inż", [["21-02-2022 11-12"]], 11],
        [16, "Aureliusz", "Baranowski", "Inż", [["25-02-2022 10-12"]], 12],
        [17, "Hubert", "Michalak", "Inż", [], 25],
        [18, "Olgierd", "Kowalski", "Inż", [["16-02-2022 14-15"]], 37],
        [19, "Fabian", "Lewandowski", "Inż", [], 20],
        [20, "Leonardo", "Ostrowski", "Inż", [["23-02-2022 11-12"], ["24-02-2022 13-15"]], 3],
        [21, "Juliusz", "Ziółkowski", "Mag", [["21-02-2022 14-15"]], 18],
        [22, "Konrad", "Zalewski", "Mag", [["22-02-2022 13-15"]], 34],
        [23, "Ola", "Mróz", "Magister", [["19-02-2022 10-13"]], 28],
        [24, "Dorian", "Andrzejewski", "Mag", [["17-02-2022 11-12"]], 13],
        [25, "Maja", "Szulc", "Mag", [["24-02-2022 10-12"]], 19],
        [26, "Aureliusz", "Jaworski", "Mag", [["21-02-2022 12-15"]], 37],
        [27, "Borys", "Wysocki", "Mag", [["17-02-2022 10-11"]], 2],
        [28, "Agnieszka", "Szymczak", "Mag", [["23-02-2022 14-15"]], 29],
        [29, "Józef", "Błaszczyk","Mag", [], 32],
        [30, "Maurycy", "Zalewski", "Mag", [["16-02-2022 11-12"]], 33]
    ]
    
    #Pracownik [Id, Imie, Nazwisko, Role, WolneTerminy]
    Pracownicy [
        [1, "Ksawery", "Chmielewski", [["Przewodniczący"],["Recenzent"],["Członek komisji"]], [[15-02-2022 10-15]]],
        [2, "Ola", "Szymczak", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[21-02-2022 10-15],[24-02-2022 10-15],[25-02-2022 10-15]]],
        [3, "Gabriel", "Marciniak", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[17-02-2022 10-15],[18-02-2022 10-15]]],
        [4, "Natan", "Jakubowski", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[14-02-2022 10-15],[22-02-2022 10-15]]],
        [5, "Adrian", "Malinowski", [["Recenzent"],["Członek komisji"]], [[15-02-2022 10-15],[18-02-2022 10-15],[22-02-2022 10-15]]],
        [6, "Daria", "Woźniak", [["Przewodniczący"],["Recenzent",],["Członek komisji"],["Opiekun"]], [[14-02-2022 10-15],[21-02-2022 10-15]]],
        [7, "Marcin", "Sikora", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[16-02-2022 10-15],[17-02-2022 10-15],[23-02-2022 10-15]]],
        [8, "Elżbieta", "Zawadzka", [["Recenzent"],["Członek komisji"]], [[22-02-2022 10-15],[23-02-2022 10-15]] ],
        [9, "Miron", "Stępień", [["Przewodniczący"],["Recenzent"],["Członek komisji"]], [[14-02-2022 10-15],[18-02-2022 10-15]]],
        [10, "Zuzanna", "Mazur", [["Recenzent"],["Członek komisji"]], [[18-02-2022 10-15],[21-02-2022 10-15],[25-02-2022 10-15]]],
        [11, "Radosław", "Makowski", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[15-02-2022 10-15],[22-02-2022 10-15],[25-02-2022 10-15]]],
        [12, "Artur", "Kaźmierczak", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[14-02-2022 10-15],[16-02-2022 10-15]]],
        [13, "Dorota", "Błaszczyk", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[23-02-2022 10-15],[24-02-2022 10-15]]],
        [14, "Eryk", "Lis", [["Przewodniczący"],["Recenzent"],["Członek komisji"]], [[16-02-2022 10-15]]],
        [15, "Urszula", "Jasińska", [["Recenzent"],["Członek komisji"]], [[18-02-2022 10-15],[21-02-2022 10-15],[22-02-2022 10-15]]],
        [16, "Dawid", "Gajewski", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[18-02-2022 10-15],[22-02-2022 10-15],[24-02-2022 10-15]]],
        [17, "Emil", "Mróz", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[14-02-2022 10-15],[17-02-2022 10-15],[21-02-2022 10-15]]],
        [18, "Henryk", "Wójcik", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[16-02-2022 10-15],[21-02-2022 10-15]]],
        [19, "Izabela", "Lis", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[17-02-2022 10-15],[22-02-2022 10-15],[23-02-2022 10-15]]],
        [20, "Julia", "Chmielewska", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[17-02-2022 10-15],[18-02-2022 10-15],[24-02-2022 10-15]]],
        [21, "Alan", "Przybylski", [["Przewodniczący"],["Recenzent"],["Członek komisji"]], [[19-02-2022 10-15],[24-02-2022 10-15]]],
        [22, "Lidia", "Marciniak", [["Recenzent"],["Członek komisji"]], [[17-02-2022 10-15],[18-02-2022 10-15]]],
        [23, "Ida", "Adamska", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[14-02-2022 10-15],[15-02-2022 10-15],[23-02-2022 10-15]]],
        [24, "Adrian", "Wójcik", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[16-02-2022 10-15],[21-02-2022 10-15],[22-02-2022 10-15]]],
        [25, "Maja", "Kucharska", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[16-02-2022 10-15],[22-02-2022 10-15]]],
        [26, "Adrian", "Lis", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[15-02-2022 10-15],[17-02-2022 10-15],[18-02-2022 10-15]]],
        [27, "Leszek", "Kowalski", [["Przewodniczący"],["Recenzent"],["Członek komisji"]], [[23-02-2022 10-15],[25-02-2022 10-15]]],
        [28, "Elżbieta", "Tomaszewska", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[15-02-2022 10-15],[18-02-2022 10-15],[24-02-2022 10-15]]],
        [29, "Aleksandra", "Sawicka", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[15-02-2022 10-15],[17-02-2022 10-15]]],
        [30, "Igor", "Krawczyk", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[18-02-2022 10-15],[21-02-2022 10-15],[22-02-2022 10-15]]],
        [31, "Jolanta", "Walczak", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[19-02-2022 10-15],[24-02-2022 10-15],[25-02-2022 10-15]]],
        [32, "Kewin", "Jakubowski", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[14-02-2022 10-15],[16-02-2022 10-15]]],
        [33, "Alek", "Kubiak", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[21-02-2022 10-15],[23-02-2022 10-15]],
        [34, "Zofia", "Wiśniewska", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[19-02-2022 10-15],[21-02-2022 10-15],[24-02-2022 10-15]],
        [35, "Honorata", "Zawadzka", [["Recenzent"],["Członek komisji"]], [[16-02-2022 10-15],[17-02-2022 10-15],[25-02-2022 10-15]],
        [36, "Wioletta", "Stępień", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[15-02-2022 10-15],[23-02-2022 10-15]],
        [37, "Antoni", "Czarnecki", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[22-02-2022 10-15],[23-02-2022 10-15],[24-02-2022 10-15]]],
        [38, "Janusz", "Krupiński", [["Przewodniczący"],["Recenzent"],["Członek komisji"]], [[17-02-2022 10-15]]],
        [39, "Żaneta", "Kamińska", [["Recenzent"],["Członek komisji"], ["Opiekun"]], [[14-02-2022 10-15],[21-02-2022 10-15]]],
        [40, "Bogusława", "Maciejewska", [["Recenzent"],["Członek komisji"]], [[15-02-2022 10-15],[17-02-2022 10-15],[25-02-2022 10-15]]]
    ] 
