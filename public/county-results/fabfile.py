import fabric
from fabric.api import *
from fabric.operations import *
from bs4 import BeautifulSoup
import re
import json

fabric.state.output.stdout = False
fabric.state.output.running = False
fabric.state.output.status = False

DEM_URL = "https://enrpages.sos.state.tx.us/public/mar01_233_race0.htm"
GOP_URL = "https://enrpages.sos.state.tx.us/public/mar01_273_race0.htm"


COUNTY_DICT = {"ANDERSON": "001", "ANDREWS": "003", "ANGELINA": "005", "ARANSAS": "007", "ARCHER": "009", "ARMSTRONG": "011", "ATASCOSA": "013", "AUSTIN": "015", "BAILEY": "017", "BANDERA": "019", "BASTROP": "021", "BAYLOR": "023", "BEE": "025", "BELL": "027", "BEXAR": "029", "BLANCO": "031", "BORDEN": "033", "BOSQUE": "035", "BOWIE": "037", "BRAZORIA": "039", "BRAZOS": "041", "BREWSTER": "043", "BRISCOE": "045", "BROOKS": "047", "BROWN": "049", "BURLESON": "051", "BURNET": "053", "CALDWELL": "055", "CALHOUN": "057", "CALLAHAN": "059", "CAMERON": "061", "CAMP": "063", "CARSON": "065", "CASS": "067", "CASTRO": "069", "CHAMBERS": "071", "CHEROKEE": "073", "CHILDRESS": "075", "CLAY": "077", "COCHRAN": "079", "COKE": "081", "COLEMAN": "083", "COLLIN": "085", "COLLINGSWORTH": "087", "COLORADO": "089", "COMAL": "091", "COMANCHE": "093", "CONCHO": "095", "COOKE": "097", "CORYELL": "099", "COTTLE": "101", "CRANE": "103", "CROCKETT": "105", "CROSBY": "107", "CULBERSON": "109", "DALLAM": "111", "DALLAS": "113", "DAWSON": "115", "DEAF SMITH": "117", "DELTA": "119", "DENTON": "121", "DEWITT": "123", "DICKENS": "125", "DIMMIT": "127", "DONLEY": "129", "DUVAL": "131", "EASTLAND": "133", "ECTOR": "135", "EDWARDS": "137", "ELLIS": "139", "EL PASO": "141", "ERATH": "143", "FALLS": "145", "FANNIN": "147", "FAYETTE": "149", "FISHER": "151", "FLOYD": "153", "FOARD": "155", "FORT BEND": "157", "FRANKLIN": "159", "FREESTONE": "161", "FRIO": "163", "GAINES": "165", "GALVESTON": "167", "GARZA": "169", "GILLESPIE": "171", "GLASSCOCK": "173", "GOLIAD": "175", "GONZALES": "177", "GRAY": "179", "GRAYSON": "181", "GREGG": "183", "GRIMES": "185", "GUADALUPE": "187", "HALE": "189", "HALL": "191", "HAMILTON": "193", "HANSFORD": "195", "HARDEMAN": "197", "HARDIN": "199", "HARRIS": "201", "HARRISON": "203", "HARTLEY": "205", "HASKELL": "207", "HAYS": "209", "HEMPHILL": "211", "HENDERSON": "213", "HIDALGO": "215", "HILL": "217", "HOCKLEY": "219", "HOOD": "221", "HOPKINS": "223", "HOUSTON": "225", "HOWARD": "227", "HUDSPETH": "229", "HUNT": "231", "HUTCHINSON": "233", "IRION": "235", "JACK": "237", "JACKSON": "239", "JASPER": "241", "JEFF DAVIS": "243", "JEFFERSON": "245", "JIM HOGG": "247", "JIM WELLS": "249", "JOHNSON": "251", "JONES": "253", "KARNES": "255", "KAUFMAN": "257", "KENDALL": "259", "KENEDY": "261", "KENT": "263", "KERR": "265", "KIMBLE": "267", "KING": "269", "KINNEY": "271", "KLEBERG": "273", "KNOX": "275", "LAMAR": "277", "LAMB": "279", "LAMPASAS": "281", "LASALLE": "283", "LAVACA": "285", "LEE": "287", "LEON": "289", "LIBERTY": "291", "LIMESTONE": "293", "LIPSCOMB": "295", "LIVE OAK": "297", "LLANO": "299", "LOVING": "301", "LUBBOCK": "303", "LYNN": "305", "MCCULLOCH": "307", "MCLENNAN": "309", "MCMULLEN": "311", "MADISON": "313", "MARION": "315", "MARTIN": "317", "MASON": "319", "MATAGORDA": "321", "MAVERICK": "323", "MEDINA": "325", "MENARD": "327", "MIDLAND": "329", "MILAM": "331", "MILLS": "333", "MITCHELL": "335", "MONTAGUE": "337", "MONTGOMERY": "339", "MOORE": "341", "MORRIS": "343", "MOTLEY": "345", "NACOGDOCHES": "347", "NAVARRO": "349", "NEWTON": "351", "NOLAN": "353", "NUECES": "355", "OCHILTREE": "357", "OLDHAM": "359", "ORANGE": "361", "PALO PINTO": "363", "PANOLA": "365", "PARKER": "367", "PARMER": "369", "PECOS": "371", "POLK": "373", "POTTER": "375", "PRESIDIO": "377", "RAINS": "379", "RANDALL": "381", "REAGAN": "383", "REAL": "385", "RED RIVER": "387", "REEVES": "389", "REFUGIO": "391", "ROBERTS": "393", "ROBERTSON": "395", "ROCKWALL": "397", "RUNNELS": "399", "RUSK": "401", "SABINE": "403", "SAN AUGUSTINE": "405", "SAN JACINTO": "407", "SAN PATRICIO": "409", "SAN SABA": "411", "SCHLEICHER": "413", "SCURRY": "415", "SHACKELFORD": "417", "SHELBY": "419", "SHERMAN": "421", "SMITH": "423", "SOMERVELL": "425", "STARR": "427", "STEPHENS": "429", "STERLING": "431", "STONEWALL": "433", "SUTTON": "435", "SWISHER": "437", "TARRANT": "439", "TAYLOR": "441", "TERRELL": "443", "TERRY": "445", "THROCKMORTON": "447", "TITUS": "449", "TOM GREEN": "451", "TRAVIS": "453", "TRINITY": "455", "TYLER": "457", "UPSHUR": "459", "UPTON": "461", "UVALDE": "463", "VAL VERDE": "465", "VAN ZANDT": "467", "VICTORIA": "469", "WALKER": "471", "WALLER": "473", "WARD": "475", "WASHINGTON": "477", "WEBB": "479", "WHARTON": "481", "WHEELER": "483", "WICHITA": "485", "WILBARGER": "487", "WILLACY": "489", "WILLIAMSON": "491", "WILSON": "493", "WINKLER": "495", "WISE": "497", "WOOD": "499", "YOAKUM": "501", "YOUNG": "503", "ZAPATA": "505", "ZAVALA": "507"}


