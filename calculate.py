import csv

def readDepth():
    count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10, \
    count11, count12, count13, count14, count15, count16, count17, count18, count19, count20, \
    count21, count22, count23, count24, count25, count26, count27, count28, count29, count30, \
    count31, count32, count33, count34, count35, count36, count37, count38, count39, count40, \
    count41, count42, count43, count44, count45, count46, count47, count48, count49, count50, \
    count51, count52, count53, count54, count55 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0
    total0, total1, total2, total3, total4, total5, total6, total7, total8, total9, total10, \
    total11, total12, total13, total14, total15, total16, total17, total18, total19, total20, \
    total21, total22, total23, total24, total25, total26, total27, total28, total29, total30, \
    total31, total32, total33, total34, total35, total36, total37, total38, total39, total40, \
    total41, total42, total43, total44, total45, total46, total47, total48, total49, total50, \
    total51, total52, total53, total54, total55 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
                                                  0, 0, 0, 0, 0, 0, 0, 0, 0
    county = ["Beaverhead", "Big Horn", "Blaine", "Broadwater", "Carbon", "Carter", "Cascade", "Chouteau", "Custer",
              "Daniels", "Dawson", "Deer Lodge", "Fallon", "Fergus", "Flathead", "Gallatin", "Garfield", "Glacier",
              "Golden Valley", "Granite", "Hill", "Jefferson", "Judith Basin", "Lake", "Lewis and Clark", "Liberty",
              "Lincoln", "Madison", "McCone", "Meagher", "Mineral", "Missoula", "Musselshell", "Park", "Petroleum",
              "Phillips", "Pondera", "Powder River", "Powell", "Prairie", "Ravalli", "Richland", "Roosevelt", "Rosebud",
              "Sanders", "Sheridan", "Silver Bow", "Stillwater", "Sweet Grass", "Teton", "Toole", "Treasure", "Valley",
              "Wheatland", "Wibaux", "Yellowstone"]

    with open("Snow Depth, May 2, 2022, end of day.csv", newline="") as csvfile:
        snowreader = csv.DictReader(csvfile)
        for row in snowreader:
            if row["State"] == "Montana":
                try:
                    if row["County"] == county[0]:
                        count0 += 1
                        snowDepth = (row["Value_inches"])
                        total0 = int(snowDepth) + total0
                except:
                    pass
                try:
                    if row["County"] == county[1]:
                        count1 += 1
                        snowDepth = (row["Value_inches"])
                        total1 = int(snowDepth) + total1
                except:
                    pass
                try:
                    if row["County"] == county[2]:
                        count2 += 1
                        snowDepth = (row["Value_inches"])
                        total2 = int(snowDepth) + total2
                except:
                    pass
                try:
                    if row["County"] == county[3]:
                        count3 += 1
                        snowDepth = (row["Value_inches"])
                        total3 = int(snowDepth) + total3
                except:
                    pass
                try:
                    if row["County"] == county[4]:
                        count4 += 1
                        snowDepth = (row["Value_inches"])
                        total4 = int(snowDepth) + total4
                except:
                    pass
                try:
                    if row["County"] == county[5]:
                        count5 += 1
                        snowDepth = (row["Value_inches"])
                        total5 = int(snowDepth) + total5
                except:
                    pass
                try:
                    if row["County"] == county[6]:
                        count6 += 1
                        snowDepth = (row["Value_inches"])
                        total6 = int(snowDepth) + total6
                except:
                    pass
                try:
                    if row["County"] == county[7]:
                        count7 += 1
                        snowDepth = (row["Value_inches"])
                        total7 = int(snowDepth) + total7
                except:
                    pass
                try:
                    if row["County"] == county[8]:
                        count8 += 1
                        snowDepth = (row["Value_inches"])
                        total8 = int(snowDepth) + total8
                except:
                    pass
                try:
                    if row["County"] == county[9]:
                        count9 += 1
                        snowDepth = (row["Value_inches"])
                        total9 = int(snowDepth) + total9
                except:
                    pass
                try:
                    if row["County"] == county[10]:
                        count10 += 1
                        snowDepth = (row["Value_inches"])
                        total10 = int(snowDepth) + total10
                except:
                    pass
                try:
                    if row["County"] == county[11]:
                        count11 += 1
                        snowDepth = (row["Value_inches"])
                        total11 = int(snowDepth) + total11
                except:
                    pass
                try:
                    if row["County"] == county[12]:
                        count12 += 1
                        snowDepth = (row["Value_inches"])
                        total12 = int(snowDepth) + total12
                except:
                    pass
                try:
                    if row["County"] == county[13]:
                        count13 += 1
                        snowDepth = (row["Value_inches"])
                        total13 = int(snowDepth) + total13
                except:
                    pass
                try:
                    if row["County"] == county[14]:
                        count14 += 1
                        snowDepth = (row["Value_inches"])
                        total14 = int(snowDepth) + total14
                except:
                    pass
                try:
                    if row["County"] == county[15]:
                        count15 += 1
                        snowDepth = (row["Value_inches"])
                        total15 = int(snowDepth) + total15
                except:
                    pass
                try:
                    if row["County"] == county[16]:
                        count16 += 1
                        snowDepth = (row["Value_inches"])
                        total16 = int(snowDepth) + total16
                except:
                    pass
                try:
                    if row["County"] == county[17]:
                        count17 += 1
                        snowDepth = (row["Value_inches"])
                        total17 = int(snowDepth) + total17
                except:
                    pass
                try:
                    if row["County"] == county[18]:
                        count18 += 1
                        snowDepth = (row["Value_inches"])
                        total18 = int(snowDepth) + total18
                except:
                    pass
                try:
                    if row["County"] == county[19]:
                        count19 += 1
                        snowDepth = (row["Value_inches"])
                        total19 = int(snowDepth) + total19
                except:
                    pass
                try:
                    if row["County"] == county[20]:
                        count20 += 1
                        snowDepth = (row["Value_inches"])
                        total20 = int(snowDepth) + total20
                except:
                    pass
                try:
                    if row["County"] == county[21]:
                        count21 += 1
                        snowDepth = (row["Value_inches"])
                        total21 = int(snowDepth) + total21
                except:
                    pass
                try:
                    if row["County"] == county[22]:
                        count22 += 1
                        snowDepth = (row["Value_inches"])
                        total22 = int(snowDepth) + total22
                except:
                    pass
                try:
                    if row["County"] == county[23]:
                        count23 += 1
                        snowDepth = (row["Value_inches"])
                        total23 = int(snowDepth) + total23
                except:
                    pass
                try:
                    if row["County"] == county[24]:
                        count24 += 1
                        snowDepth = (row["Value_inches"])
                        total24 = int(snowDepth) + total24
                except:
                    pass
                try:
                    if row["County"] == county[25]:
                        count25 += 1
                        snowDepth = (row["Value_inches"])
                        total25 = int(snowDepth) + total25
                except:
                    pass
                try:
                    if row["County"] == county[26]:
                        count26 += 1
                        snowDepth = (row["Value_inches"])
                        total26 = int(snowDepth) + total26
                except:
                    pass
                try:
                    if row["County"] == county[27]:
                        count27 += 1
                        snowDepth = (row["Value_inches"])
                        total27 = int(snowDepth) + total27
                except:
                    pass
                try:
                    if row["County"] == county[28]:
                        count28 += 1
                        snowDepth = (row["Value_inches"])
                        total28 = int(snowDepth) + total28
                except:
                    pass
                try:
                    if row["County"] == county[29]:
                        count29 += 1
                        snowDepth = (row["Value_inches"])
                        total29 = int(snowDepth) + total29
                except:
                    pass
                try:
                    if row["County"] == county[30]:
                        count30 += 1
                        snowDepth = (row["Value_inches"])
                        total30 = int(snowDepth) + total30
                except:
                    pass
                try:
                    if row["County"] == county[31]:
                        count31 += 1
                        snowDepth = (row["Value_inches"])
                        total31 = int(snowDepth) + total31
                except:
                    pass
                try:
                    if row["County"] == county[32]:
                        count32 += 1
                        snowDepth = (row["Value_inches"])
                        total32 = int(snowDepth) + total32
                except:
                    pass
                try:
                    if row["County"] == county[33]:
                        count33 += 1
                        snowDepth = (row["Value_inches"])
                        total33 = int(snowDepth) + total33
                except:
                    pass
                try:
                    if row["County"] == county[34]:
                        count34 += 1
                        snowDepth = (row["Value_inches"])
                        total34 = int(snowDepth) + total34
                except:
                    pass
                try:
                    if row["County"] == county[35]:
                        count35 += 1
                        snowDepth = (row["Value_inches"])
                        total35 = int(snowDepth) + total35
                except:
                    pass
                try:
                    if row["County"] == county[36]:
                        count36 += 1
                        snowDepth = (row["Value_inches"])
                        total36 = int(snowDepth) + total36
                except:
                    pass
                try:
                    if row["County"] == county[37]:
                        count37 += 1
                        snowDepth = (row["Value_inches"])
                        total37 = int(snowDepth) + total37
                except:
                    pass
                try:
                    if row["County"] == county[38]:
                        count38 += 1
                        snowDepth = (row["Value_inches"])
                        total38 = int(snowDepth) + total38
                except:
                    pass
                try:
                    if row["County"] == county[39]:
                        count39 += 1
                        snowDepth = (row["Value_inches"])
                        total39 = int(snowDepth) + total39
                except:
                    pass
                try:
                    if row["County"] == county[40]:
                        count40 += 1
                        snowDepth = (row["Value_inches"])
                        total40 = int(snowDepth) + total40
                except:
                    pass
                try:
                    if row["County"] == county[41]:
                        count41 += 1
                        snowDepth = (row["Value_inches"])
                        total41 = int(snowDepth) + total41
                except:
                    pass
                try:
                    if row["County"] == county[42]:
                        count42 += 1
                        snowDepth = (row["Value_inches"])
                        total42 = int(snowDepth) + total42
                except:
                    pass
                try:
                    if row["County"] == county[43]:
                        count43 += 1
                        snowDepth = (row["Value_inches"])
                        total43 = int(snowDepth) + total43
                except:
                    pass
                try:
                    if row["County"] == county[44]:
                        count44 += 1
                        snowDepth = (row["Value_inches"])
                        total44 = int(snowDepth) + total44
                except:
                    pass
                try:
                    if row["County"] == county[45]:
                        count45 += 1
                        snowDepth = (row["Value_inches"])
                        total45 = int(snowDepth) + total45
                except:
                    pass
                try:
                    if row["County"] == county[46]:
                        count46 += 1
                        snowDepth = (row["Value_inches"])
                        total46 = int(snowDepth) + total46
                except:
                    pass
                try:
                    if row["County"] == county[47]:
                        count47 += 1
                        snowDepth = (row["Value_inches"])
                        total47 = int(snowDepth) + total47
                except:
                    pass
                try:
                    if row["County"] == county[48]:
                        count48 += 1
                        snowDepth = (row["Value_inches"])
                        total48 = int(snowDepth) + total48
                except:
                    pass
                try:
                    if row["County"] == county[49]:
                        count49 += 1
                        snowDepth = (row["Value_inches"])
                        total49 = int(snowDepth) + total49
                except:
                    pass
                try:
                    if row["County"] == county[50]:
                        count50 += 1
                        snowDepth = (row["Value_inches"])
                        total50 = int(snowDepth) + total50
                except:
                    pass
                try:
                    if row["County"] == county[51]:
                        count51 += 1
                        snowDepth = (row["Value_inches"])
                        total51 = int(snowDepth) + total51
                except:
                    pass
                try:
                    if row["County"] == county[52]:
                        count52 += 1
                        snowDepth = (row["Value_inches"])
                        total52 = int(snowDepth) + total52
                except:
                    pass
                try:
                    if row["County"] == county[53]:
                        count53 += 1
                        snowDepth = (row["Value_inches"])
                        total53 = int(snowDepth) + total53
                except:
                    pass
                try:
                    if row["County"] == county[54]:
                        count54 += 1
                        snowDepth = (row["Value_inches"])
                        total54 = int(snowDepth) + total54
                except:
                    pass
                try:
                    if row["County"] == county[55]:
                        count55 += 1
                        snowDepth = (row["Value_inches"])
                        total55 = int(snowDepth) + total55
                except:
                    pass

    return(total0, total1, total2, total3, total4, total5, total6, total7, total8, total9, total10,
    total11, total12, total13, total14, total15, total16, total17, total18, total19, total20,
    total21, total22, total23, total24, total25, total26, total27, total28, total29, total30,
    total31, total32, total33, total34, total35, total36, total37, total38, total39, total40,
    total41, total42, total43, total44, total45, total46, total47, total48, total49, total50,
    total51, total52, total53, total54, total55, count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10,
    count11, count12, count13, count14, count15, count16, count17, count18, count19, count20,
    count21, count22, count23, count24, count25, count26, count27, count28, count29, count30,
    count31, count32, count33, count34, count35, count36, count37, count38, count39, count40,
    count41, count42, count43, count44, count45, count46, count47, count48, count49, count50,
    count51, count52, count53, count54, count55 )

