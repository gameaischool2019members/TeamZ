import tracery, json
from pprint import pprint
from pymclevel import alphaMaterials

grammarTest = {
    "origin": ["#[karmaCounter:0]dothings#"],
    "dothings": ["#thing# #karma#", "#thing# and #thing# #karma#", "#thing# and #thing# and #thing# #karma#"],
    "thing": ["#goodThing#","#badThing#"],
    "goodThing": ["[karmaCounter:#karmaCounter# 10]saved a kitty","[karmaCounter:#karmaCounter# 15]helped an old lady across the road",],
    "badThing": ["[karmaCounter:#karmaCounter# -10]kicked a puppy","[karmaCounter:#karmaCounter# -20]burnt an orphanage",],
    "karma": ["Your Karma was: #karmaCounter#"]
}

grammar = {
    "origin": ["#[VarPop:0][Town:#townName#][Size:#size#][Type:#township#][Founder:#personName#][YearFounded:#year#][Material:#materials#][InitialSize:#Size#]output#"],
    "output": ["#lore# #json#"],
    "lore": ["#foundingLore#\n\n#storyBeat#", "#foundingLore#\n\n#storyBeat#\n\n#storyBeat#",
             "#foundingLore#\n\n#storyBeat#\n\n#storyBeat#\n\n#storyBeat#",
             "#foundingLore#\n\n#storyBeat#\n\n#storyBeat#\n\n#storyBeat#\n\n#storyBeat#", ],
    "township": ["hamlet", "village", "city", "metropolis", "town", "township", "port", "principality",
                 "borough", "municipality","suburb"],
    "size": ["[VarPop:#VarPop# 100]small", "[VarPop:#VarPop# 150]medium", "[VarPop:#VarPop# 200]large"],
    "townName": ["Helena Valley Southeast", "Fredericksburg", "Salmon Creek", "Grizzly Flats",
                 "Cocoa Beach", "Quasqueton", "Meadowbrook Farm", "Falconaire", "Saluda",
                 "Leadville North", "Marvin", "Briar", "Lookingglass", "Oronoco", "Pine Point",
                 "Setauket", "Ossineke", "Eldora", "Hooppole", "Tunica Resorts", "Dunfermline",
                 "Port Costa", "Marble Cliff", "Painted Hills", "Carlsbad", "Frontier",
                 "Village Shires", "Deer Grove", "Valley Springs", "Crugers", "Southbridge Town",
                 "Ridge", "Stonewall", "Plattsburgh", "Waukegan", "Funston", "Yantis",
                 "North Spearfish", "Damar", "Pasco", "Commack", "Klein", "Comunas", "Buchanan",
                 "Yeager", "Danforth", "Nibley", "Mars Hill", "Port Aransas", "Orem", "Culloden",
                 "Brian Head", "Iowa Colony", "Honaunau", "Accident", "Batchtown", "Rew",
                 "Clearlake", "Titonka", "Byromville", "Simpson", "Shawneetown", "Dierks",
                 "Hooper", "Lead", "Fontanelle", "Henrietta", "Chevy Chase", "Cohasset",
                 "Fruit Cove", "Wide Ruins", "East Grand Forks", "Wataga", "West Carthage",
                 "Oreana", "Egg Harbor", "Wake Village", "Poughkeepsie", "Campbellton",
                 "West Middlesex", "Cementon", "Moncure", "Bell Gardens", "Airmont",
                 "Emigration Canyon", "Fifth Ward", "Oquawka", "Toston", "Foscoe",
                 "Fernandina Beach", "Candor", "South Heart", "South Pasadena", "Atqasuk",
                 "Warrior Run", "Beech Mountain", "East Kingston", "Boomer", "East New Market",
                 "Peppermill Village", "Selfridge", "North Edwards", "Swaledale", "Valley Falls",
                 "Bradley Gardens", "Bridge City", "Canadian Lakes", "Humeston", "Belleville",
                 "Bunkerville", "Albert", "North Syracuse", "San Buenaventura", "Upper Falls",
                 "Mount Etna", "North Lynbrook", "Cheney", "Hidden Valley Lake", "Deepstep",
                 "Point Comfort", "Falls City", "Spring Gap", "Cuyahoga Heights", "Lonaconing",
                 "Bonita Springs", "Killeen", "Swayzee", "Saw Creek", "Nickerson", "Wolcottville",
                 "Royal Palm Estates", "Northvale", "Fort Shaw", "Clara", "St. Libory",
                 "Bucksport", "South Miami", "Westview", "Frazer", "Wallins Creek", "Diomede",
                 "Fort Bragg", "Leola", "Kearns", "Eagle Lake", "Comanche Creek", "Gurnee",
                 "Tonopah", "Sharonville", "Big Bear Lake"],
    "personName": ["Doris K Harmon", "Gloria N Quintana", "Kristen M Bronson",
                   "Katherine N Wylie", "Tiffany Y Wheatley", "Sandra D Guidry",
                   "Frances D Gross", "Geraldine A Renteria", "Audrey N Hinson",
                   "Evelyn Q Walden", "Gertrude M Lutz", "Linda G Mosher",
                   "Doris I Beck", "Rose H Shaw", "Sherry M Carranza",
                   "Frances Q Carney", "Christina P Sell", "Amy N Robison",
                   "Amy Y Temple", "Phyllis F Wheatley", "Jacqueline D Mahan",
                   "Joann Y Olson", "Regina R Kauffman", "Juanita F Sanchez",
                   "Dana Y Bowling", "Wendy W Wendt", "Yolanda C Severson",
                   "Ruth L Slater", "Stephanie T Sharpe", "Beth T Brown",
                   "Laura X Dempsey", "Annie L Duncan", "Carla R Stump",
                   "Jacqueline O Ballard", "Josephine H Jennings", "Carrie B Walden",
                   "Kelly Z Soria", "Theresa A Bentley", "Dana U Myrick",
                   "Dana R Avalos", "Eva G England", "Paula V Cleveland",
                   "Kelly Q Guajardo", "Tammy J Cardona", "Wendy A Lord",
                   "Judith W Rinehart", "Judith Y Skinner", "Rita O Hopkins",
                   "Dolores B Fallon", "Eva N Ellis", "Sean M Henriquez", "Ben D Slocum",
                   "Joshua O Diorio", "Jerry G Kennon", "Steve A Macha",
                   "Melvin J Prevost", "Lewis P Kinley", "Jesus N Arndt",
                   "Reginald X Simien", "Benjamin T Canada", "Rafael D Schisler",
                   "Bernard U Weier", "Kurt G McCalister", "Matthew P Bullinger",
                   "Clarence G Moyes", "Robert X Shoaf", "Brad N Minyard",
                       "Leslie U Counts", "Leo S Ruppert", "Marc E Chiu",
                   "Leonard Y Blystone", "Dean F Stoecker", "Anthony U Cale",
                   "Brandon G Uren", "Theodore I Dearborn", "Bradley Z Hasson",
                   "Sean C Callier", "Shawn W Serratos", "James B Rigby",
                   "Larry O Mellon", "Jason T Rispoli", "Kurt J Smedley",
                   "Theodore T Griffeth", "Tony M Khang", "Thomas D Schwanke",
                   "Jeffrey X Carlin", "Casey I Freiberg", "Dwayne Q Oser",
                   "Sam B Michalak", "Max Z Sumpter", "Alexander T Traub",
                   "Hugh Q Wildman", "Douglas T Markiewicz", "Christian E Bitz",
                   "Douglas Q Postma", "Jessie X Barrington", "Ray L Stitt",
                   "Barry Z Sipe", "Tony J Wilbur", "Leroy X Latino", "Jeffery I Pell",
                   "Jeffrey D Goldston", "Leonard V Lamberson", "Brett F Stenzel",
                   "Bryan O Hardin", "Bob Z Amar", "Glenn Q Gano", "Lester S Rudd",
                   "Thomas N Gagnier", "Roberto I Dearth", "Chris E Crow",
                   "Cory N Salisbury", "Benjamin O Howze", "Micheal V Dubey",
                   "Henry E Yearwood", "Edgar K Rockhill", "Chris Q Marquart",
                   "Fernando W Thornell", "Leon F Militello", "Charles Z Edman",
                   "Jacob C Foxx", "Jesse K Whitehill", "Lloyd J Rutter",
                   "Corey I White", "Dwight E Hildenbrand", "Cory Q Begaye",
                   "Edward N Currey", "Jeremy A Laduke", "Shane A Worcester",
                   "Tyler Q Stauffer", "Greg I Keener", "Brandon L Clem",
                   "Aaron M Wardell", "Jay C Schexnayder", "Alexander N Wardle",
                   "Bryan M Jaggers", "Barry N Carrick", "Paul D Curd",
                   "Melvin T Goodwill", "Leo X Stallman", "Ryan Z McNally",
                   "Harry F Harmer", "Jamie Y Admire", "Lonnie W Steen",
                   "Leonard W Gaddie", "Glenn L Varner", "Theodore T Alcantar",
                   "Derek E Marquart", "Gary C Benefiel", "Jimmy W Kroening"],
    "personType": ["scientist", "engineer", "artist", "politician",
                   "philanthropist", "military officer"],
    "year": ["1800", "1801", "1802", "1803", "1804", "1805",
             "1806", "1807", "1808", "1809", "1810", "1811",
             "1812", "1813", "1814", "1815", "1816", "1817",
             "1818", "1819", "1820", "1821", "1822", "1823",
             "1824", "1825", "1826", "1827", "1828", "1829",
             "1830", "1831", "1832", "1833", "1834", "1835",
             "1836", "1837", "1838", "1839", "1840", "1841",
             "1842", "1843", "1844", "1845", "1846", "1847",
             "1848", "1849", "1850", "1851", "1852", "1853",
             "1854", "1855", "1856", "1857", "1858", "1859",
             "1860", "1861", "1862", "1863", "1864", "1865",
             "1866", "1867", "1868", "1869", "1870", "1871",
             "1872", "1873", "1874", "1875", "1876", "1877",
             "1878", "1879", "1880", "1881", "1882", "1883",
             "1884", "1885", "1886", "1887", "1888", "1889",
             "1890", "1891", "1892", "1893", "1894", "1895",
             "1896", "1897", "1898", "1899", "1900", "1901",
             "1902", "1903", "1904", "1905", "1906", "1907",
             "1908", "1909", "1910", "1911", "1912", "1913",
             "1914", "1915", "1916", "1917", "1918", "1919",
             "1920", "1921", "1922", "1923", "1924", "1925",
             "1926", "1927", "1928", "1929", "1930", "1931",
             "1932", "1933", "1934", "1935", "1936", "1937",
             "1938", "1939", "1940", "1941", "1942", "1943",
             "1944", "1945", "1946", "1947", "1948", "1949",
             "1950", "1951", "1952", "1953", "1954", "1955",
             "1956", "1957", "1958", "1959", "1960", "1961",
             "1962", "1963", "1964", "1965", "1966", "1967",
             "1968", "1969", "1970", "1971", "1972", "1973",
             "1974", "1975", "1976", "1977", "1978", "1979",
             "1980", "1981", "1982", "1983", "1984", "1985",
             "1986", "1987", "1988", "1989", "1990", "1991",
             "1992", "1993", "1994", "1995", "1996", "1997",
             "1998", "1999", "2000", "2001", "2002", "2003",
             "2004", "2005", "2006", "2007", "2008", "2009",
             "2010", "2011", "2012", "2013", "2014", "2015",
             "2016", "2017", "2018", "2019", "2020", "2021"],
    "materials":[
            "Stone",
            "Cobblestone",
            "Sandstone",
            "Wood",
            "Pine",
            "Birch",
            "Gravel"
        ],

    "adjective": ["sunny", "glorious", "opulent", "snowy",
                  "wonderful", "", "sleepy", "prosperous"],
    "townReference": ["#Town#",
                      "the #Type# of #Town#",
                      "the #adjective# #Type# of #Town#",
                      "the #adjective# #Type#",
                      "the #Type#"],
    "townReferenceName": [
        "#Town#",
        "the #Type# of #Town#",
        "the #adjective# #Type# of #Town#"],

    "foundingLore": [
        "#welcome#. #founding#. #buildingLore#"],
    "founding": [
        "#Town# was founded by #Founder# #yearDescription#",
        "It is recorded that #Founder# was responsible for creating the #Type# #yearDescription#",
        "History shows #Founder# originally settled this area #yearDescription#"
    ],
    "welcome": [
        "Welcome to #townReferenceName#",
        "Greetings from #townReferenceName#"],

    "yearDescription": [
        "in #YearFounded#",
        "sometime around #YearFounded#",
        "in the year #YearFounded#"],

    "buildingLore":["#buildingAvailability# #buildingConsequence#."],
    "buildingAvailability":["There was an abundance of #Material# in the area", "#Material# was readily available"],
    "buildingConsequence":["so the #Type# was built largely with that", "and this was used as a construction material", "to help construct the fledgling #Type#"],

    "storyBeat": [
        "#timing# #event#."],
    "timing": [
        "Shortly thereafter,",
        "After some time,",
        "Not long after this,",
        "After a brief period,",
        "As time passed,",
        "More recently,",
        "Since then,"],
    "event": [
        "#goodHappening#",
        "#badHappening#"],
    "goodHappening": [
        "#goodEvent# #neutralOutcome#",
        "#goodEvent#",
        "#goodEvent# #goodOutcome#"],
    "goodEvent": [
        "[VarPop:#VarPop# 2]more people moved to #townReference#",
        "a wealthy benefactor made an endowment to #townReference#",
        "#personName#, a famous #personType#, visited #townReference#"],
    "goodOutcome": [
        "[VarPop:#VarPop# 40]contributing significantly to its growth",
        "and the #Type# began to thrive",
        "and word of #Town# spread far and wide",
        "[VarPop:#VarPop# 20]and the #Type# prospered"],
    "badHappening": [
        "#badEvent# #neutralOutcome#",
        "#badEvent#",
        "#badEvent# #badOutcome#"],
    "badEvent": [
        "[VarPop:#VarPop# -10]a blight struck the nearby fields",
        "the nearby river flooded",
        "a rockslide occurred",
        "a plague of locusts descended"],
    "badOutcome": [
        "and the people began to suffer",
        "[VarPop:#VarPop# -30]and a number of citizens fled", ],
    "neutralOutcome": [
        "but life continued regardless",
        "although little really changed"],




    "json": [
        "MACHINEREADABLE:{\"town\":\"#Town#\",\"type\":\"#Type#\",\"yearFounded\":#YearFounded#,\"founder\":\"#Founder#\",\"material\":\"#Material#\",\"population\":\"#VarPop#\"}"]
}


def trace():
    g = tracery.Grammar(grammar)
    root = g.expand("#origin#")

    parts = root.finished_text.split("MACHINEREADABLE:")
    print "\n\n-----\n"
    print parts[0]
    print "\n\n-----"
    data = json.loads(parts[1])
    data = parse_data(data)
    #print data
    return data

def parse_data(data):

    def parse_data_materials(name):
        if name == "Stone":
            return alphaMaterials.Stone
        if name == "Cobblestone":
            return alphaMaterials.Cobblestone
        if name == "Sandstone":
            return alphaMaterials.Sandstone
        if name == "Wood":
            return alphaMaterials.Wood
        if name == "Pine":
            return alphaMaterials.PineWood
        if name == "Birch":
            return alphaMaterials.BirchWood
        if name == "Gravel":
            return alphaMaterials.Gravel
    def parse_data_population(string):
        sum = 0
        for part in string.split(' '):
            sum += int(part)
        return sum

    data["material"] = parse_data_materials(data["material"])
    data["population"] = parse_data_population(data["population"])
    return data

if __name__ == "__main__":
    trace()