def isOdd(n):
    if n % 2 == 0:
        return False
    else:
        return True


DEM_CANDS = [
    "Hillary Clinton",
    "Roque \"Rocky\" De La Fuente",
    "Calvis L. Hawes",
    "Keith Judd",
    "Star Locke",
    "Martin O'Malley",
    "Bernie Sanders",
    "Willie Wilson"
    ]

GOP_CANDS = [
    "Jeb Bush",
    "Ben Carson",
    "Chris Christie",
    "Ted Cruz",
    "Carly Fiorina",
    "Lindsey Graham",
    "Elizabeth Gray",
    "Mike Huckabee",
    "John Kasich",
    "Rand Paul",
    "Marco Rubio",
    "Rick Santorum",
    "Donald Trump",
    "Uncommitted"
    ]


def scrape(party):
    if party == "d":
        x = local('curl ' + DEM_URL, capture=True)
        soup = BeautifulSoup(x, "html.parser")
        table = soup.find('table')
        rows = table.find_all('tr')

        dem_obj = {}
        dem_obj['delegate_count'] = {
            'al': {},
            'alt': {},
            'ppeo': {}
        }
        dem_obj['popular_vote'] = []

        for idx, row in enumerate(rows[3:]):
            col = row.find_all('td')
            if re.compile("^DELEGATE AL$").match(col[0].string.upper()):
                for i, name in enumerate(DEM_CANDS):
                    votes = int(col[i+1].string.replace(",", ""))
                    dem_obj['delegate_count']['al'][name] = votes
            if re.compile("^DELEGATE ALT$").match(col[0].string.upper()):
                for i, name in enumerate(DEM_CANDS):
                    votes = int(col[i+1].string.replace(",", ""))
                    dem_obj['delegate_count']['alt'][name] = votes
            if re.compile("^DELEGATE PPEO$").match(col[0].string.upper()):
                for i, name in enumerate(DEM_CANDS):
                    votes = int(col[i+1].string.replace(",", ""))
                    dem_obj['delegate_count']['ppeo'][name] = votes
            if idx > 4:
                if isOdd(idx):
                    county = col[0].string.strip().upper()
                    try:
                        county = COUNTY_DICT[county]
                    except KeyError:
                        pass
                    c_length = len(DEM_CANDS)
                    reg_voters = col[c_length+2].string.strip().replace(",", "")
                    provisional = col[c_length+4].string.strip().replace(",", "")
                    precincts_rep = col[c_length+5].string.strip().replace(",", "")
                    precincts_total = col[c_length+6].string.strip().replace(",", "")
                    countydict = {}
                    countydict[county] = {
                        'early': {},
                        'regular': {},
                        'registered_voters': int(reg_voters),
                        'provisional': int(provisional),
                        'precincts_reported': int(precincts_rep),
                        'precincts_total': int(precincts_total)
                    }
                    for i, name in enumerate(DEM_CANDS):
                        votes = int(col[i+1].string.replace(",", ""))
                        countydict[county]['regular'][name] = votes
                else:
                    for i, name in enumerate(DEM_CANDS):
                        votes = int(col[i+1].string.replace(",", ""))
                        countydict[county]['early'][name] = votes
                    dem_obj['popular_vote'].append(countydict)
        print json.dumps(dem_obj)

    if party == "r":
        x = local('curl ' + GOP_URL, capture=True)
        soup = BeautifulSoup(x, "html.parser")
        table = soup.find('table')
        rows = table.find_all('tr')

        gop_obj = {}
        gop_obj['delegate_count'] = {
            'al': {}
        }
        gop_obj['popular_vote'] = []

        for idx, row in enumerate(rows[3:]):
            col = row.find_all('td')
            if re.compile("^DELEGATE AL$").match(col[0].string.upper()):
                for i, name in enumerate(DEM_CANDS):
                    votes = int(col[i+1].string.replace(",", ""))
                    gop_obj['delegate_count']['al'][name] = votes
            if idx > 2:
                if isOdd(idx):
                    county = col[0].string.strip().upper()
                    try:
                        county = COUNTY_DICT[county]
                    except KeyError:
                        pass
                    c_length = len(GOP_CANDS)
                    reg_voters = col[c_length+2].string.strip().replace(",", "")
                    provisional = col[c_length+4].string.strip().replace(",", "")
                    precincts_rep = col[c_length+5].string.strip().replace(",", "")
                    precincts_total = col[c_length+6].string.strip().replace(",", "")
                    countydict = {}
                    countydict[county] = {
                        'early': {},
                        'regular': {},
                        'registered_voters': int(reg_voters),
                        'provisional': int(provisional),
                        'precincts_reported': int(precincts_rep),
                        'precincts_total': int(precincts_total)
                    }
                    for i, name in enumerate(GOP_CANDS):
                        votes = int(col[i+1].string.replace(",", ""))
                        countydict[county]['regular'][name] = votes
                else:
                    for i, name in enumerate(GOP_CANDS):
                        votes = int(col[i+1].string.replace(",", ""))
                        countydict[county]['early'][name] = votes
                    gop_obj['popular_vote'].append(countydict)
        print json.dumps(gop_obj)