def calculateAverageDepth():
    try:
        Beaverhead = readDepth()[0] / readDepth()[56]
    except:
        Beaverhead = 0
    try:
        BigHorn = readDepth()[1] / readDepth()[57]
    except:
        BigHorn = 0
    try:
        Blaine = readDepth()[2] / readDepth()[58]
    except:
        Blaine = 0
    try:
        Broadwater = readDepth()[3] / readDepth()[59]
    except:
        Broadwater = 0
    try:
        Carbon = readDepth()[4] / readDepth()[60]
    except:
        Carbon = 0
    try:
        Carter = readDepth()[5] / readDepth()[61]
    except:
        Carter = 0
    try:
        Cascade = readDepth()[6] / readDepth()[62]
    except:
        Cascade = 0
    try:
        Chouteau = readDepth()[7] / readDepth()[63]
    except:
        Chouteau = 0
    try:
        Custer = readDepth()[8] / readDepth()[64]
    except:
        Custer = 0
    try:
        Daniels = readDepth()[9] / readDepth()[65]
    except:
        Daniels = 0
    try:
        Dawson = readDepth()[10] / readDepth()[66]
    except:
        Dawson = 0
    try:
        DeerLodge = readDepth()[11] / readDepth()[67]
    except:
        DeerLodge = 0
    try:
        Fallon = readDepth()[12] / readDepth()[68]
    except:
        Fallon = 0
    try:
        Fergus = readDepth()[13] / readDepth()[69]
    except:
        Fergus = 0
    try:
        Flathead = readDepth()[14] / readDepth()[70]
    except:
        Flathead = 0
    try:
        Gallatin = readDepth()[15] / readDepth()[71]
    except:
        Gallatin = 0
    try:
        Garfield = readDepth()[16] / readDepth()[72]
    except:
        Garfield = 0
    try:
        Glacier = readDepth()[17] / readDepth()[73]
    except:
        Glacier = 0
    try:
        GoldenValley = readDepth()[18] / readDepth()[74]
    except:
        GoldenValley = 0
    try:
        Granite = readDepth()[19] / readDepth()[75]
    except:
        Granite = 0
    try:
        Hill = readDepth()[20] / readDepth()[76]
    except:
        Hill = 0
    try:
        Jefferson = readDepth()[21] / readDepth()[77]
    except:
        Jefferson = 0
    try:
        JudithBasin = readDepth()[22] / readDepth()[78]
    except:
        JudithBasin = 0
    try:
        Lake = readDepth()[23] / readDepth()[79]
    except:
        Lake = 0
    try:
        LewisAndClark = readDepth()[24] / readDepth()[80]
    except:
        LewisAndClark = 0
    try:
        Liberty = readDepth()[25] / readDepth()[81]
    except:
        Liberty = 0
    try:
        Lincoln = readDepth()[26] / readDepth()[82]
    except:
        Lincoln = 0
    try:
        Madison = readDepth()[27] / readDepth()[83]
    except:
        Madison = 0
    try:
        McCone = readDepth()[28] / readDepth()[84]
    except:
        McCone = 0
    try:
        Meagher = readDepth()[29] / readDepth()[85]
    except:
        Meagher = 0
    try:
        Mineral = readDepth()[30] / readDepth()[86]
    except:
        Mineral = 0
    try:
        Missoula = readDepth()[31] / readDepth()[87]
    except:
        Missoula = 0
    try:
        Musselshell = readDepth()[32] / readDepth()[88]
    except:
        Musselshell = 0
    try:
        Park = readDepth()[33] / readDepth()[89]
    except:
        Park = 0
    try:
        Petrolium = readDepth()[34] / readDepth()[90]
    except:
        Petrolium = 0
    try:
        Phillips = readDepth()[35] / readDepth()[91]
    except:
        Phillips = 0
    try:
        Pondera = readDepth()[36] / readDepth()[92]
    except:
        Pondera = 0
    try:
        PowderRiver = readDepth()[37] / readDepth()[93]
    except:
        PowderRiver = 0
    try:
        Powell = readDepth()[38] / readDepth()[94]
    except:
        Powell = 0
    try:
        Prairie = readDepth()[39] / readDepth()[95]
    except:
        Prairie = 0
    try:
        Ravalli = readDepth()[40] / readDepth()[96]
    except:
        Ravalli = 0
    try:
        Richland = readDepth()[41] / readDepth()[97]
    except:
        Richland = 0
    try:
        Roosevelt = readDepth()[42] / readDepth()[98]
    except:
        Roosevelt = 0
    try:
        Rosebud = readDepth()[43] / readDepth()[99]
    except:
        Rosebud = 0
    try:
        Sanders = readDepth()[44] / readDepth()[100]
    except:
        Sanders = 0
    try:
        Sheridan = readDepth()[45] / readDepth()[101]
    except:
        Sheridan = 0
    try:
        SilverBow = readDepth()[46] / readDepth()[102]
    except:
        SilverBow = 0
    try:
        Stillwater = readDepth()[47] / readDepth()[103]
    except:
        Stillwater = 0
    try:
        SweetGrass = readDepth()[48] / readDepth()[104]
    except:
        SweetGrass = 0
    try:
        Teton = readDepth()[49] / readDepth()[105]
    except:
        Teton = 0
    try:
        Toole = readDepth()[50] / readDepth()[106]
    except:
        Toole = 0
    try:
        Treasure = readDepth()[51] / readDepth()[107]
    except:
        Treasure = 0
    try:
        Valley = readDepth()[52] / readDepth()[108]
    except:
        Valley = 0
    try:
        Wheatland = readDepth()[53] / readDepth()[109]
    except:
        Wheatland = 0
    try:
        Wibaux = readDepth()[54] / readDepth()[110]
    except:
        Wibaux = 0
    try:
        Yellowstone = readDepth()[55] / readDepth()[111]
    except:
        Yellowstone = 0

    with open('Averages.csv', 'w', newline='') as csvfile:
        CSV = csv.writer(csvfile)

        county1 = ["Beaverhead", "Big Horn", "Blaine", "Broadwater", "Carbon", "Carter", "Cascade", "Chouteau", "Custer",
                  "Daniels", "Dawson", "Deer Lodge", "Fallon", "Fergus", "Flathead", "Gallatin", "Garfield", "Glacier",
                  "Golden Valley", "Granite", "Hill", "Jefferson", "Judith Basin", "Lake", "Lewis and Clark", "Liberty",
                  "Lincoln", "Madison", "McCone", "Meagher", "Mineral", "Missoula", "Musselshell", "Park", "Petroleum",
                  "Phillips", "Pondera", "Powder River", "Powell", "Prairie", "Ravalli", "Richland", "Roosevelt", "Rosebud",
                  "Sanders", "Sheridan", "Silver Bow", "Stillwater", "Sweet Grass", "Teton", "Toole", "Treasure", "Valley",
                  "Wheatland", "Wibaux", "Yellowstone"]
        county = []
        for i in range(len(county1)):
            county.append(county1[i].upper())

        CSV.writerow([county[0], Beaverhead])
        CSV.writerow([county[1], BigHorn])
        CSV.writerow([county[2], Blaine])
        CSV.writerow([county[3], Broadwater])
        CSV.writerow([county[4], Carbon])
        CSV.writerow([county[5], Carter])
        CSV.writerow([county[6], Cascade])
        CSV.writerow([county[7], Chouteau])
        CSV.writerow([county[8], Custer])
        CSV.writerow([county[9], Daniels])
        CSV.writerow([county[10], Dawson])
        CSV.writerow([county[11], DeerLodge])
        CSV.writerow([county[12], Fallon])
        CSV.writerow([county[13], Fergus])
        CSV.writerow([county[14], Flathead])
        CSV.writerow([county[15], Gallatin])
        CSV.writerow([county[16], Garfield])
        CSV.writerow([county[17], Glacier])
        CSV.writerow([county[18], GoldenValley])
        CSV.writerow([county[19], Granite])
        CSV.writerow([county[20], Hill])
        CSV.writerow([county[21], Jefferson])
        CSV.writerow([county[22], JudithBasin])
        CSV.writerow([county[23], Lake])
        CSV.writerow([county[24], LewisAndClark])
        CSV.writerow([county[25], Liberty])
        CSV.writerow([county[26], Lincoln])
        CSV.writerow([county[27], Madison])
        CSV.writerow([county[28], McCone])
        CSV.writerow([county[29], Meagher])
        CSV.writerow([county[30], Mineral])
        CSV.writerow([county[31], Missoula])
        CSV.writerow([county[32], Musselshell])
        CSV.writerow([county[33], Park])
        CSV.writerow([county[34], Petrolium])
        CSV.writerow([county[35], Phillips])
        CSV.writerow([county[36], Pondera])
        CSV.writerow([county[37], PowderRiver])
        CSV.writerow([county[38], Powell])
        CSV.writerow([county[39], Prairie])
        CSV.writerow([county[40], Ravalli])
        CSV.writerow([county[41], Richland])
        CSV.writerow([county[42], Roosevelt])
        CSV.writerow([county[43], Rosebud])
        CSV.writerow([county[44], Sanders])
        CSV.writerow([county[45], Sheridan])
        CSV.writerow([county[46], SilverBow])
        CSV.writerow([county[47], Stillwater])
        CSV.writerow([county[48], SweetGrass])
        CSV.writerow([county[49], Teton])
        CSV.writerow([county[50], Toole])
        CSV.writerow([county[51], Treasure])
        CSV.writerow([county[52], Valley])
        CSV.writerow([county[53], Wheatland])
        CSV.writerow([county[54], Wibaux])
        CSV.writerow([county[55], Yellowstone])

calculateAverageDepth()
