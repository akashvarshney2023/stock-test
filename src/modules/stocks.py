class Stock:
    def __init__(self, symbol):
        self.symbol = symbol

# List of Nifty 50 stocks
nifty_500_stocks = [
    "HINDZINC",
    "JWL",
    "VIJAYA",
    "HONAUT",
    "ENDURANCE",
    "UPL",
    "JSWENERGY",
    "POLYCAB",
    "IIFL",
    "RRKABEL",
    "CGCL",
    "JUBLINGREA",
    "FINEORG",
    "LALPATHLAB",
    "MANAPPURAM",
    "RHIM",
    "PAYTM",
    "ABFRL",
    "RAJESHEXPO",
    "BPCL",
    "SAPPHIRE",
    "ZOMATO",
    "ASTRAL",
    "STLTECH",
    "CHOLAFIN",
    "ZENSARTECH",
    "JBMA",
    "RBA",
    "CAMS",
    "MUTHOOTFIN",
    "VGUARD",
    "ENGINERSIN",
    "VEDL",
    "GPIL",
    "PEL",
    "HINDCOPPER",
    "COFORGE",
    "AEGISCHEM",
    "BIKAJI",
    "AAVAS",
    "VARROC",
    "SPARC",
    "TORNTPHARM",
    "RAYMOND",
    "TEJASNET",
    "ABCAPITAL",
    "LINDEINDIA",
    "TIINDIA",
    "QUESS",
    "ABBOTINDIA",
    "ABB",
    "ASTRAZEN",
    "KAYNES",
    "SUNDARMFIN",
    "VTL",
    "ESCORTS",
    "GSFC",
    "MANKIND",
    "JUBLPHARMA",
    "LLOYDSME",
    "NCC",
    "GLENMARK",
    "KALYANKJIL",
    "LAURUSLABS",
    "CUB",
    "MAHABANK",
    "SAIL",
    "SHYAMMETL",
    "DEEPAKNTR",
    "BANDHANBNK",
    "PIDILITIND",
    "MANYAVAR",
    "JBCHEPHARM",
    "REDINGTON",
    "GESHIP",
    "POWERGRID",
    "SYNGENE",
    "NTPC",
    "AFFLE",
    "POONAWALLA",
    "360ONE",
    "CASTROLIND",
    "HEROMOTOCO",
    "UJJIVANSFB",
    "PPLPHARMA",
    "CANFINHOME",
    "NLCINDIA",
    "CENTURYPLY",
    "FLUOROCHEM",
    "ATUL",
    "EICHERMOT",
    "TATAMTRDVR",
    "EIHOTEL",
    "JSWSTEEL",
    "ASIANPAINT",
    "ADANIPORTS",
    "LATENTVIEW",
    "APTUS",
    "THERMAX",
    "JINDALSAW",
    "ICICIPRULI",
    "NATIONALUM",
    "PRINCEPIPE",
    "IPCALAB",
    "UNOMINDA",
    "ASHOKLEY",
    "DIXON",
    "ITC",
    "METROPOLIS",
    "BOSCHLTD",
    "BERGEPAINT",
    "ANGELONE",
    "SUNTV",
    "SYRMA",
    "FIVESTAR",
    "DELHIVERY",
    "KEI",
    "CHAMBLFERT",
    "FEDERALBNK",
    "BLUESTARCO",
    "BHARTIARTL",
    "GMRINFRA",
    "HDFCLIFE",
    "RAMCOCEM",
    "MINDACORP",
    "USHAMART",
    "GRANULES",
    "HBLPOWER",
    "UCOBANK",
    "VOLTAS",
    "BIOCON",
    "HINDUNILVR",
    "RBLBANK",
    "JUBLFOOD",
    "INDIACEM",
    "ONGC",
    "IOC",
    "FINPIPE",
    "BAJAJ-AUTO",
    "SJVN",
    "ELGIEQUIP",
    "LUPIN",
    "MOTHERSON",
    "ACI",
    "ADANIENSOL",
    "TATAMOTORS",
    "MFSL",
    "ANANDRATHI",
    "BALKRISIND",
    "TRIDENT",
    "JMFINANCIL",
    "IDFC",
    "NH",
    "TV18BRDCST",
    "IEX",
    "MEDPLUS",
    "ZYDUSLIFE",
    "PNB",
    "INDUSTOWER",
    "GRSE",
    "AARTIIND",
    "TRENT",
    "SOLARINDS",
    "TITAN",
    "NAUKRI",
    "KSB",
    "FACT",
    "CHENNPETRO",
    "MAXHEALTH",
    "IRCON",
    "GNFC",
    "JUSTDIAL",
    "SBFC",
    "OBEROIRLTY",
    "PNCINFRA",
    "NIACL",
    "ADANIENT",
    "IBULHSGFIN",
    "VBL",
    "SBICARD",
    "MCX",
    "AMBUJACEM",
    "UTIAMC",
    "RKFORGE",
    "MEDANTA",
    "COALINDIA",
    "IGL",
    "IOB",
    "AUROPHARMA",
    "TATACHEM",
    "CRISIL",
    "CSBBANK",
    "NYKAA",
    "NBCC",
    "IDFCFIRSTB",
    "LICHSGFIN",
    "ROUTE",
    "CESC",
    "ERIS",
    "MRF",
    "NMDC",
    "ALOKINDS",
    "KARURVYSYA",
    "MARUTI",
    "PRESTIGE",
    "PIIND",
    "GLAND",
    "SAREGAMA",
    "AUBANK",
    "GMDCLTD",
    "BAJFINANCE",
    "RADICO",
    "FINCABLES",
    "SAFARI",
    "COLPAL",
    "JYOTHYLAB",
    "PHOENIXLTD",
    "LICI",
    "MAHLIFE",
    "HAVELLS",
    "CAPLIPOINT",
    "IRCTC",
    "PETRONET",
    "SKFINDIA",
    "ALKEM",
    "HINDALCO",
    "CREDITACC",
    "RITES",
    "TVSSCS",
    "EXIDEIND",
    "CONCOR",
    "BATAINDIA",
    "BALRAMCHIN",
    "HDFCBANK",
    "MARICO",
    "TRITURBINE",
    "GAEL",
    "TATACOMM",
    "JSL",
    "JKPAPER",
    "IDEA",
    "HAL",
    "JINDALSTEL",
    "PATANJALI",
    "AVANTIFEED",
    "SUZLON",
    "TITAGARH",
    "ICICIGI",
    "ULTRACEMCO",
    "NHPC",
    "NUVAMA",
    "DRREDDY",
    "RENUKA",
    "CONCORDBIO",
    "RTNINDIA",
    "POLYMED",
    "RELIANCE",
    "SHREECEM",
    "KPRMILL",
    "SUNPHARMA",
    "DOMS",
    "HDFCAMC",
    "ALLCARGO",
    "MMTC",
    "RATNAMANI",
    "RECLTD",
    "HEG",
    "SIEMENS",
    "METROBRAND",
    "AWL",
    "SWSOLAR",
    "JIOFIN",
    "AXISBANK",
    "APOLLOHOSP",
    "ACE",
    "DEVYANI",
    "NATCOPHARM",
    "NAVINFLUOR",
    "CANBK",
    "J&KBANK",
    "NESTLEIND",
    "INDUSINDBK",
    "JKLAKSHMI",
    "PRAJIND",
    "APOLLOTYRE",
    "SIGNATURE",
    "BHEL",
    "SBILIFE",
    "MCDOWELL-N",
    "TATAPOWER",
    "APARINDS",
    "CUMMINSIND",
    "OFSS",
    "ADANIGREEN",
    "BEL",
    "CHALET",
    "TORNTPOWER",
    "GSPL",
    "RCF",
    "RAINBOW",
    "BAJAJFINSV",
    "BEML",
    "KANSAINER",
    "EQUITASBNK",
    "BAJAJHLDNG",
    "TATACONSUM",
    "WELSPUNLIV",
    "GRASIM",
    "AIAENG",
    "PERSISTENT",
    "IRFC",
    "NSLNISP",
    "HFCL",
    "TATASTEEL",
    "PGHH",
    "JSWINFRA",
    "SONATSOFTW",
    "HINDPETRO",
    "NETWORK18",
    "CENTRALBK",
    "GRAPHITE",
    "ICICIBANK",
    "PFC",
    "UBL",
    "TANLA",
    "PAGEIND",
    "HAPPYFORGE",
    "RVNL",
    "ASTERDM",
    "GICRE",
    "CLEAN",
    "PCBL",
    "COCHINSHIP",
    "FSL",
    "KFINTECH",
    "MAPMYINDIA",
    "MTARTECH",
    "OIL",
    "WHIRLPOOL",
    "GRINDWELL",
    "OLECTRA",
    "BALAMINES",
    "DIVISLAB",
    "APLLTD",
    "AETHER",
    "LT",
    "SCHAEFFLER",
    "SUVENPHAR",
    "CCL",
    "KAJARIACER",
    "EASEMYTRIP",
    "BDL",
    "CERA",
    "VIPIND",
    "CRAFTSMAN",
    "KIMS",
    "HCLTECH",
    "LODHA",
    "BRITANNIA",
    "NUVOCO",
    "UNIONBANK",
    "DMART",
    "HONASA",
    "IDBI",
    "BLS",
    "TATATECH",
    "HUDCO",
    "CIEINDIA",
    "GODREJCP",
    "GAIL",
    "KNRCON",
    "EPL",
    "DALBHARAT",
    "ZFCVINDIA",
    "TTML",
    "ISEC",
    "BANKINDIA",
    "YESBANK",
    "GUJGASLTD",
    "TVSMOTOR",
    "SUNTECK",
    "ITI",
    "CARBORUNIV",
    "BBTC",
    "HAPPSTMNDS",
    "MOTILALOFS",
    "ATGL",
    "GLAXO",
    "RAILTEL",
    "SRF",
    "DABUR",
    "BAYERCROP",
    "CHEMPLASTS",
    "SBIN",
    "COROMANDEL",
    "TECHM",
    "GPPL",
    "TMB",
    "SUMICHEM",
    "INDIGO",
    "3MINDIA",
    "M&MFIN",
    "STARHEALTH",
    "SHRIRAMFIN",
    "FDC",
    "MAZDOCK",
    "CGPOWER",
    "MPHASIS",
    "TATAELXSI",
    "PVRINOX",
    "MAHSEAMLES",
    "GMMPFAUDLR",
    "SCHNEIDER",
    "MHRIL",
    "CENTURYTEX",
    "LTTS",
    "SUNDRMFAST",
    "APLAPOLLO",
    "TRIVENI",
    "LTF",
    "M&M",
    "INDIANB",
    "BORORENEW",
    "CELLO",
    "WIPRO",
    "ASAHIINDIA",
    "ZEEL",
    "INFY",
    "EMAMILTD",
    "ANURAS",
    "ALKYLAMINE",
    "HSCL",
    "CHOLAHLDNG",
    "EIDPARRY",
    "NAM-INDIA",
    "LXCHEM",
    "DLF",
    "WESTLIFE",
    "TATAINVEST",
    "DEEPAKFERT",
    "GLS",
    "BHARATFORG",
    "BLUEDART",
    "CAMPUS",
    "INDHOTEL",
    "KOTAKBANK",
    "JKCEMENT",
    "LTIM",
    "DATAPATTNS",
    "AJANTPHARM",
    "MRPL",
    "CIPLA",
    "DCMSHRIRAM",
    "TIMKEN",
    "ELECON",
    "BIRLACORPN",
    "SWANENERGY",
    "MSUMI",
    "ECLERX",
    "KEC",
    "KRBL",
    "TCS",
    "BRIGADE",
    "MASTEK",
    "CROMPTON",
    "SANOFI",
    "GODREJIND",
    "KPITTECH",
    "MGL",
    "LEMONTREE",
    "INDIGOPNTS",
    "ADANIPOWER",
    "GILLETTE",
    "KPIL",
    "CYIENT",
    "ARE&M",
    "AMBER",
    "GODFRYPHLP",
    "BSE",
    "PRSMJOHNSN",
    "ACC",
    "POWERINDIA",
    "VAIBHAVGBL",
    "INOXWIND",
    "CEATLTD",
    "GODREJPROP",
    "FORTIS",
    "PNBHOUSING",
    "SUPREMEIND",
    "CDSL",
    "SONACOMS",
    "POLICYBZR",
    "BANKBARODA",
    "SOBHA",
    "WELCORP",
    "BSOFT",
    "HOMEFIRST",
    "IRB",
    "JAIBALAJI",
    "INTELLECT",
]

# Create a list of Stock objects
stock_objects = [Stock(symbol) for symbol in nifty_500_stocks]