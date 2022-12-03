#%reset

# LookUp Table for anomalies

lookUp = {
}
#
# crash = tuple(["1.Koenige", "5", 1])
# if crash in lookUp.keys():
#     a, b, c, d = lookUp[crash]
#     print(c)
#

import xml.etree.ElementTree as ET

german = ET.parse('german_S2000.xml')
root = german.getroot()
russian = ET.parse('russian.xml')
root2 = russian.getroot()

x = -1
y = -1
z = -1
anomaly = 0

for b in root.findall('BIBLEBOOK'):
    x = x + 1
    y = -1
    infobook = b.attrib
    print(infobook["bname"])
    for c in b.findall('CHAPTER'):
        y = y + 1
        z = -1
        infochapter = c.attrib
        print("Chapter: " + infochapter["cnumber"])

        if infobook["bname"] == "Offenbarung" and infochapter["cnumber"] == "23":
            print("\n##### Reached the end! #####\n")
            break
        else:
            for char in c.findall('VERS'):
                infoverse = char.attrib
                z = z + 1

                # Psalms special treatment. I had to do this, you might not need this. Just comment lines 46-64 in this case.
                if str(infobook["bname"]) == "Psalmen" and int(infoverse["vnumber"]) == 1:
                    verse1 = root2[x][y][z].text
                    #print(verse1)
                    if ":2)" in verse1 or "-2)" in verse1:
                        insert_element = ET.Element("VERS")
                        spl = verse1.split("2)")
                        insert_element.text = " (" + str(infochapter["cnumber"]) + ":" + infoverse["vnumber"] + ")" + spl[1]
                        while spl[0][-1].isnumeric() or spl[0][-1] in ["(", ":", ")", "-"]:
                            spl[0] = spl[0][:-1]
                        root2[x][y][z].text = spl[0]
                        #print(root2[x][y][z].text)

                        for br in root2.findall('BIBLEBOOK'):
                            for cr in br.findall('CHAPTER'):
                                if br.attrib["bname"] == "Psalm" and cr.attrib["cnumber"] == infochapter["cnumber"]:
                                    print("Anfang ersetzen:", br.attrib["bname"], cr.attrib["cnumber"])
                                    cr.insert(1, insert_element)
                                    print("###Worked!###")
                                    #ET.dump(cr)

                crash = tuple([str(infobook["bname"]), str(infochapter["cnumber"]), int(infoverse["vnumber"])])
                if crash in lookUp.keys():
                    print("Anomaly!!!")
                    anomaly = 1
                    until, dx, dy, new_z = lookUp[crash]
                if anomaly == 1:
                    new_y = y+dy
                    gv = root[x][y][z].text
                    rv = root2[x][new_y][new_z].text
                    vv = str(gv) + "(" + str(new_y+1) + ":" + str(new_z + 1) + ") " + str(rv)
                    new_z = new_z + 1
                    if int(infoverse["vnumber"]) == until:
                        print("Ende, Vers: " + infoverse["vnumber"])
                        anomaly = 0
                        z = -1
                else:
                    gv = root[x][y][z].text
                    rv = root2[x][y][z].text
                    vv = str(gv) +  "&#10;" + str(rv)
                char.text = vv
    else:
        continue

    break


export = ET.ElementTree(root)
export.write("export.xml",encoding="UTF-8")
