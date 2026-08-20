/**
 * Taiwan Driver & Rider Prep Web App - Dual Module Engine
 * Sheppard Air Style Accelerated Learning System + Interactive Practice
 */

// STATE MANAGEMENT
let allQuestions = [];
let filteredQuestions = [];
let cheatSheetData = [];

let currentModule = 'motorcycle'; // 'motorcycle' or 'car'
let currentIndex = 0;
let currentTab = 'mode0'; // mode0, sheppard1, sheppard2, interactive, practice, bookmarks, failed, cheatsheet
let selectedCategory = 'ALL';
let selectedTopic = 'ALL_TOPICS';
let searchQuery = '';

// Interactive Quiz state per question
let interactiveAnswered = {}; // qId -> selectedIndex
let bookmarksAnswered = {}; // qId -> selectedIndex

// User Profile Data structure stored in localStorage
let activeProfile = 'diego';
let userState = {
  "diego": {
    "name": "Diego (Pilot Mode)",
    "motorcycle": {
      "bookmarks": [],
      "failedQuestions": [],
      "studiedQuestions": [
        1,
        2,
        3
      ],
      "examHistory": [],
      "lastIndices": {
        "sheppard1": 0,
        "sheppard2": 0,
        "interactive": 0,
        "mode0": 0,
        "bookmarks": 0,
        "failed": 0
      }
    },
    "car": {
      "bookmarks": [
        "CAR_0046",
        "CAR_0058",
        "CAR_0071",
        "CAR_0087",
        "CAR_0090",
        "CAR_0091",
        "CAR_0100",
        "CAR_0111",
        "CAR_0128",
        "CAR_0133",
        "CAR_0158",
        "CAR_0164",
        "CAR_0166",
        "CAR_0175",
        "CAR_0182",
        "CAR_0183",
        "CAR_0184",
        "CAR_0185",
        "CAR_0186",
        "CAR_0190",
        "CAR_0200",
        "CAR_0201",
        "CAR_0203",
        "CAR_0204",
        "CAR_0211",
        "CAR_0213",
        "CAR_0220",
        "CAR_0230",
        "CAR_0232",
        "CAR_0233",
        "CAR_0234",
        "CAR_0236",
        "CAR_0239",
        "CAR_0240",
        "CAR_0241",
        "CAR_0243",
        "CAR_0245",
        "CAR_0246",
        "CAR_0250",
        "CAR_0251",
        "CAR_0258",
        "CAR_0259",
        "CAR_0260",
        "CAR_0263",
        "CAR_0266",
        "CAR_0268",
        "CAR_0272",
        "CAR_0274",
        "CAR_0275",
        "CAR_0278",
        "CAR_0282",
        "CAR_0286",
        "CAR_0287",
        "CAR_0296",
        "CAR_0298",
        "CAR_0299",
        "CAR_0302",
        "CAR_0304",
        "CAR_0308",
        "CAR_0316",
        "CAR_0328",
        "CAR_0330",
        "CAR_0333",
        "CAR_0335",
        "CAR_0344",
        "CAR_0353",
        "CAR_0354",
        "CAR_0356",
        "CAR_0365",
        "CAR_0374",
        "CAR_0376",
        "CAR_0377",
        "CAR_0382",
        "CAR_0389",
        "CAR_0396",
        "CAR_0401",
        "CAR_0405",
        "CAR_0419",
        "CAR_0425",
        "CAR_0426",
        "CAR_0427",
        "CAR_0431",
        "CAR_0452",
        "CAR_0453",
        "CAR_0464",
        "CAR_0470",
        "CAR_0484",
        "CAR_0494",
        "CAR_0506",
        "CAR_0512",
        "CAR_0519",
        "CAR_0532",
        "CAR_0538",
        "CAR_0558",
        "CAR_0564",
        "CAR_0568",
        "CAR_0569",
        "CAR_0572",
        "CAR_0594",
        "CAR_0601",
        "CAR_0769",
        "CAR_0799",
        "CAR_0863",
        "CAR_0916",
        "CAR_0976",
        "CAR_1020",
        "CAR_1068",
        "CAR_1084",
        "CAR_0720",
        "CAR_0728",
        "CAR_0736",
        "CAR_0771",
        "CAR_0779",
        "CAR_0780",
        "CAR_0793",
        "CAR_0803",
        "CAR_0820",
        "CAR_0825",
        "CAR_0855",
        "CAR_0859",
        "CAR_0861",
        "CAR_0864",
        "CAR_0871",
        "CAR_0886",
        "CAR_0906",
        "CAR_0911",
        "CAR_0913",
        "CAR_0915",
        "CAR_0919",
        "CAR_0922",
        "CAR_0929",
        "CAR_0931",
        "CAR_0932",
        "CAR_0934",
        "CAR_0937",
        "CAR_0940",
        "CAR_0942",
        "CAR_0955",
        "CAR_0958",
        "CAR_0959",
        "CAR_0961",
        "CAR_0963",
        "CAR_0969",
        "CAR_0972",
        "CAR_0975",
        "CAR_0980",
        "CAR_0985",
        "CAR_0990",
        "CAR_1011",
        "CAR_1029",
        "CAR_1030",
        "CAR_1035",
        "CAR_1054",
        "CAR_1076",
        "CAR_1077",
        "CAR_0116"
      ],
      "failedQuestions": [
        "CAR_0825",
        "CAR_0003",
        "CAR_0820"
      ],
      "studiedQuestions": [
        "CAR_0001",
        "CAR_0002",
        "CAR_0003",
        "CAR_0004",
        "CAR_0005",
        "CAR_0006",
        "CAR_0007",
        "CAR_0008",
        "CAR_0009",
        "CAR_0010",
        "CAR_0011",
        "CAR_0012",
        "CAR_0013",
        "CAR_0014",
        "CAR_0015",
        "CAR_0016",
        "CAR_0017",
        "CAR_0018",
        "CAR_0019",
        "CAR_0020",
        "CAR_0021",
        "CAR_0022",
        "CAR_0023",
        "CAR_0024",
        "CAR_0025",
        "CAR_0026",
        "CAR_0027",
        "CAR_0028",
        "CAR_0029",
        "CAR_0030",
        "CAR_0031",
        "CAR_0032",
        "CAR_0033",
        "CAR_0034",
        "CAR_0035",
        "CAR_0036",
        "CAR_0037",
        "CAR_0038",
        "CAR_0039",
        "CAR_0040",
        "CAR_0041",
        "CAR_0042",
        "CAR_0043",
        "CAR_0044",
        "CAR_0045",
        "CAR_0046",
        "CAR_0047",
        "CAR_0048",
        "CAR_0049",
        "CAR_0050",
        "CAR_0051",
        "CAR_0052",
        "CAR_0053",
        "CAR_0054",
        "CAR_0055",
        "CAR_0056",
        "CAR_0057",
        "CAR_0058",
        "CAR_0059",
        "CAR_0060",
        "CAR_0061",
        "CAR_0062",
        "CAR_0063",
        "CAR_0064",
        "CAR_0065",
        "CAR_0066",
        "CAR_0067",
        "CAR_0068",
        "CAR_0069",
        "CAR_0070",
        "CAR_0071",
        "CAR_0072",
        "CAR_0073",
        "CAR_0074",
        "CAR_0075",
        "CAR_0076",
        "CAR_0077",
        "CAR_0078",
        "CAR_0079",
        "CAR_0080",
        "CAR_0081",
        "CAR_0082",
        "CAR_0083",
        "CAR_0084",
        "CAR_0085",
        "CAR_0086",
        "CAR_0087",
        "CAR_0088",
        "CAR_0089",
        "CAR_0090",
        "CAR_0091",
        "CAR_0092",
        "CAR_0093",
        "CAR_0094",
        "CAR_0095",
        "CAR_0096",
        "CAR_0097",
        "CAR_0098",
        "CAR_0099",
        "CAR_0100",
        "CAR_0101",
        "CAR_0102",
        "CAR_0103",
        "CAR_0104",
        "CAR_0105",
        "CAR_0106",
        "CAR_0107",
        "CAR_0108",
        "CAR_0109",
        "CAR_0110",
        "CAR_0111",
        "CAR_0112",
        "CAR_0113",
        "CAR_0114",
        "CAR_0115",
        "CAR_0116",
        "CAR_0117",
        "CAR_0118",
        "CAR_0119",
        "CAR_0120",
        "CAR_0121",
        "CAR_0122",
        "CAR_0123",
        "CAR_0124",
        "CAR_0125",
        "CAR_0126",
        "CAR_0127",
        "CAR_0128",
        "CAR_0129",
        "CAR_0130",
        "CAR_0131",
        "CAR_0132",
        "CAR_0133",
        "CAR_0134",
        "CAR_0135",
        "CAR_0136",
        "CAR_0137",
        "CAR_0138",
        "CAR_0139",
        "CAR_0140",
        "CAR_0141",
        "CAR_0142",
        "CAR_0143",
        "CAR_0144",
        "CAR_0145",
        "CAR_0146",
        "CAR_0147",
        "CAR_0148",
        "CAR_0149",
        "CAR_0150",
        "CAR_0151",
        "CAR_0152",
        "CAR_0153",
        "CAR_0154",
        "CAR_0155",
        "CAR_0156",
        "CAR_0157",
        "CAR_0158",
        "CAR_0159",
        "CAR_0160",
        "CAR_0161",
        "CAR_0162",
        "CAR_0163",
        "CAR_0164",
        "CAR_0165",
        "CAR_0166",
        "CAR_0167",
        "CAR_0168",
        "CAR_0169",
        "CAR_0170",
        "CAR_0171",
        "CAR_0172",
        "CAR_0173",
        "CAR_0174",
        "CAR_0175",
        "CAR_0176",
        "CAR_0177",
        "CAR_0178",
        "CAR_0179",
        "CAR_0180",
        "CAR_0181",
        "CAR_0182",
        "CAR_0183",
        "CAR_0184",
        "CAR_0185",
        "CAR_0186",
        "CAR_0187",
        "CAR_0188",
        "CAR_0189",
        "CAR_0190",
        "CAR_0191",
        "CAR_0192",
        "CAR_0193",
        "CAR_0194",
        "CAR_0195",
        "CAR_0196",
        "CAR_0197",
        "CAR_0198",
        "CAR_0199",
        "CAR_0200",
        "CAR_0201",
        "CAR_0202",
        "CAR_0203",
        "CAR_0204",
        "CAR_0205",
        "CAR_0206",
        "CAR_0207",
        "CAR_0208",
        "CAR_0209",
        "CAR_0210",
        "CAR_0211",
        "CAR_0212",
        "CAR_0213",
        "CAR_0214",
        "CAR_0215",
        "CAR_0216",
        "CAR_0217",
        "CAR_0218",
        "CAR_0219",
        "CAR_0220",
        "CAR_0221",
        "CAR_0222",
        "CAR_0223",
        "CAR_0224",
        "CAR_0225",
        "CAR_0226",
        "CAR_0227",
        "CAR_0228",
        "CAR_0229",
        "CAR_0230",
        "CAR_0231",
        "CAR_0232",
        "CAR_0233",
        "CAR_0234",
        "CAR_0235",
        "CAR_0236",
        "CAR_0237",
        "CAR_0238",
        "CAR_0239",
        "CAR_0240",
        "CAR_0241",
        "CAR_0242",
        "CAR_0243",
        "CAR_0244",
        "CAR_0245",
        "CAR_0246",
        "CAR_0247",
        "CAR_0248",
        "CAR_0249",
        "CAR_0250",
        "CAR_0251",
        "CAR_0252",
        "CAR_0253",
        "CAR_0254",
        "CAR_0255",
        "CAR_0256",
        "CAR_0257",
        "CAR_0258",
        "CAR_0259",
        "CAR_0260",
        "CAR_0261",
        "CAR_0262",
        "CAR_0263",
        "CAR_0264",
        "CAR_0265",
        "CAR_0266",
        "CAR_0267",
        "CAR_0268",
        "CAR_0269",
        "CAR_0270",
        "CAR_0271",
        "CAR_0272",
        "CAR_0273",
        "CAR_0274",
        "CAR_0275",
        "CAR_0276",
        "CAR_0277",
        "CAR_0278",
        "CAR_0279",
        "CAR_0280",
        "CAR_0281",
        "CAR_0282",
        "CAR_0283",
        "CAR_0284",
        "CAR_0285",
        "CAR_0286",
        "CAR_0287",
        "CAR_0288",
        "CAR_0289",
        "CAR_0290",
        "CAR_0291",
        "CAR_0292",
        "CAR_0293",
        "CAR_0294",
        "CAR_0295",
        "CAR_0296",
        "CAR_0297",
        "CAR_0298",
        "CAR_0299",
        "CAR_0300",
        "CAR_0301",
        "CAR_0302",
        "CAR_0303",
        "CAR_0304",
        "CAR_0305",
        "CAR_0306",
        "CAR_0307",
        "CAR_0308",
        "CAR_0309",
        "CAR_0310",
        "CAR_0311",
        "CAR_0312",
        "CAR_0313",
        "CAR_0314",
        "CAR_0315",
        "CAR_0316",
        "CAR_0317",
        "CAR_0318",
        "CAR_0319",
        "CAR_0320",
        "CAR_0321",
        "CAR_0322",
        "CAR_0323",
        "CAR_0324",
        "CAR_0325",
        "CAR_0326",
        "CAR_0327",
        "CAR_0328",
        "CAR_0329",
        "CAR_0330",
        "CAR_0331",
        "CAR_0332",
        "CAR_0333",
        "CAR_0334",
        "CAR_0335",
        "CAR_0336",
        "CAR_0337",
        "CAR_0338",
        "CAR_0339",
        "CAR_0340",
        "CAR_0341",
        "CAR_0342",
        "CAR_0343",
        "CAR_0344",
        "CAR_0345",
        "CAR_0346",
        "CAR_0347",
        "CAR_0348",
        "CAR_0349",
        "CAR_0350",
        "CAR_0351",
        "CAR_0352",
        "CAR_0353",
        "CAR_0354",
        "CAR_0355",
        "CAR_0356",
        "CAR_0357",
        "CAR_0358",
        "CAR_0359",
        "CAR_0360",
        "CAR_0361",
        "CAR_0362",
        "CAR_0363",
        "CAR_0364",
        "CAR_0365",
        "CAR_0366",
        "CAR_0367",
        "CAR_0368",
        "CAR_0369",
        "CAR_0370",
        "CAR_0371",
        "CAR_0372",
        "CAR_0373",
        "CAR_0374",
        "CAR_0375",
        "CAR_0376",
        "CAR_0377",
        "CAR_0378",
        "CAR_0379",
        "CAR_0380",
        "CAR_0381",
        "CAR_0382",
        "CAR_0383",
        "CAR_0384",
        "CAR_0385",
        "CAR_0386",
        "CAR_0387",
        "CAR_0388",
        "CAR_0389",
        "CAR_0390",
        "CAR_0391",
        "CAR_0392",
        "CAR_0393",
        "CAR_0394",
        "CAR_0395",
        "CAR_0396",
        "CAR_0397",
        "CAR_0398",
        "CAR_0399",
        "CAR_0400",
        "CAR_0401",
        "CAR_0402",
        "CAR_0403",
        "CAR_0404",
        "CAR_0405",
        "CAR_0406",
        "CAR_0407",
        "CAR_0408",
        "CAR_0409",
        "CAR_0410",
        "CAR_0411",
        "CAR_0412",
        "CAR_0413",
        "CAR_0414",
        "CAR_0415",
        "CAR_0416",
        "CAR_0417",
        "CAR_0418",
        "CAR_0419",
        "CAR_0420",
        "CAR_0421",
        "CAR_0422",
        "CAR_0423",
        "CAR_0424",
        "CAR_0425",
        "CAR_0426",
        "CAR_0427",
        "CAR_0428",
        "CAR_0429",
        "CAR_0430",
        "CAR_0431",
        "CAR_0432",
        "CAR_0433",
        "CAR_0434",
        "CAR_0435",
        "CAR_0436",
        "CAR_0437",
        "CAR_0438",
        "CAR_0439",
        "CAR_0440",
        "CAR_0441",
        "CAR_0442",
        "CAR_0443",
        "CAR_0444",
        "CAR_0445",
        "CAR_0446",
        "CAR_0447",
        "CAR_0448",
        "CAR_0449",
        "CAR_0450",
        "CAR_0451",
        "CAR_0452",
        "CAR_0453",
        "CAR_0454",
        "CAR_0455",
        "CAR_0456",
        "CAR_0457",
        "CAR_0458",
        "CAR_0459",
        "CAR_0460",
        "CAR_0461",
        "CAR_0462",
        "CAR_0463",
        "CAR_0464",
        "CAR_0465",
        "CAR_0466",
        "CAR_0467",
        "CAR_0468",
        "CAR_0469",
        "CAR_0470",
        "CAR_0471",
        "CAR_0472",
        "CAR_0473",
        "CAR_0474",
        "CAR_0475",
        "CAR_0476",
        "CAR_0477",
        "CAR_0478",
        "CAR_0479",
        "CAR_0480",
        "CAR_0481",
        "CAR_0482",
        "CAR_0483",
        "CAR_0484",
        "CAR_0485",
        "CAR_0486",
        "CAR_0487",
        "CAR_0488",
        "CAR_0489",
        "CAR_0490",
        "CAR_0491",
        "CAR_0492",
        "CAR_0493",
        "CAR_0494",
        "CAR_0495",
        "CAR_0496",
        "CAR_0497",
        "CAR_0498",
        "CAR_0499",
        "CAR_0500",
        "CAR_0501",
        "CAR_0502",
        "CAR_0503",
        "CAR_0504",
        "CAR_0505",
        "CAR_0506",
        "CAR_0507",
        "CAR_0508",
        "CAR_0509",
        "CAR_0510",
        "CAR_0511",
        "CAR_0512",
        "CAR_0513",
        "CAR_0514",
        "CAR_0515",
        "CAR_0516",
        "CAR_0517",
        "CAR_0518",
        "CAR_0519",
        "CAR_0520",
        "CAR_0521",
        "CAR_0522",
        "CAR_0523",
        "CAR_0524",
        "CAR_0525",
        "CAR_0526",
        "CAR_0527",
        "CAR_0528",
        "CAR_0529",
        "CAR_0530",
        "CAR_0531",
        "CAR_0532",
        "CAR_0533",
        "CAR_0534",
        "CAR_0535",
        "CAR_0536",
        "CAR_0537",
        "CAR_0538",
        "CAR_0539",
        "CAR_0540",
        "CAR_0541",
        "CAR_0542",
        "CAR_0543",
        "CAR_0544",
        "CAR_0545",
        "CAR_0546",
        "CAR_0547",
        "CAR_0548",
        "CAR_0549",
        "CAR_0550",
        "CAR_0551",
        "CAR_0552",
        "CAR_0553",
        "CAR_0554",
        "CAR_0555",
        "CAR_0556",
        "CAR_0557",
        "CAR_0558",
        "CAR_0559",
        "CAR_0560",
        "CAR_0561",
        "CAR_0562",
        "CAR_0563",
        "CAR_0564",
        "CAR_0565",
        "CAR_0566",
        "CAR_0567",
        "CAR_0568",
        "CAR_0569",
        "CAR_0570",
        "CAR_0571",
        "CAR_0572",
        "CAR_0573",
        "CAR_0574",
        "CAR_0575",
        "CAR_0576",
        "CAR_0577",
        "CAR_0578",
        "CAR_0579",
        "CAR_0580",
        "CAR_0581",
        "CAR_0582",
        "CAR_0583",
        "CAR_0584",
        "CAR_0585",
        "CAR_0586",
        "CAR_0587",
        "CAR_0588",
        "CAR_0589",
        "CAR_0590",
        "CAR_0591",
        "CAR_0592",
        "CAR_0593",
        "CAR_0594",
        "CAR_0595",
        "CAR_0596",
        "CAR_0597",
        "CAR_0598",
        "CAR_0599",
        "CAR_0600",
        "CAR_0601",
        "CAR_0602",
        "CAR_0603",
        "CAR_0604",
        "CAR_0605",
        "CAR_0606",
        "CAR_0607",
        "CAR_0608",
        "CAR_0609",
        "CAR_0610",
        "CAR_0611",
        "CAR_0612",
        "CAR_0613",
        "CAR_0614",
        "CAR_0615",
        "CAR_0616",
        "CAR_0617",
        "CAR_0618",
        "CAR_0619",
        "CAR_0620",
        "CAR_0621",
        "CAR_0622",
        "CAR_0623",
        "CAR_0624",
        "CAR_0625",
        "CAR_0626",
        "CAR_0627",
        "CAR_0628",
        "CAR_0629",
        "CAR_0630",
        "CAR_0631",
        "CAR_0632",
        "CAR_0633",
        "CAR_0634",
        "CAR_0635",
        "CAR_0636",
        "CAR_0637",
        "CAR_0638",
        "CAR_0639",
        "CAR_0640",
        "CAR_0641",
        "CAR_0642",
        "CAR_0643",
        "CAR_0644",
        "CAR_0645",
        "CAR_0646",
        "CAR_0647",
        "CAR_0648",
        "CAR_0649",
        "CAR_0650",
        "CAR_0651",
        "CAR_0652",
        "CAR_0653",
        "CAR_0654",
        "CAR_0655",
        "CAR_0656",
        "CAR_0657",
        "CAR_0658",
        "CAR_0659",
        "CAR_0660",
        "CAR_0661",
        "CAR_0662",
        "CAR_0663",
        "CAR_0664",
        "CAR_0665",
        "CAR_0666",
        "CAR_0667",
        "CAR_0668",
        "CAR_0669",
        "CAR_0670",
        "CAR_0671",
        "CAR_0672",
        "CAR_0673",
        "CAR_0674",
        "CAR_0675",
        "CAR_0676",
        "CAR_0677",
        "CAR_0678",
        "CAR_0679",
        "CAR_0680",
        "CAR_0681",
        "CAR_0682",
        "CAR_0683",
        "CAR_0684",
        "CAR_0685",
        "CAR_0686",
        "CAR_0687",
        "CAR_0688",
        "CAR_0689",
        "CAR_0690",
        "CAR_0691",
        "CAR_0692",
        "CAR_0693",
        "CAR_0694",
        "CAR_0695",
        "CAR_0696",
        "CAR_0697",
        "CAR_0698",
        "CAR_0699",
        "CAR_0700",
        "CAR_0701",
        "CAR_0702",
        "CAR_0703",
        "CAR_0704",
        "CAR_0705",
        "CAR_0706",
        "CAR_0707",
        "CAR_0708",
        "CAR_0709",
        "CAR_0710",
        "CAR_0711",
        "CAR_0712",
        "CAR_0713",
        "CAR_0714",
        "CAR_0715",
        "CAR_0716",
        "CAR_0717",
        "CAR_0718",
        "CAR_0719",
        "CAR_0720",
        "CAR_0721",
        "CAR_0722",
        "CAR_0723",
        "CAR_0724",
        "CAR_0725",
        "CAR_0726",
        "CAR_0727",
        "CAR_0728",
        "CAR_0729",
        "CAR_0730",
        "CAR_0731",
        "CAR_0732",
        "CAR_0733",
        "CAR_0734",
        "CAR_0735",
        "CAR_0736",
        "CAR_0737",
        "CAR_0738",
        "CAR_0739",
        "CAR_0740",
        "CAR_0741",
        "CAR_0742",
        "CAR_0743",
        "CAR_0744",
        "CAR_0745",
        "CAR_0746",
        "CAR_0747",
        "CAR_0748",
        "CAR_0749",
        "CAR_0750",
        "CAR_0751",
        "CAR_0752",
        "CAR_0753",
        "CAR_0754",
        "CAR_0755",
        "CAR_0756",
        "CAR_0757",
        "CAR_0758",
        "CAR_0759",
        "CAR_0760",
        "CAR_0761",
        "CAR_0762",
        "CAR_0763",
        "CAR_0764",
        "CAR_0765",
        "CAR_0766",
        "CAR_0767",
        "CAR_0768",
        "CAR_0769",
        "CAR_0770",
        "CAR_0771",
        "CAR_0772",
        "CAR_0773",
        "CAR_0774",
        "CAR_0775",
        "CAR_0776",
        "CAR_0777",
        "CAR_0778",
        "CAR_0779",
        "CAR_0780",
        "CAR_0781",
        "CAR_0782",
        "CAR_0783",
        "CAR_0784",
        "CAR_0785",
        "CAR_0786",
        "CAR_0787",
        "CAR_0788",
        "CAR_0789",
        "CAR_0790",
        "CAR_0791",
        "CAR_0792",
        "CAR_0793",
        "CAR_0794",
        "CAR_0795",
        "CAR_0796",
        "CAR_0797",
        "CAR_0798",
        "CAR_0799",
        "CAR_0800",
        "CAR_0801",
        "CAR_0802",
        "CAR_0803",
        "CAR_0804",
        "CAR_0805",
        "CAR_0806",
        "CAR_0807",
        "CAR_0808",
        "CAR_0809",
        "CAR_0810",
        "CAR_0811",
        "CAR_0812",
        "CAR_0813",
        "CAR_0814",
        "CAR_0815",
        "CAR_0816",
        "CAR_0817",
        "CAR_0818",
        "CAR_0819",
        "CAR_0820",
        "CAR_0821",
        "CAR_0822",
        "CAR_0823",
        "CAR_0824",
        "CAR_0825",
        "CAR_0826",
        "CAR_0827",
        "CAR_0828",
        "CAR_0829",
        "CAR_0830",
        "CAR_0831",
        "CAR_0832",
        "CAR_0833",
        "CAR_0834",
        "CAR_0835",
        "CAR_0836",
        "CAR_0837",
        "CAR_0838",
        "CAR_0839",
        "CAR_0840",
        "CAR_0841",
        "CAR_0842",
        "CAR_0843",
        "CAR_0844",
        "CAR_0845",
        "CAR_0846",
        "CAR_0847",
        "CAR_0848",
        "CAR_0849",
        "CAR_0850",
        "CAR_0851",
        "CAR_0852",
        "CAR_0853",
        "CAR_0854",
        "CAR_0855",
        "CAR_0856",
        "CAR_0857",
        "CAR_0858",
        "CAR_0859",
        "CAR_0860",
        "CAR_0861",
        "CAR_0862",
        "CAR_0863",
        "CAR_0864",
        "CAR_0865",
        "CAR_0866",
        "CAR_0867",
        "CAR_0868",
        "CAR_0869",
        "CAR_0870",
        "CAR_0871",
        "CAR_0872",
        "CAR_0873",
        "CAR_0874",
        "CAR_0875",
        "CAR_0876",
        "CAR_0877",
        "CAR_0878",
        "CAR_0879",
        "CAR_0880",
        "CAR_0881",
        "CAR_0882",
        "CAR_0883",
        "CAR_0884",
        "CAR_0885",
        "CAR_0886",
        "CAR_0887",
        "CAR_0888",
        "CAR_0889",
        "CAR_0890",
        "CAR_0891",
        "CAR_0892",
        "CAR_0893",
        "CAR_0894",
        "CAR_0895",
        "CAR_0896",
        "CAR_0897",
        "CAR_0898",
        "CAR_0899",
        "CAR_0900",
        "CAR_0901",
        "CAR_0902",
        "CAR_0903",
        "CAR_0904",
        "CAR_0905",
        "CAR_0906",
        "CAR_0907",
        "CAR_0908",
        "CAR_0909",
        "CAR_0910",
        "CAR_0911",
        "CAR_0912",
        "CAR_0913",
        "CAR_0914",
        "CAR_0915",
        "CAR_0916",
        "CAR_0917",
        "CAR_0918",
        "CAR_0919",
        "CAR_0920",
        "CAR_0921",
        "CAR_0922",
        "CAR_0923",
        "CAR_0924",
        "CAR_0925",
        "CAR_0926",
        "CAR_0927",
        "CAR_0928",
        "CAR_0929",
        "CAR_0930",
        "CAR_0931",
        "CAR_0932",
        "CAR_0933",
        "CAR_0934",
        "CAR_0935",
        "CAR_0936",
        "CAR_0937",
        "CAR_0938",
        "CAR_0939",
        "CAR_0940",
        "CAR_0941",
        "CAR_0942",
        "CAR_0943",
        "CAR_0944",
        "CAR_0945",
        "CAR_0946",
        "CAR_0947",
        "CAR_0948",
        "CAR_0949",
        "CAR_0950",
        "CAR_0951",
        "CAR_0952",
        "CAR_0953",
        "CAR_0954",
        "CAR_0955",
        "CAR_0956",
        "CAR_0957",
        "CAR_0958",
        "CAR_0959",
        "CAR_0960",
        "CAR_0961",
        "CAR_0962",
        "CAR_0963",
        "CAR_0964",
        "CAR_0965",
        "CAR_0966",
        "CAR_0967",
        "CAR_0968",
        "CAR_0969",
        "CAR_0970",
        "CAR_0971",
        "CAR_0972",
        "CAR_0973",
        "CAR_0974",
        "CAR_0975",
        "CAR_0976",
        "CAR_0977",
        "CAR_0978",
        "CAR_0979",
        "CAR_0980",
        "CAR_0981",
        "CAR_0982",
        "CAR_0983",
        "CAR_0984",
        "CAR_0985",
        "CAR_0986",
        "CAR_0987",
        "CAR_0988",
        "CAR_0989",
        "CAR_0990",
        "CAR_0991",
        "CAR_0992",
        "CAR_0993",
        "CAR_0994",
        "CAR_0995",
        "CAR_0996",
        "CAR_0997",
        "CAR_0998",
        "CAR_0999",
        "CAR_1000",
        "CAR_1001",
        "CAR_1002",
        "CAR_1003",
        "CAR_1004",
        "CAR_1005",
        "CAR_1006",
        "CAR_1007",
        "CAR_1008",
        "CAR_1009",
        "CAR_1010",
        "CAR_1011",
        "CAR_1012",
        "CAR_1013",
        "CAR_1014",
        "CAR_1015",
        "CAR_1016",
        "CAR_1017",
        "CAR_1018",
        "CAR_1019",
        "CAR_1020",
        "CAR_1021",
        "CAR_1022",
        "CAR_1023",
        "CAR_1024",
        "CAR_1025",
        "CAR_1026",
        "CAR_1027",
        "CAR_1028",
        "CAR_1029",
        "CAR_1030",
        "CAR_1031",
        "CAR_1032",
        "CAR_1033",
        "CAR_1034",
        "CAR_1035",
        "CAR_1036",
        "CAR_1037",
        "CAR_1038",
        "CAR_1039",
        "CAR_1040",
        "CAR_1041",
        "CAR_1042",
        "CAR_1043",
        "CAR_1044",
        "CAR_1045",
        "CAR_1046",
        "CAR_1047",
        "CAR_1048",
        "CAR_1049",
        "CAR_1050",
        "CAR_1051",
        "CAR_1052",
        "CAR_1053",
        "CAR_1054",
        "CAR_1055",
        "CAR_1056",
        "CAR_1057",
        "CAR_1058",
        "CAR_1059",
        "CAR_1060",
        "CAR_1061",
        "CAR_1062",
        "CAR_1063",
        "CAR_1064",
        "CAR_1065",
        "CAR_1066",
        "CAR_1067",
        "CAR_1068",
        "CAR_1069",
        "CAR_1070",
        "CAR_1071",
        "CAR_1072",
        "CAR_1073",
        "CAR_1074",
        "CAR_1075",
        "CAR_1076",
        "CAR_1077",
        "CAR_1078",
        "CAR_1079",
        "CAR_1080",
        "CAR_1081",
        "CAR_1082",
        "CAR_1083",
        "CAR_1084",
        "CAR_1085",
        "CAR_1086",
        "CAR_1087",
        "CAR_1088",
        "CAR_1089",
        "CAR_1090"
      ],
      "examHistory": [],
      "lastIndices": {
        "sheppard1": 1089,
        "sheppard2": 823,
        "interactive": 823,
        "mode0": 0,
        "bookmarks": 19,
        "failed": 2
      }
    }
  },
  "johana": {
    "name": "Johana (Study Profile)",
    "motorcycle": {
      "bookmarks": [],
      "failedQuestions": [],
      "studiedQuestions": [],
      "examHistory": [],
      "lastIndices": {
        "sheppard1": 0,
        "sheppard2": 0,
        "interactive": 0,
        "mode0": 0,
        "bookmarks": 0,
        "failed": 0
      }
    },
    "car": {
      "bookmarks": [],
      "failedQuestions": [],
      "studiedQuestions": [],
      "examHistory": [],
      "lastIndices": {
        "sheppard1": 0,
        "sheppard2": 0,
        "interactive": 0,
        "mode0": 0,
        "bookmarks": 0,
        "failed": 0
      }
    }
  },
  "alejandro": {
    "name": "Alejandro (Study Profile)",
    "motorcycle": {
      "bookmarks": [],
      "failedQuestions": [],
      "studiedQuestions": [],
      "examHistory": [],
      "lastIndices": {
        "sheppard1": 0,
        "sheppard2": 0,
        "interactive": 0,
        "mode0": 0,
        "bookmarks": 0,
        "failed": 0
      }
    },
    "car": {
      "bookmarks": [],
      "failedQuestions": [],
      "studiedQuestions": [],
      "examHistory": [],
      "lastIndices": {
        "sheppard1": 0,
        "sheppard2": 0,
        "interactive": 0,
        "mode0": 0,
        "bookmarks": 0,
        "failed": 0
      }
    }
  },
  "last_updated": 1787163500000
};

// Practice Exam State
let examQuestions = [];
let examUserAnswers = {}; // qId -> optionIndex
let examSubmitted = false;

// INITIALIZATION
document.addEventListener('DOMContentLoaded', async () => {
  loadProfileFromStorage();
  const savedMod = localStorage.getItem('tw_driver_active_module') || 'car';
  currentModule = savedMod;
  const modSelect = document.getElementById('moduleSelect');
  if (modSelect) modSelect.value = currentModule;

  await loadModuleData(currentModule);
  setupEventListeners();

  const savedTab = localStorage.getItem('tw_driver_active_tab') || 'sheppard1';
  switchTab(savedTab);
});

let masterRulesData = [];

// LOAD MODULE DATA (Motorcycle vs. Car)
async function loadModuleData(mod) {
  currentModule = mod;
  try {
    const qFile = (mod === 'car') ? 'car_questions.json' : 'questions.json';
    const cFile = (mod === 'car') ? 'car_cheat_sheet.json' : 'cheat_sheet.json';
    const mFile = (mod === 'car') ? 'car_master_rules.json' : 'moto_master_rules.json';

    // Add cachebuster to ensure latest updated explanations are loaded instantly
    const cacheBuster = '?v=20260816_V7_' + Date.now();
    const qResp = await fetch(qFile + cacheBuster);
    allQuestions = await qResp.json();

    // Comprehensive question normalization
    allQuestions.forEach((q, qIndex) => {
      if (q.answer !== undefined) {
        q.correct_index = (typeof q.answer === 'number') ? (q.answer - 1) : (parseInt(q.answer) - 1);
      } else if (q.correct_index === undefined) {
        q.correct_index = 0;
      }
      if (!q.correct_answer && q.options && q.options[q.correct_index]) {
        q.correct_answer = q.options[q.correct_index];
      }
      if (q.image && !q.sign_image) {
        q.sign_image = q.image;
      }
    });

    const cResp = await fetch(cFile + cacheBuster);
    cheatSheetData = await cResp.json();

    const mResp = await fetch(mFile + cacheBuster);
    masterRulesData = await mResp.json();

    updateModuleHeaderUI();
    updateCategoryAndTopicDropdowns();
    updateFilteredQuestions();
  } catch (err) {
    console.error('Error loading module question bank:', err);
  }
}

function updateModuleHeaderUI() {
  const totalCountEl = document.getElementById('dbTotalCountText');
  if (totalCountEl) {
    totalCountEl.textContent = `${allQuestions.length.toLocaleString()} Questions`;
  }
  const brandIcon = document.getElementById('brandIcon');
  if (brandIcon) {
    if (currentModule === 'car') {
      brandIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A2 2 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>`;
    } else {
      brandIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A2 2 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="3"/><circle cx="17" cy="17" r="3"/></svg>`;
    }
  }
}

function updateCategoryAndTopicDropdowns() {
  const catSelect = document.getElementById('categorySelect');
  const topicSelect = document.getElementById('topicSelect');

  if (catSelect) {
    const cats = Array.from(new Set(allQuestions.map(q => q.category))).filter(Boolean);
    catSelect.innerHTML = `<option value="ALL">All Categories (${allQuestions.length} Questions)</option>` +
      cats.map(c => `<option value="${c}">${c}</option>`).join('');
  }

  if (topicSelect) {
    const topics = Array.from(new Set(allQuestions.map(q => q.topic))).filter(Boolean);
    topicSelect.innerHTML = `<option value="ALL_TOPICS">All Subjects / Topics</option>` +
      topics.map(t => `<option value="${t}">${t}</option>`).join('');
  }
}

// ==========================================
// TOAST NOTIFICATIONS & FEEDBACK
// ==========================================
function showToast(msg, isError = false) {
  const existing = document.getElementById('appToastMsg');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.id = 'appToastMsg';
  toast.className = 'toast-msg';
  if (isError) {
    toast.style.backgroundColor = '#ef4444';
  }
  toast.textContent = msg;
  document.body.appendChild(toast);
  setTimeout(() => {
    if (toast && toast.parentNode) toast.remove();
  }, 2600);
}

// ==========================================
// ROBUST MULTI-TIER CLOUD AUTO-SYNC ENGINE
// Bulletproof Non-Destructive Multi-Device Synchronization
// ==========================================
const PRIMARY_CLOUD_ENDPOINT = 'https://taiwan-car-license-default-rtdb.asia-southeast1.firebasedatabase.app/user_sync_state.json';

function getCloudEndpoints() {
  const endpoints = [];
  const custom = localStorage.getItem('tw_driver_custom_cloud_endpoint');
  if (custom && custom.trim()) {
    endpoints.push(custom.trim());
  }

  // If hosted on local/network server with /api/sync
  if (typeof window !== 'undefined' && window.location && window.location.origin && window.location.origin.startsWith('http')) {
    const localApi = window.location.origin + '/api/sync';
    if (!endpoints.includes(localApi)) {
      endpoints.push(localApi);
    }
  }

  if (!endpoints.includes(PRIMARY_CLOUD_ENDPOINT)) {
    endpoints.push(PRIMARY_CLOUD_ENDPOINT);
  }
  return endpoints;
}

let isSyncing = false;
let syncDebounceTimer = null;
let pendingOfflineSync = false;

// Visual Status Update Helper
function updateSyncStatusUI(state, extraInfo = '') {
  const syncBadge = document.getElementById('cloudSyncStatus');
  const syncText = document.getElementById('cloudSyncText');
  const modalText = document.getElementById('cloudModalStatusText');
  if (!syncBadge && !syncText) return;

  const nowStr = extraInfo || new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  if (state === 'online_synced') {
    if (syncBadge) {
      syncBadge.style.background = 'rgba(16, 185, 129, 0.15)';
      syncBadge.style.color = '#34d399';
      syncBadge.style.borderColor = 'rgba(16, 185, 129, 0.3)';
    }
    if (syncText) syncText.textContent = `🟢 Cloud Synced ✓ (${nowStr})`;
    if (modalText) modalText.textContent = `🟢 All study progress fully synchronized with Cloud at ${nowStr}.`;
  } else if (state === 'syncing') {
    if (syncBadge) {
      syncBadge.style.background = 'rgba(99, 102, 241, 0.15)';
      syncBadge.style.color = '#818cf8';
      syncBadge.style.borderColor = 'rgba(99, 102, 241, 0.3)';
    }
    if (syncText) syncText.textContent = '🔵 Syncing...';
  } else if (state === 'offline_flight') {
    if (syncBadge) {
      syncBadge.style.background = 'rgba(245, 158, 11, 0.15)';
      syncBadge.style.color = '#fbbf24';
      syncBadge.style.borderColor = 'rgba(245, 158, 11, 0.3)';
    }
    if (syncText) syncText.textContent = '✈️ Flight Mode (Offline - Saved Locally)';
    if (modalText) modalText.textContent = '✈️ Offline Mode: All questions, answers & bookmarks saved securely in local storage. Auto-sync queued for landing reconnection.';
  } else if (state === 'warning') {
    if (syncBadge) {
      syncBadge.style.background = 'rgba(239, 68, 68, 0.15)';
      syncBadge.style.color = '#f87171';
      syncBadge.style.borderColor = 'rgba(239, 68, 68, 0.3)';
    }
    if (syncText) syncText.textContent = '💾 Local Safe (Ready to Sync)';
    if (modalText) modalText.textContent = `💾 Progress safely preserved in local storage. Cloud auto-sync scheduled.`;
  }
}

// Conflict-Free Non-Destructive State Merger
function mergeCloudAndLocalState(remoteData, localData) {
  if (!remoteData || typeof remoteData !== 'object') return localData;
  if (!localData || typeof localData !== 'object') localData = {};

  const profiles = ['diego', 'johana', 'alejandro'];
  const modules = ['motorcycle', 'car'];
  const tabKeys = ['sheppard1', 'sheppard2', 'interactive', 'mode0', 'bookmarks', 'failed'];

  const rTime = Number(remoteData.last_updated) || 0;
  const lTime = Number(localData.last_updated) || 0;
  const remoteIsNewer = rTime > lTime;

  profiles.forEach(prof => {
    if (!localData[prof]) localData[prof] = {};
    const rProf = remoteData[prof];
    const lProf = localData[prof];

    if (rProf) {
      if (rProf.name && !lProf.name) lProf.name = rProf.name;

      modules.forEach(mod => {
        if (!lProf[mod]) {
          lProf[mod] = {
            bookmarks: [],
            failedQuestions: [],
            studiedQuestions: [],
            examHistory: [],
            lastIndices: { sheppard1: 0, sheppard2: 0, interactive: 0, mode0: 0, bookmarks: 0, failed: 0 }
          };
        }
        if (!lProf[mod].lastIndices) {
          lProf[mod].lastIndices = { sheppard1: 0, sheppard2: 0, interactive: 0, mode0: 0, bookmarks: 0, failed: 0 };
        }

        const rMod = rProf[mod];
        if (rMod) {
          // 1. Studied Questions: Non-destructive union merge
          const rStudied = Array.isArray(rMod.studiedQuestions) ? rMod.studiedQuestions : [];
          const lStudied = Array.isArray(lProf[mod].studiedQuestions) ? lProf[mod].studiedQuestions : [];
          lProf[mod].studiedQuestions = Array.from(new Set([...lStudied, ...rStudied]));

          // 2. Bookmarks: Union merge across all devices so bookmarks are never lost
          const rBookmarks = Array.isArray(rMod.bookmarks) ? rMod.bookmarks : [];
          const lBookmarks = Array.isArray(lProf[mod].bookmarks) ? lProf[mod].bookmarks : [];
          lProf[mod].bookmarks = Array.from(new Set([...lBookmarks, ...rBookmarks]));

          // 3. Failed Questions: Union merge across all devices so missed questions are always unified
          const rFailed = Array.isArray(rMod.failedQuestions) ? rMod.failedQuestions : [];
          const lFailed = Array.isArray(lProf[mod].failedQuestions) ? lProf[mod].failedQuestions : [];
          lProf[mod].failedQuestions = Array.from(new Set([...lFailed, ...rFailed]));

          // 4. Exam History Union (keyed by ISO date)
          const rExams = Array.isArray(rMod.examHistory) ? rMod.examHistory : [];
          const lExams = Array.isArray(lProf[mod].examHistory) ? lProf[mod].examHistory : [];
          const examMap = new Map();
          [...lExams, ...rExams].forEach(ex => {
            if (ex && ex.date) examMap.set(ex.date, ex);
          });
          lProf[mod].examHistory = Array.from(examMap.values());

          // 5. Smart Index Resolution: Take the furthest studied question index across all devices
          if (rMod.lastIndices && typeof rMod.lastIndices === 'object') {
            tabKeys.forEach(tk => {
              const rIdx = Number(rMod.lastIndices[tk]) || 0;
              const lIdx = Number(lProf[mod].lastIndices[tk]) || 0;
              lProf[mod].lastIndices[tk] = Math.max(lIdx, rIdx);
            });
          }
        }
      });
    }
  });

  localData.last_updated = Math.max(lTime, rTime, Date.now());
  return localData;
}

// Fetch with strict timeout controller
async function fetchWithTimeout(url, options = {}, timeoutMs = 6000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(url, { ...options, signal: controller.signal });
    clearTimeout(timeoutId);
    return response;
  } catch (err) {
    clearTimeout(timeoutId);
    throw err;
  }
}

// Robust Core Sync Engine
async function syncWithCloud(forcePush = false, showFeedback = false) {
  if (isSyncing) {
    pendingOfflineSync = true;
    return;
  }

  if (!navigator.onLine) {
    pendingOfflineSync = true;
    updateSyncStatusUI('offline_flight');
    if (showFeedback) {
      showToast('✈️ Flight Mode: Progress safely preserved offline on iPad.', false);
    }
    return;
  }

  isSyncing = true;
  updateSyncStatusUI('syncing');

  const endpoints = getCloudEndpoints();
  let syncSuccess = false;
  let lastError = null;

  for (const endpoint of endpoints) {
    try {
      // 1. PULL & MERGE FROM CLOUD
      const pullUrl = endpoint + (endpoint.includes('?') ? '&' : '?') + 'nocache=' + Date.now();
      const getRes = await fetchWithTimeout(pullUrl, { method: 'GET' }, 5000);

      let cloudData = null;
      if (getRes.ok) {
        const raw = await getRes.json();
        if (raw) {
          if (raw.diego || raw.johana || raw.alejandro) {
            cloudData = raw;
          } else if (raw.data) {
            try {
              cloudData = (typeof raw.data === 'string') ? JSON.parse(raw.data) : raw.data;
            } catch (e) {}
          } else if (typeof raw === 'string') {
            try { cloudData = JSON.parse(raw); } catch (e) {}
          }
        }
      }

      const lTime = Number(userState.last_updated) || 0;
      const rTime = cloudData ? (Number(cloudData.last_updated) || 0) : 0;
      const localHasNewerChanges = lTime > rTime;

      // Merge Cloud state with Local state
      if (cloudData && (cloudData.diego || cloudData.johana || cloudData.alejandro)) {
        userState = mergeCloudAndLocalState(cloudData, userState);
        localStorage.setItem('tw_driver_prep_state_v2', JSON.stringify(userState));
      }

      // 2. PUSH TO CLOUD IF FORCE PUSH REQUESTED, OR LOCAL HAS NEWER DATA, OR STATE EXPANDED
      const stateNeedsPush = forcePush || localHasNewerChanges || (cloudData && JSON.stringify(cloudData) !== JSON.stringify(userState));
      if (stateNeedsPush) {
        userState.last_updated = Math.max(lTime, rTime, Date.now());
        const isLocalServer = endpoint.includes('/api/sync') || endpoint.includes('localhost') || endpoint.includes('127.0.0.1');
        const putMethod = isLocalServer ? 'POST' : 'PUT';
        const putContentType = 'application/json';

        const putRes = await fetchWithTimeout(endpoint, {
          method: putMethod,
          headers: { 'Content-Type': putContentType },
          body: JSON.stringify(userState)
        }, 6000);

        if (!putRes.ok) {
          throw new Error(`Cloud PUT status ${putRes.status}`);
        }
      }

      syncSuccess = true;
      pendingOfflineSync = false;
      const nowStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      localStorage.setItem('tw_driver_last_sync_time', Date.now().toString());
      updateSyncStatusUI('online_synced', nowStr);

      updateProfileUI();
      updateDashboardStats();
      updateFilteredQuestions();
      renderCurrentQuestion();
      if (showFeedback) {
        showToast('🎉 Cloud sync complete! All study progress is unified.');
      }
      break; // Successfully synced to active endpoint
    } catch (err) {
      console.warn(`Sync attempt failed on ${endpoint}:`, err);
      lastError = err;
    }
  }

  isSyncing = false;

  if (!syncSuccess) {
    if (!navigator.onLine) {
      updateSyncStatusUI('offline_flight');
    } else {
      updateSyncStatusUI('warning');
      if (showFeedback) {
        showToast('💾 Progress safely preserved locally (Cloud bin unreachable).', false);
      }
    }
  }
}

// Auto-sync polling every 30 seconds while app is active
setInterval(() => {
  if (navigator.onLine && document.visibilityState === 'visible') {
    syncWithCloud(false);
  }
}, 30000);

// ==========================================
// STARTUP PROFILE PICKER OVERLAY LOGIC
// ==========================================
function showProfilePickerModal() {
  const pickerModal = document.getElementById('profilePickerModal');
  if (!pickerModal) return;

  ['diego', 'johana', 'alejandro'].forEach(prof => {
    const statsEl = document.getElementById(`pickerStats${prof.charAt(0).toUpperCase() + prof.slice(1)}`);
    if (statsEl && userState[prof]) {
      const carStudied = (userState[prof].car && userState[prof].car.studiedQuestions) ? userState[prof].car.studiedQuestions.length : 0;
      const carBook = (userState[prof].car && userState[prof].car.bookmarks) ? userState[prof].car.bookmarks.length : 0;
      statsEl.textContent = `${carStudied} Studied • ${carBook} Bookmarks`;
    }
  });

  pickerModal.classList.remove('hidden');
}

function hideProfilePickerModal() {
  const pickerModal = document.getElementById('profilePickerModal');
  if (pickerModal) pickerModal.classList.add('hidden');
}

// STORAGE PERSISTENCE
function loadProfileFromStorage() {
  const savedState = localStorage.getItem('tw_driver_prep_state_v2');
  if (savedState) {
    try {
      const parsed = JSON.parse(savedState);
      if (parsed.diego || parsed.johana || parsed.alejandro) {
        userState = mergeCloudAndLocalState(parsed, userState);
      }
    } catch (e) {}
  }
  const savedProfile = localStorage.getItem('tw_driver_active_profile');
  if (savedProfile && userState[savedProfile]) {
    activeProfile = savedProfile;
  }
  const savedMod = localStorage.getItem('tw_driver_active_module');
  if (savedMod && (savedMod === 'car' || savedMod === 'motorcycle')) {
    currentModule = savedMod;
  }
  const savedTab = localStorage.getItem('tw_driver_active_tab');
  if (savedTab) {
    currentTab = savedTab;
  }
  updateProfileUI();

  // Set initial sync UI based on network status
  if (!navigator.onLine) {
    updateSyncStatusUI('offline_flight');
  } else {
    const lastSyncTime = localStorage.getItem('tw_driver_last_sync_time');
    if (lastSyncTime) {
      const dt = new Date(parseInt(lastSyncTime));
      updateSyncStatusUI('online_synced', dt.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
    }
  }

  // Show profile picker on fresh startup
  const hasPicked = sessionStorage.getItem('tw_driver_profile_picked_session');
  if (!hasPicked) {
    showProfilePickerModal();
  }
  
  // Background Cloud Sync on startup
  syncWithCloud(false);

  // Auto-sync whenever device reconnects to Wi-Fi/Internet (e.g. landing after flight)
  window.addEventListener('online', () => {
    showToast('🌐 Internet reconnected! Syncing flight progress to Cloud...');
    syncWithCloud(true);
  });

  // Flight Mode indicator when airplane mode is toggled or connection drops
  window.addEventListener('offline', () => {
    updateSyncStatusUI('offline_flight');
  });

  // Auto-pull updates when tab is opened/focused on iPad/PC, flush when hidden
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') {
      if (navigator.onLine) {
        syncWithCloud(false);
      } else {
        updateSyncStatusUI('offline_flight');
      }
    } else if (document.visibilityState === 'hidden') {
      flushImmediateSync();
    }
  });

  // iOS Safari pagehide (fires when switching apps or locking iPad)
  window.addEventListener('pagehide', () => {
    flushImmediateSync();
  });

  // Window beforeunload (fires when closing desktop tab)
  window.addEventListener('beforeunload', () => {
    flushImmediateSync();
  });

  // Window focus (refresh state when switching back to tab)
  window.addEventListener('focus', () => {
    if (navigator.onLine) {
      syncWithCloud(false);
    }
  });
}

function flushImmediateSync() {
  if (syncDebounceTimer) {
    clearTimeout(syncDebounceTimer);
    syncDebounceTimer = null;
  }
  if (navigator.onLine) {
    userState.last_updated = Date.now();
    try {
      fetch(PRIMARY_CLOUD_ENDPOINT, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userState),
        keepalive: true
      });
    } catch (e) {
      console.warn('Immediate flush error:', e);
    }
  }
}

function saveStateToStorage() {
  const m = getModuleData();
  if (m) {
    if (!m.lastIndices) m.lastIndices = {};
    m.lastIndices[currentTab] = currentIndex;
  }
  userState.last_updated = Date.now();
  localStorage.setItem('tw_driver_prep_state_v2', JSON.stringify(userState));
  localStorage.setItem('tw_driver_active_profile', activeProfile);
  localStorage.setItem('tw_driver_active_module', currentModule);
  localStorage.setItem('tw_driver_active_tab', currentTab);
  updateDashboardStats();

  // Debounced auto-sync to Cloud in background (1500ms debounce)
  if (syncDebounceTimer) clearTimeout(syncDebounceTimer);
  syncDebounceTimer = setTimeout(() => {
    syncWithCloud(true);
  }, 1500);
}

function getModuleData() {
  const p = userState[activeProfile] || userState['diego'];
  if (!p[currentModule]) {
    p[currentModule] = { 
      bookmarks: [], 
      failedQuestions: [], 
      studiedQuestions: [], 
      examHistory: [],
      lastIndices: { sheppard1: 0, sheppard2: 0, interactive: 0, mode0: 0, bookmarks: 0, failed: 0 }
    };
  }
  if (!p[currentModule].lastIndices) {
    p[currentModule].lastIndices = { sheppard1: 0, sheppard2: 0, interactive: 0, mode0: 0, bookmarks: 0, failed: 0 };
  }
  return p[currentModule];
}

function updateProfileUI() {
  const profSelect = document.getElementById('profileSelect');
  if (profSelect) profSelect.value = activeProfile;
}

// ==========================================
// BACKUP, RESTORE & MODAL HUB LOGIC
// ==========================================
function updateModalSummary() {
  const profNameEl = document.getElementById('backupProfileName');
  const statsEl = document.getElementById('backupStatsSummary');
  const rawJsonArea = document.getElementById('rawJsonArea');

  const p = userState[activeProfile] || {};
  const motoStudied = p.motorcycle?.studiedQuestions?.length || 0;
  const carStudied = p.car?.studiedQuestions?.length || 0;
  const motoFailed = p.motorcycle?.failedQuestions?.length || 0;
  const carFailed = p.car?.failedQuestions?.length || 0;
  const motoBook = p.motorcycle?.bookmarks?.length || 0;
  const carBook = p.car?.bookmarks?.length || 0;

  if (profNameEl) profNameEl.textContent = activeProfile.charAt(0).toUpperCase() + activeProfile.slice(1);
  if (statsEl) {
    statsEl.innerHTML = `
      <div>🏍️ <strong>Motorcycle:</strong> ${motoStudied} studied • ${motoFailed} failed • ${motoBook} stars</div>
      <div>🚗 <strong>Car:</strong> ${carStudied} studied • ${carFailed} failed • ${carBook} stars</div>
      <div style="margin-top:0.25rem; font-size:0.75rem; color:#10b981; font-weight:700;">✓ Total Diego Studied: ${motoStudied + carStudied} questions</div>
    `;
  }
  if (rawJsonArea) {
    rawJsonArea.value = JSON.stringify(userState, null, 2);
  }
}

function openSyncModal(initialTab = 'backup') {
  const modal = document.getElementById('syncHubModal');
  if (!modal) return;
  modal.classList.remove('hidden');
  switchModalTab(initialTab);
  updateModalSummary();

  const customInp = document.getElementById('customCloudEndpointInput');
  if (customInp) {
    customInp.value = localStorage.getItem('tw_driver_custom_cloud_endpoint') || '';
  }
}

function closeSyncModal() {
  const modal = document.getElementById('syncHubModal');
  if (modal) modal.classList.add('hidden');
}

function switchModalTab(tab) {
  const tabs = {
    backup: { btn: document.getElementById('modalTabBackup'), sec: document.getElementById('modalSectionBackup') },
    restore: { btn: document.getElementById('modalTabRestore'), sec: document.getElementById('modalSectionRestore') },
    cloud: { btn: document.getElementById('modalTabCloud'), sec: document.getElementById('modalSectionCloud') }
  };

  Object.keys(tabs).forEach(k => {
    if (tabs[k].btn) tabs[k].btn.classList.toggle('active', k === tab);
    if (tabs[k].sec) tabs[k].sec.classList.toggle('hidden', k !== tab);
  });
}

// Share via Native Share API (AirDrop / Files on iPadOS/iOS)
async function shareBackupFile() {
  const jsonStr = JSON.stringify(userState, null, 2);
  const fileName = `taiwan_driver_backup_${activeProfile}_${new Date().toISOString().slice(0,10)}.json`;

  try {
    const file = new File([jsonStr], fileName, { type: 'application/json' });
    if (navigator.canShare && navigator.canShare({ files: [file] })) {
      await navigator.share({
        title: 'Taiwan License Prep Backup',
        text: `Backup for ${activeProfile} (${new Date().toLocaleDateString()})`,
        files: [file]
      });
      showToast('✓ Backup shared successfully!');
      return;
    }
  } catch (e) {
    if (e.name !== 'AbortError') {
      console.warn('Share file error:', e);
    }
  }

  // Fallback 1: Text Share
  if (navigator.share) {
    try {
      await navigator.share({
        title: 'Taiwan License Prep Backup Code',
        text: jsonStr
      });
      showToast('✓ Backup shared successfully!');
      return;
    } catch (e) {}
  }

  // Fallback 2: Direct Blob Download
  downloadBackupBlob(jsonStr, fileName);
}

function downloadBackupBlob(jsonStr, fileName) {
  try {
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName || `taiwan_driver_backup_${activeProfile}.json`;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      URL.revokeObjectURL(url);
      a.remove();
    }, 1500);
    showToast('✓ Backup file downloaded!');
  } catch (e) {
    copyBackupToClipboard();
  }
}

async function copyBackupToClipboard() {
  const jsonStr = JSON.stringify(userState, null, 2);
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(jsonStr);
      showToast('📋 Copied full backup code to clipboard!');
      return;
    }
  } catch (e) {}

  // Fallback for older WebViews / iOS Safari
  const textArea = document.createElement('textarea');
  textArea.value = jsonStr;
  textArea.style.position = 'fixed';
  textArea.style.left = '-9999px';
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();
  try {
    document.execCommand('copy');
    showToast('📋 Copied full backup code to clipboard!');
  } catch (err) {
    alert('Please copy manually from the View Code box.');
  }
  document.body.removeChild(textArea);
}

function applyRestoredData(importedData) {
  if (importedData && (importedData.diego || importedData.johana || importedData.alejandro)) {
    userState = mergeCloudAndLocalState(importedData, userState);
    saveStateToStorage();
    updateFilteredQuestions();
    renderCurrentQuestion();
    updateDashboardStats();
    updateModalSummary();
    closeSyncModal();
    showToast('🎉 Progress successfully restored and merged!');
    syncWithCloud(true, false);
  } else {
    showToast('⚠️ Unrecognized backup file format.', true);
  }
}

// EVENT LISTENERS SETUP
function setupEventListeners() {
  // Profile Picker Card Clicks
  const pickerCards = document.querySelectorAll('.profile-select-card');
  pickerCards.forEach(card => {
    card.addEventListener('click', () => {
      const prof = card.getAttribute('data-profile');
      if (prof && userState[prof]) {
        activeProfile = prof;
        sessionStorage.setItem('tw_driver_profile_picked_session', 'true');
        localStorage.setItem('tw_driver_active_profile', prof);
        updateProfileUI();
        hideProfilePickerModal();

        const m = getModuleData();
        if (m.lastIndices && m.lastIndices[currentTab] !== undefined && m.lastIndices[currentTab] >= 0) {
          currentIndex = m.lastIndices[currentTab];
        } else if (m.studiedQuestions && m.studiedQuestions.length > 0 && (currentTab === 'sheppard1' || currentTab === 'sheppard2' || currentTab === 'interactive')) {
          currentIndex = Math.min(allQuestions.length - 1, m.studiedQuestions.length);
        } else {
          currentIndex = 0;
        }

        localStorage.setItem('tw_driver_active_profile', prof);
        updateFilteredQuestions();
        renderCurrentQuestion();
        updateModalSummary();
        showToast(`👤 Perfil activo: ${prof.toUpperCase()}`);
        syncWithCloud(false);
      }
    });
  });

  const profSelect = document.getElementById('profileSelect');
  if (profSelect) {
    profSelect.addEventListener('change', (e) => {
      activeProfile = e.target.value;
      localStorage.setItem('tw_driver_active_profile', activeProfile);
      updateFilteredQuestions();
      renderCurrentQuestion();
      updateModalSummary();
      syncWithCloud(false);
    });
  }

  // Backup & Restore Hub Triggers
  const expBtn = document.getElementById('exportSyncBtn');
  if (expBtn) expBtn.addEventListener('click', () => openSyncModal('backup'));

  const impBtn = document.getElementById('importSyncBtn');
  if (impBtn) impBtn.addEventListener('click', () => openSyncModal('restore'));

  const cloudPill = document.getElementById('cloudSyncStatus');
  if (cloudPill) cloudPill.addEventListener('click', () => openSyncModal('cloud'));

  // Modal Controls
  const closeBtn = document.getElementById('closeSyncModalBtn');
  if (closeBtn) closeBtn.addEventListener('click', closeSyncModal);

  const modalTabBackup = document.getElementById('modalTabBackup');
  if (modalTabBackup) modalTabBackup.addEventListener('click', () => switchModalTab('backup'));

  const modalTabRestore = document.getElementById('modalTabRestore');
  if (modalTabRestore) modalTabRestore.addEventListener('click', () => switchModalTab('restore'));

  const modalTabCloud = document.getElementById('modalTabCloud');
  if (modalTabCloud) modalTabCloud.addEventListener('click', () => switchModalTab('cloud'));

  // Modal Action Buttons
  const shareBtn = document.getElementById('shareBackupBtn');
  if (shareBtn) shareBtn.addEventListener('click', shareBackupFile);

  const copyBtn = document.getElementById('copyBackupCodeBtn');
  if (copyBtn) copyBtn.addEventListener('click', copyBackupToClipboard);

  const dlBtn = document.getElementById('directDownloadJsonBtn');
  if (dlBtn) dlBtn.addEventListener('click', () => downloadBackupBlob(JSON.stringify(userState, null, 2)));

  const toggleRawBtn = document.getElementById('toggleRawJsonBtn');
  const rawBox = document.getElementById('rawJsonBox');
  if (toggleRawBtn && rawBox) {
    toggleRawBtn.addEventListener('click', () => rawBox.classList.toggle('hidden'));
  }

  // Paste Restore
  const applyPastedBtn = document.getElementById('applyPastedRestoreBtn');
  const pasteArea = document.getElementById('pasteRestoreArea');
  if (applyPastedBtn && pasteArea) {
    applyPastedBtn.addEventListener('click', () => {
      const text = pasteArea.value.trim();
      if (!text) {
        showToast('⚠️ Please paste JSON backup code first.', true);
        return;
      }
      try {
        const parsed = JSON.parse(text);
        applyRestoredData(parsed);
      } catch (err) {
        showToast('⚠️ Invalid JSON code. Check and try again.', true);
      }
    });
  }

  // File Upload Restore
  const impFile = document.getElementById('importFileInput');
  const chooseFileBtn = document.getElementById('chooseFileRestoreBtn');
  if (chooseFileBtn && impFile) {
    chooseFileBtn.addEventListener('click', () => impFile.click());
    impFile.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {
        try {
          const importedData = JSON.parse(event.target.result);
          applyRestoredData(importedData);
        } catch (err) {
          showToast('⚠️ Invalid JSON backup file format.', true);
        }
      };
      reader.readAsText(file);
    });
  }

  // Cloud Manual Sync
  const forcePushBtn = document.getElementById('forcePushCloudBtn');
  if (forcePushBtn) forcePushBtn.addEventListener('click', () => syncWithCloud(true, true));

  const forcePullBtn = document.getElementById('forcePullCloudBtn');
  if (forcePullBtn) forcePullBtn.addEventListener('click', () => syncWithCloud(false, true));

  const saveEndpointBtn = document.getElementById('saveCloudEndpointBtn');
  const customInp = document.getElementById('customCloudEndpointInput');
  if (saveEndpointBtn && customInp) {
    saveEndpointBtn.addEventListener('click', () => {
      const val = customInp.value.trim();
      if (val) {
        localStorage.setItem('tw_driver_custom_cloud_endpoint', val);
        showToast('✓ Custom sync endpoint saved!');
      } else {
        localStorage.removeItem('tw_driver_custom_cloud_endpoint');
        showToast('✓ Reset to Default Cloud Bin');
      }
      syncWithCloud(true, true);
    });
  }

  const modSelect = document.getElementById('moduleSelect');
  if (modSelect) {
    modSelect.addEventListener('change', async (e) => {
      currentIndex = 0;
      examQuestions = [];
      examSubmitted = false;
      examUserAnswers = {};
      await loadModuleData(e.target.value);
      if (currentTab === 'practice') {
        startPracticeExam();
      } else {
        switchTab(currentTab);
      }
    });
  }

  const topicSelect = document.getElementById('topicSelect');
  if (topicSelect) {
    topicSelect.addEventListener('change', (e) => {
      selectedTopic = e.target.value;
      currentIndex = 0;
      updateFilteredQuestions();
      renderCurrentQuestion();
    });
  }

  const catSelect = document.getElementById('categorySelect');
  if (catSelect) {
    catSelect.addEventListener('change', (e) => {
      selectedCategory = e.target.value;
      currentIndex = 0;
      updateFilteredQuestions();
      renderCurrentQuestion();
    });
  }

  const searchInp = document.getElementById('searchInput');
  if (searchInp) {
    searchInp.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      currentIndex = 0;
      updateFilteredQuestions();
      renderCurrentQuestion();
    });
  }

  // Restart Mode / Clear Action Button
  const restartBtn = document.getElementById('restartModeBtn');
  if (restartBtn) {
    restartBtn.addEventListener('click', () => {
      if (currentTab === 'failed') {
        const m = getModuleData();
        if (!m.failedQuestions || m.failedQuestions.length === 0) {
          showToast('⚠️ Failed bank is already empty!');
          return;
        }
        if (confirm(`Clear all ${m.failedQuestions.length} failed questions from your Failed Questions Bank?`)) {
          m.failedQuestions = [];
          currentIndex = 0;
          if (m.lastIndices) m.lastIndices.failed = 0;
          saveStateToStorage();
          updateFilteredQuestions();
          renderCurrentQuestion();
          showToast('🗑️ All failed questions cleared!');
        }
      } else {
        if (confirm(`Reset current mode progress (${currentTab}) back to Question #1? Your overall studied progress and Exam Readiness will be preserved.`)) {
          currentIndex = 0;
          const m = getModuleData();
          if (m.lastIndices) m.lastIndices[currentTab] = 0;
          saveStateToStorage();
          renderCurrentQuestion();
          showToast('🔄 Returned to Question #1');
        }
      }
    });
  }

  // Jump-to-Question Input Listener
  const jumpInp = document.getElementById('jumpInput');
  if (jumpInp) {
    jumpInp.addEventListener('change', (e) => {
      const targetVal = parseInt(e.target.value);
      if (!isNaN(targetVal) && targetVal >= 1 && targetVal <= filteredQuestions.length) {
        currentIndex = targetVal - 1;
        const m = getModuleData();
        if (m.lastIndices) m.lastIndices[currentTab] = currentIndex;
        saveStateToStorage();
        renderCurrentQuestion();
      }
    });
  }

  // Tab Buttons
  document.querySelectorAll('.nav-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = btn.dataset.tab;
      switchTab(tab);
    });
  });

  // Unified Keyboard Shortcuts for Rapid Evaluation (Arrow keys, 1/2/3, Space, E, B)
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;
    if (document.activeElement && ['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      document.getElementById('prevBtn')?.click();
    } else if (e.key === 'ArrowRight' || e.key === ' ') {
      e.preventDefault();
      document.getElementById('nextBtn')?.click();
    } else if (['1', '2', '3'].includes(e.key)) {
      const optBtns = document.querySelectorAll('#optionsContainer button.opt-btn');
      const idx = parseInt(e.key) - 1;
      if (optBtns[idx]) {
        optBtns[idx].click();
      }
    } else if (e.key === 'e' || e.key === 'E') {
      document.getElementById('toggleExplBtn')?.click();
    } else if (e.key === 'b' || e.key === 'B') {
      document.getElementById('bookmarkBtn')?.click();
    }
  });

  // Theme Toggle
  document.getElementById('themeToggleBtn')?.addEventListener('click', () => {
    document.body.classList.toggle('light-theme');
  });

  // Mobile Bottom Navigation Bar Listeners
  document.getElementById('mobilePrevBtn')?.addEventListener('click', () => {
    document.getElementById('prevBtn')?.click();
  });
  document.getElementById('mobileNextBtn')?.addEventListener('click', () => {
    document.getElementById('nextBtn')?.click();
  });
  document.getElementById('mobileExplBtn')?.addEventListener('click', () => {
    document.getElementById('toggleExplBtn')?.click();
  });
  document.getElementById('mobileSubmitBtn')?.addEventListener('click', () => {
    document.getElementById('submitExamBtn')?.click();
  });

  // Filter Drawer Toggle on Mobile
  document.getElementById('filterToggleBtn')?.addEventListener('click', () => {
    const sidebar = document.getElementById('sidebarPanel');
    if (sidebar) {
      sidebar.classList.toggle('collapsed');
    }
  });

  // Navigation Buttons
  document.getElementById('prevBtn')?.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      const m = getModuleData();
      if (m.lastIndices) m.lastIndices[currentTab] = currentIndex;
      saveStateToStorage();
      renderCurrentQuestion();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  });

  document.getElementById('nextBtn')?.addEventListener('click', () => {
    if (currentIndex < filteredQuestions.length - 1) {
      currentIndex++;
      const m = getModuleData();
      if (m.lastIndices) m.lastIndices[currentTab] = currentIndex;
      saveStateToStorage();
      recordQuestionStudied(filteredQuestions[currentIndex - 1]?.id);
      renderCurrentQuestion();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  });

  // Bookmark Button (Toggle Star)
  document.getElementById('bookmarkBtn')?.addEventListener('click', () => {
    if (!filteredQuestions[currentIndex]) return;
    const qId = filteredQuestions[currentIndex].id;
    const m = getModuleData();
    const idx = m.bookmarks.indexOf(qId);
    if (idx >= 0) {
      m.bookmarks.splice(idx, 1);
      showToast('★ Removed from Bookmarks');
    } else {
      m.bookmarks.push(qId);
      showToast('★ Added to Bookmarks');
    }
    saveStateToStorage();
    updateBookmarkUI(qId);
    if (currentTab === 'bookmarks') {
      updateFilteredQuestions();
      renderCurrentQuestion();
    }
  });

  // Remove from Failed Button Handlers (Header and Action bar)
  const removeFailedHandler = () => {
    if (!filteredQuestions[currentIndex]) return;
    const qId = filteredQuestions[currentIndex].id;
    const m = getModuleData();
    const idx = m.failedQuestions.indexOf(qId);
    if (idx >= 0) {
      m.failedQuestions.splice(idx, 1);
      saveStateToStorage();
      showToast('🗑️ Question removed from Failed Bank!');
      updateFilteredQuestions();
      renderCurrentQuestion();
    }
  };

  document.getElementById('removeFailedBtn')?.addEventListener('click', removeFailedHandler);
  document.getElementById('actionFailedBtn')?.addEventListener('click', removeFailedHandler);

  // Explanation Toggle
  document.getElementById('toggleExplBtn')?.addEventListener('click', () => {
    const card = document.getElementById('explanationCard');
    const label = document.getElementById('explBtnLabel');
    if (card.classList.contains('hidden')) {
      card.classList.remove('hidden');
      label.textContent = 'Hide Explanation';
    } else {
      card.classList.add('hidden');
      label.textContent = 'Show Explanation';
    }
  });

  // Retake / Review / Submit Exam
  document.getElementById('restartExamBtn')?.addEventListener('click', () => {
    startPracticeExam();
  });
  document.getElementById('reviewFailedExamBtn')?.addEventListener('click', () => {
    switchTab('failed');
  });
  document.getElementById('submitExamBtn')?.addEventListener('click', () => {
    submitPracticeExam();
  });


}

// FILTERING LOGIC
function updateFilteredQuestions() {
  const m = getModuleData();

  if (currentTab === 'bookmarks') {
    filteredQuestions = allQuestions.filter(q => m.bookmarks.includes(q.id));
  } else if (currentTab === 'failed') {
    filteredQuestions = allQuestions.filter(q => m.failedQuestions.includes(q.id));
  } else if (currentTab === 'practice') {
    filteredQuestions = examQuestions;
  } else {
    // Sheppard 1, 2, Interactive
    filteredQuestions = allQuestions.filter(q => {
      const matchCat = (selectedCategory === 'ALL' || q.category === selectedCategory);
      const matchTopic = (selectedTopic === 'ALL_TOPICS' || q.topic === selectedTopic);
      const matchSearch = !searchQuery || (
        q.question.toLowerCase().includes(searchQuery) ||
        q.options.some(o => o.toLowerCase().includes(searchQuery))
      );
      return matchCat && matchTopic && matchSearch;
    });
  }

  if (currentIndex >= filteredQuestions.length) {
    currentIndex = Math.max(0, filteredQuestions.length - 1);
  }

  updateDashboardStats();
}

// TAB SWITCHING
function switchTab(tab) {
  currentTab = tab;

  document.querySelectorAll('.nav-tab').forEach(btn => {
    if (btn.dataset.tab === tab) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  const questionCard = document.getElementById('questionContainer');
  const resultCard = document.getElementById('examResultCard');
  const cheatCard = document.getElementById('cheatSheetContainer');
  const masterCardContainer = document.getElementById('masterRulesContainer');

  questionCard.classList.add('hidden');
  resultCard.classList.add('hidden');
  cheatCard.classList.add('hidden');
  if (masterCardContainer) masterCardContainer.classList.add('hidden');

  const modeTitle = document.getElementById('modeTitle');
  const modeDesc = document.getElementById('modeDesc');
  const restartBtn = document.getElementById('restartModeBtn');

  if (tab === 'mode0') {
    const modLabel = (currentModule === 'car') ? 'Car License (汽車)' : 'Motorcycle License (機車)';
    modeTitle.innerHTML = `🧠 Mode 0: Master Rule Grouping (${modLabel})`;
    modeDesc.textContent = 'High-level synthesis: Consolidates 3,000+ questions into 9 core Master Rule Cards for 5x faster learning.';
    if (restartBtn) {
      restartBtn.classList.remove('hidden');
      restartBtn.innerHTML = '🔄 Restart to #1';
      restartBtn.title = 'Return to Rule #1';
      restartBtn.style.background = 'rgba(99,102,241,0.15)';
      restartBtn.style.color = '#818cf8';
      restartBtn.style.borderColor = 'rgba(99,102,241,0.3)';
    }
    if (masterCardContainer) {
      masterCardContainer.classList.remove('hidden');
      renderMasterRules();
    }
  } else if (tab === 'sheppard1') {
    modeTitle.innerHTML = '✨ Sheppard Air Mode 1: Direct Answer Recall';
    modeDesc.textContent = 'Shows ONLY the correct answer for rapid, distraction-free neural memorization.';
    if (restartBtn) {
      restartBtn.classList.remove('hidden');
      restartBtn.innerHTML = '🔄 Restart to #1';
      restartBtn.title = 'Return to Question #1 in this mode';
      restartBtn.style.background = 'rgba(99,102,241,0.15)';
      restartBtn.style.color = '#818cf8';
      restartBtn.style.borderColor = 'rgba(99,102,241,0.3)';
    }
    questionCard.classList.remove('hidden');
  } else if (tab === 'sheppard2') {
    modeTitle.innerHTML = '🖍️ Sheppard Air Mode 2: Highlighted Options';
    modeDesc.textContent = 'Displays all options with the correct answer explicitly highlighted in green.';
    if (restartBtn) {
      restartBtn.classList.remove('hidden');
      restartBtn.innerHTML = '🔄 Restart to #1';
      restartBtn.title = 'Return to Question #1 in this mode';
      restartBtn.style.background = 'rgba(99,102,241,0.15)';
      restartBtn.style.color = '#818cf8';
      restartBtn.style.borderColor = 'rgba(99,102,241,0.3)';
    }
    questionCard.classList.remove('hidden');
  } else if (tab === 'interactive') {
    modeTitle.innerHTML = '🎯 Interactive Quiz + Instant Feedback';
    modeDesc.textContent = 'Click options for instant Green (Correct) / Red (Incorrect) feedback & law context.';
    if (restartBtn) {
      restartBtn.classList.remove('hidden');
      restartBtn.innerHTML = '🔄 Restart to #1';
      restartBtn.title = 'Return to Question #1 in this mode';
      restartBtn.style.background = 'rgba(99,102,241,0.15)';
      restartBtn.style.color = '#818cf8';
      restartBtn.style.borderColor = 'rgba(99,102,241,0.3)';
    }
    questionCard.classList.remove('hidden');
  } else if (tab === 'practice') {
    modeTitle.innerHTML = '⏱️ 50-Question Practice Exam Simulation';
    modeDesc.textContent = 'Simulated test environment with 85% passing score threshold.';
    if (restartBtn) restartBtn.classList.add('hidden');
    if (examQuestions.length === 0 || examSubmitted) {
      startPracticeExam();
    } else {
      questionCard.classList.remove('hidden');
    }
  } else if (tab === 'bookmarks') {
    modeTitle.innerHTML = '⭐ Bookmarked Starred Questions';
    modeDesc.textContent = 'Targeted review for your starred key items.';
    if (restartBtn) {
      restartBtn.classList.remove('hidden');
      restartBtn.innerHTML = '🔄 Go to #1';
      restartBtn.title = 'Go to first bookmarked item';
      restartBtn.style.background = 'rgba(99,102,241,0.15)';
      restartBtn.style.color = '#818cf8';
      restartBtn.style.borderColor = 'rgba(99,102,241,0.3)';
    }
    questionCard.classList.remove('hidden');
  } else if (tab === 'failed') {
    modeTitle.innerHTML = '⚠️ Failed Questions Retry Bank';
    modeDesc.textContent = 'Review questions missed in previous quizzes/exams. Click "Remove from Failed" when mastered!';
    if (restartBtn) {
      restartBtn.classList.remove('hidden');
      restartBtn.innerHTML = '🗑️ Clear All Failed';
      restartBtn.title = 'Clear all questions from Failed Questions Bank';
      restartBtn.style.background = 'rgba(239,68,68,0.2)';
      restartBtn.style.color = '#f87171';
      restartBtn.style.borderColor = 'rgba(239,68,68,0.4)';
    }
    questionCard.classList.remove('hidden');
  } else if (tab === 'cheatsheet') {
    const modLabel = (currentModule === 'car') ? 'Car License (汽車)' : 'Motorcycle License (機車)';
    modeTitle.innerHTML = `📋 ${modLabel} Cram Sheet & Key Facts`;
    modeDesc.textContent = 'Quick reference guide covering numbers, cargo, speeds, BAC limits, fines, and CPR.';
    if (restartBtn) restartBtn.classList.add('hidden');
    cheatCard.classList.remove('hidden');
    renderCheatSheet();
  }

  const m = getModuleData();
  if (m.lastIndices && m.lastIndices[tab] !== undefined) {
    currentIndex = m.lastIndices[tab];
  } else {
    currentIndex = 0;
  }
  updateFilteredQuestions();
  renderCurrentQuestion();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// RENDER CURRENT QUESTION
function renderCurrentQuestion() {
  if (currentTab === 'cheatsheet') return;

  const optionsDiv = document.getElementById('optionsContainer');
  const explanationCard = document.getElementById('explanationCard');
  const signBox = document.getElementById('signIllustrationBox');
  const signSvgDiv = document.getElementById('signSvgContainer');

  if (filteredQuestions.length === 0) {
    document.getElementById('questionCategoryBadge').textContent = 'No Items';
    document.getElementById('questionTopicBadge').textContent = 'Empty Bank';
    document.getElementById('questionIndexText').textContent = '0 of 0';
    document.getElementById('questionText').textContent = getEmptyMessage();
    optionsDiv.innerHTML = '';
    signBox.classList.add('hidden');
    explanationCard.classList.add('hidden');
    document.getElementById('prevBtn').disabled = true;
    document.getElementById('nextBtn').disabled = true;
    return;
  }

  const q = filteredQuestions[currentIndex];
  const m = getModuleData();

  // Sign Image & Video Link Rendering
  const imgUrl = q.sign_image || q.image;
  if (imgUrl || q.sign_svg || q.video_link) {
    let mediaHTML = '';
    if (imgUrl) {
      mediaHTML += `<div style="text-align:center; padding:0.5rem;"><img src="${imgUrl}" style="max-height:140px; max-width:100%; border-radius:8px; border:1px solid var(--border-color); background:#fff; padding:6px; box-shadow:0 4px 12px rgba(0,0,0,0.25);" alt="Official Sign Image" /></div>`;
    } else if (q.sign_svg) {
      mediaHTML += q.sign_svg;
    }
    if (q.video_link) {
      mediaHTML += `<div style="text-align:center; margin-top:0.5rem;"><a href="${q.video_link}" target="_blank" rel="noopener" class="btn-primary" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.4rem 0.8rem; font-size:0.82rem; text-decoration:none; border-radius:6px; background:#ef4444; color:#fff;">🎬 Watch Official THB Hazard Video #${q.video_number || ''}</a></div>`;
    }
    signSvgDiv.innerHTML = mediaHTML;
    signBox.classList.remove('hidden');
  } else {
    signBox.classList.add('hidden');
  }

  // Badges & Jump Input Sync
  const isStudied = m.studiedQuestions && m.studiedQuestions.includes(q.id);
  const studiedBadgeHTML = isStudied ? `<span style="font-size:0.7rem; font-weight:800; background:rgba(16,185,129,0.2); color:#34d399; border:1px solid rgba(16,185,129,0.4); padding:0.15rem 0.45rem; border-radius:6px; margin-right:0.4rem;">✓ STUDIED</span>` : '';
  
  document.getElementById('questionCategoryBadge').innerHTML = studiedBadgeHTML + q.category;
  document.getElementById('questionTopicBadge').textContent = q.topic || 'General Law';
  document.getElementById('questionIndexText').textContent = `Question ${currentIndex + 1} of ${filteredQuestions.length}`;
  const jumpInpEl = document.getElementById('jumpInput');
  if (jumpInpEl) {
    jumpInpEl.value = currentIndex + 1;
    jumpInpEl.max = filteredQuestions.length;
  }

  // Bookmark Button State
  updateBookmarkUI(q.id);

  // Question Text
  document.getElementById('questionText').textContent = q.question;

  // Render Options By Tab Mode
  optionsDiv.innerHTML = '';
  explanationCard.classList.add('hidden');
  const explLabel = document.getElementById('explBtnLabel');
  if (explLabel) explLabel.textContent = 'Show Explanation';
  const explTextEl = document.getElementById('explanationText');

  // Helper for rendering option label with sign image if present
  function getOptHTML(optIdx, labelText) {
    if (q.option_images && q.option_images[optIdx]) {
      return `<div style="display:flex; align-items:center; gap:0.75rem; width:100%;">
        <div style="background:#fff; padding:4px; border-radius:8px; display:inline-flex; align-items:center; justify-content:center; box-shadow:0 2px 6px rgba(0,0,0,0.15); flex-shrink:0;">
          <img src="${q.option_images[optIdx]}" style="max-height:75px; max-width:85px; object-fit:contain;" alt="Option ${optIdx+1}">
        </div>
        <span style="font-weight:700; font-size:0.92rem;">${labelText}</span>
      </div>`;
    }
    return `<span>${labelText}</span>`;
  }

  // Prepare explanation HTML with visual diagram if available
  let diagramHTML = '';
  if (q.diagram) {
    diagramHTML = getDiagramHTML(q.diagram, currentModule);
  }

  const formattedExpl = (q.explanation || 'Official Taiwan Road Traffic Safety Rule.')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/(🎯 [^\n:]+:)/g, '<strong style="color:#34d399; display:block; margin-bottom:0.25rem; font-size:0.95rem;">$1</strong>')
    .replace(/(❌ [^\n:]+:)/g, '<strong style="color:#f87171; display:block; margin-top:0.65rem; margin-bottom:0.25rem; font-size:0.95rem;">$1</strong>')
    .replace(/(✅ [^\n:]+:)/g, '<strong style="color:#60a5fa; display:block; margin-top:0.65rem; margin-bottom:0.25rem; font-size:0.95rem;">$1</strong>')
    .replace(/(💡 [^\n:]+:)/g, '<strong style="color:#fbbf24; display:block; margin-top:0.65rem; margin-bottom:0.25rem; font-size:0.95rem;">$1</strong>')
    .replace(/\n\n/g, '<br/><br/>')
    .replace(/\n/g, '<br/>');

  explTextEl.innerHTML = `<div style="line-height:1.6; font-size:0.92rem; color:var(--text-main);">${formattedExpl}</div>${diagramHTML}`;

  if (currentTab === 'sheppard1') {
    // Mode 1: SHOW ONLY CORRECT ANSWER (Clickable to mark studied)
    const optBtn = document.createElement('button');
    optBtn.className = 'opt-btn correct-highlight';
    optBtn.style.width = '100%';
    optBtn.style.cursor = 'pointer';
    
    const correctLabel = q.correct_answer || (q.options ? q.options[q.correct_index] : '');
    optBtn.innerHTML = `
      <div style="width:100%;">
        <div style="font-size:0.7rem; text-transform:uppercase; font-weight:800; color:#34d399; margin-bottom:0.35rem;">Sheppard Air Correct Recall Answer ${isStudied ? '(Marked Studied ✓)' : '(Click to Mark Studied)'}</div>
        <div>${getOptHTML(q.correct_index, correctLabel)}</div>
      </div>
      <span style="font-size:1.2rem; flex-shrink:0;">${isStudied ? '✓' : '👉'}</span>
    `;
    optBtn.addEventListener('click', () => {
      recordQuestionStudied(q.id);
      renderCurrentQuestion();
    });
    optionsDiv.appendChild(optBtn);
  } else if (currentTab === 'sheppard2') {
    // Mode 2: HIGHLIGHT CORRECT ANSWER IN GREEN (Clickable to mark studied)
    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('button');
      optBtn.style.width = '100%';
      optBtn.style.cursor = 'pointer';
      const isCorrect = (idx === q.correct_index);
      if (isCorrect) {
        optBtn.className = 'opt-btn correct-highlight';
        optBtn.innerHTML = `${getOptHTML(idx, optText)} <span style="font-weight:800; font-size:0.75rem; background:rgba(16,185,129,0.25); padding:0.2rem 0.5rem; border-radius:4px; flex-shrink:0;">${isStudied ? '✓ STUDIED' : 'CORRECT (CLICK)'}</span>`;
      } else {
        optBtn.className = 'opt-btn';
        optBtn.style.opacity = '0.5';
        optBtn.innerHTML = `${getOptHTML(idx, optText)}`;
      }
      optBtn.addEventListener('click', () => {
        recordQuestionStudied(q.id);
        renderCurrentQuestion();
      });
      optionsDiv.appendChild(optBtn);
    });
  } else if (currentTab === 'interactive') {
    // Mode 3: INTERACTIVE INSTANT RED/GREEN FEEDBACK
    const userSel = interactiveAnswered[q.id];

    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('button');
      optBtn.className = 'opt-btn';

      if (userSel !== undefined) {
        if (idx === q.correct_index) {
          optBtn.classList.add('correct-highlight');
          optBtn.innerHTML = `${getOptHTML(idx, optText)} <span style="flex-shrink:0;">✓ Correct</span>`;
        } else if (userSel === idx) {
          optBtn.classList.add('incorrect-highlight');
          optBtn.innerHTML = `${getOptHTML(idx, optText)} <span style="flex-shrink:0;">✗ Incorrect</span>`;
        } else {
          optBtn.style.opacity = '0.4';
          optBtn.innerHTML = `${getOptHTML(idx, optText)}`;
        }
      } else {
        optBtn.innerHTML = `${getOptHTML(idx, optText)}`;
        optBtn.addEventListener('click', () => {
          interactiveAnswered[q.id] = idx;
          if (idx === q.correct_index) {
            recordQuestionStudied(q.id);
          } else {
            if (!m.failedQuestions.includes(q.id)) {
              m.failedQuestions.push(q.id);
              saveStateToStorage();
            }
          }
          renderCurrentQuestion();
        });
      }
      optionsDiv.appendChild(optBtn);
    });

    if (userSel !== undefined) {
      explanationCard.classList.remove('hidden');
      if (explLabel) explLabel.textContent = 'Hide Explanation';
    }
  } else if (currentTab === 'practice') {
    // Mode 4: PRACTICE EXAM CHOICES
    const userSel = examUserAnswers[q.id];

    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('button');
      optBtn.className = 'opt-btn';

      if (userSel === idx) {
        optBtn.style.borderColor = 'var(--accent-indigo)';
        optBtn.style.backgroundColor = 'rgba(99,102,241,0.2)';
        optBtn.innerHTML = `${getOptHTML(idx, optText)} <span style="flex-shrink:0;">Selected</span>`;
      } else {
        optBtn.innerHTML = `${getOptHTML(idx, optText)}`;
      }

      optBtn.addEventListener('click', () => {
        if (!examSubmitted) {
          examUserAnswers[q.id] = idx;
          renderCurrentQuestion();
        }
      });
      optionsDiv.appendChild(optBtn);
    });
  } else {
    // Bookmarks / Failed Mode -> Interactive Self-Test (Answer and explanation hidden until option selected)
    const userSel = bookmarksAnswered[q.id];

    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('button');
      optBtn.className = 'opt-btn';

      if (userSel !== undefined) {
        if (idx === q.correct_index) {
          optBtn.classList.add('correct-highlight');
          optBtn.innerHTML = `${getOptHTML(idx, optText)} <span style="flex-shrink:0;">✓ Correct</span>`;
        } else if (userSel === idx) {
          optBtn.classList.add('incorrect-highlight');
          optBtn.innerHTML = `${getOptHTML(idx, optText)} <span style="flex-shrink:0;">✗ Incorrect</span>`;
        } else {
          optBtn.style.opacity = '0.4';
          optBtn.innerHTML = `${getOptHTML(idx, optText)}`;
        }
      } else {
        optBtn.innerHTML = `${getOptHTML(idx, optText)}`;
        optBtn.addEventListener('click', () => {
          bookmarksAnswered[q.id] = idx;
          if (idx === q.correct_index) {
            recordQuestionStudied(q.id);
          } else {
            if (!m.failedQuestions.includes(q.id)) {
              m.failedQuestions.push(q.id);
              saveStateToStorage();
            }
          }
          renderCurrentQuestion();
        });
      }
      optionsDiv.appendChild(optBtn);
    });

    if (userSel !== undefined) {
      explanationCard.classList.remove('hidden');
      if (explLabel) explLabel.textContent = 'Hide Explanation';
    } else {
      explanationCard.classList.add('hidden');
      if (explLabel) explLabel.textContent = 'Show Explanation';
    }
  }

  // Update Nav Buttons & Submit Exam Visibility
  const submitBtn = document.getElementById('submitExamBtn');
  const mobileSubmitBtn = document.getElementById('mobileSubmitBtn');
  const isPracticeActive = (currentTab === 'practice' && !examSubmitted);

  if (submitBtn) {
    if (isPracticeActive) submitBtn.classList.remove('hidden');
    else submitBtn.classList.add('hidden');
  }
  if (mobileSubmitBtn) {
    if (isPracticeActive) mobileSubmitBtn.classList.remove('hidden');
    else mobileSubmitBtn.classList.add('hidden');
  }

  const isFirst = (currentIndex === 0 || filteredQuestions.length === 0);
  const isLast = (currentIndex === filteredQuestions.length - 1 || filteredQuestions.length === 0);

  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const mobilePrevBtn = document.getElementById('mobilePrevBtn');
  const mobileNextBtn = document.getElementById('mobileNextBtn');

  if (prevBtn) prevBtn.disabled = isFirst;
  if (nextBtn) nextBtn.disabled = isLast;
  if (mobilePrevBtn) mobilePrevBtn.disabled = isFirst;
  if (mobileNextBtn) mobileNextBtn.disabled = isLast;

  // Contextual Failed Question Removal Buttons
  const removeFailedBtn = document.getElementById('removeFailedBtn');
  const actionFailedBtn = document.getElementById('actionFailedBtn');
  if (currentTab === 'failed') {
    if (removeFailedBtn) removeFailedBtn.classList.remove('hidden');
    if (actionFailedBtn) actionFailedBtn.classList.remove('hidden');
  } else {
    if (removeFailedBtn) removeFailedBtn.classList.add('hidden');
    if (actionFailedBtn) actionFailedBtn.classList.add('hidden');
  }
}

function updateBookmarkUI(qId) {
  const m = getModuleData();
  const isBookmarked = m.bookmarks.includes(qId);
  const btn = document.getElementById('bookmarkBtn');
  if (btn) {
    if (isBookmarked) {
      btn.classList.add('bookmarked');
      btn.textContent = '★';
      btn.title = 'Click to remove from Bookmarks';
    } else {
      btn.classList.remove('bookmarked');
      btn.textContent = '☆';
      btn.title = 'Click to star / add to Bookmarks';
    }
  }
}

function recordQuestionStudied(qId) {
  if (!qId) return;
  const m = getModuleData();
  if (!m.studiedQuestions.includes(qId)) {
    m.studiedQuestions.push(qId);
    saveStateToStorage();
  }
}

// PRACTICE EXAM LOGIC
function startPracticeExam() {
  examSubmitted = false;
  examUserAnswers = {};

  const shuffled = [...allQuestions].sort(() => 0.5 - Math.random());
  examQuestions = shuffled.slice(0, Math.min(50, allQuestions.length));

  document.getElementById('questionContainer').classList.remove('hidden');
  document.getElementById('examResultCard').classList.add('hidden');

  updateFilteredQuestions();
  renderCurrentQuestion();
}

function submitPracticeExam() {
  examSubmitted = true;
  let correctCount = 0;
  const m = getModuleData();

  examQuestions.forEach(q => {
    const userSel = examUserAnswers[q.id];
    if (userSel === q.correct_index) {
      correctCount++;
    } else {
      if (!m.failedQuestions.includes(q.id)) {
        m.failedQuestions.push(q.id);
      }
    }
  });

  const total = examQuestions.length || 1;
  const scorePercent = Math.round((correctCount / total) * 100);
  const passed = scorePercent >= 85;

  m.examHistory.push({
    date: new Date().toISOString(),
    score: scorePercent,
    passed: passed,
    totalCount: total,
    correctCount: correctCount
  });

  saveStateToStorage();

  const questionCard = document.getElementById('questionContainer');
  const resultCard = document.getElementById('examResultCard');

  questionCard.classList.add('hidden');
  resultCard.classList.remove('hidden');

  document.getElementById('examResultTitle').textContent = passed ? '🎉 Exam Passed!' : '⚠️ Exam Not Passed';
  document.getElementById('examResultScore').textContent = `${scorePercent}% (${correctCount} / ${total} Correct)`;
  document.getElementById('examResultScore').style.color = passed ? 'var(--accent-emerald)' : 'var(--accent-rose)';
  document.getElementById('examResultStatus').textContent = passed
    ? `Congratulations! You scored ${scorePercent}%. Taiwan Highway Bureau requires 85% to pass.`
    : `You scored ${scorePercent}%. Passing score is 85%. Review failed questions and retake when ready!`;
}

// RENDER CHEAT SHEET
function renderCheatSheet() {
  const container = document.getElementById('cheatSheetContainer');
  container.innerHTML = '';

  cheatSheetData.forEach(sec => {
    const secCard = document.createElement('div');
    secCard.className = 'cheat-card';

    let itemsHTML = sec.items.map(item => `
      <div class="cheat-row">
        <span class="cheat-label">${item.label}</span>
        <span class="cheat-badge">${item.value || item.val || ''}</span>
      </div>
    `).join('');

    secCard.innerHTML = `
      <div class="cheat-head">
        <span>${sec.category}</span>
      </div>
      <div>${itemsHTML}</div>
    `;
    container.appendChild(secCard);
  });
}

function getDiagramHTML(diagramKey, moduleType) {
  const isCar = moduleType === 'car';
  if (diagramKey === 'car_door') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="35" width="120" height="40" rx="8" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="55" cy="75" r="10" fill="#64748b"/>
        <circle cx="125" cy="75" r="10" fill="#64748b"/>
        <line x1="120" y1="35" x2="160" y2="10" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
        <circle cx="160" cy="10" r="4" fill="#ef4444"/>
        <text x="240" y="45" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Car Door Warning!</text>
        <text x="240" y="65" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Fine: NT$2,400–4,800</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'phone_fine') {
    const fineText = isCar ? "Fine: NT$3,000 (Car)" : "Fine: NT$1,000 (Moto)";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="60" y="20" width="35" height="60" rx="5" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
        <rect x="67" y="27" width="21" height="40" rx="2" fill="#38bdf8"/>
        <circle cx="77" cy="73" r="2.5" fill="#f59e0b"/>
        <circle cx="77" cy="50" r="28" fill="none" stroke="#ef4444" stroke-width="4"/>
        <line x1="57" y1="30" x2="97" y2="70" stroke="#ef4444" stroke-width="4"/>
        <text x="220" y="45" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">No Handheld Phone</text>
        <text x="220" y="65" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">${fineText}</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'seatbelt_law') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="40" y="20" width="80" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <line x1="45" y1="25" x2="115" y2="75" stroke="#10b981" stroke-width="6"/>
        <text x="230" y="45" fill="#10b981" font-size="13" font-weight="800" text-anchor="middle">Seatbelt Mandatory</text>
        <text x="230" y="65" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">All Occupants (Front & Rear)</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'speed_limit_50') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <circle cx="80" cy="50" r="32" fill="#ffffff" stroke="#ef4444" stroke-width="7"/>
        <text x="80" y="60" fill="#0f172a" font-size="26" font-weight="900" text-anchor="middle">50</text>
        <text x="230" y="45" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Max Speed 50 km/h</text>
        <text x="230" y="65" fill="#94a3b8" font-size="11" text-anchor="middle">Unmarked Urban Roads</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'speed_limit_40') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <circle cx="80" cy="50" r="32" fill="#ffffff" stroke="#ef4444" stroke-width="7"/>
        <text x="80" y="60" fill="#0f172a" font-size="26" font-weight="900" text-anchor="middle">40</text>
        <text x="230" y="45" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Max Speed 40 km/h</text>
        <text x="230" y="65" fill="#94a3b8" font-size="11" text-anchor="middle">Slow Lanes & Narrow Roads</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'railroad_crossing') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <line x1="30" y1="70" x2="130" y2="70" stroke="#94a3b8" stroke-width="6"/>
        <line x1="50" y1="55" x2="50" y2="85" stroke="#e2e8f0" stroke-width="4"/>
        <line x1="80" y1="55" x2="80" y2="85" stroke="#e2e8f0" stroke-width="4"/>
        <line x1="110" y1="55" x2="110" y2="85" stroke="#e2e8f0" stroke-width="4"/>
        <rect x="140" y="30" width="30" height="30" fill="#ef4444" rx="4"/>
        <text x="155" y="50" fill="#ffffff" font-size="10" font-weight="900" text-anchor="middle">SOS</text>
        <text x="250" y="40" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Railroad Crossing</text>
        <text x="250" y="60" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Max 15 km/h / Press SOS Button</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'braking_physics') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <text x="40" y="35" fill="#38bdf8" font-size="11" font-weight="800">1x Speed (40km/h) → 1x Distance</text>
        <rect x="40" y="42" width="40" height="8" rx="2" fill="#38bdf8"/>
        <text x="40" y="70" fill="#ef4444" font-size="11" font-weight="800">2x Speed (80km/h) → 4x Distance (Quadrupled!)</text>
        <rect x="40" y="77" width="160" height="8" rx="2" fill="#ef4444"/>
      </svg>
    </div>`;
  } else if (diagramKey === 'siren_yield') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="30" width="70" height="40" rx="6" fill="#dc2626"/>
        <path d="M 40 30 Q 65 10 90 30" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="3"/>
        <text x="65" y="55" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">AMBULANCE</text>
        <text x="230" y="45" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Must Yield to Emergency Siren</text>
        <text x="230" y="65" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Violation = License Revocation!</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'traffic_light') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="20" width="100" height="60" rx="10" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        <circle cx="50" cy="50" r="12" fill="#ef4444"/>
        <circle cx="80" cy="50" r="12" fill="#f59e0b"/>
        <circle cx="110" cy="50" r="12" fill="#10b981"/>
        <text x="240" y="40" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Solid Red: Stop Behind Line</text>
        <text x="240" y="60" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Red Light Fine + 3 Demerit Points</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'demerit_points') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <circle cx="70" cy="50" r="28" fill="#7e22ce" stroke="#c084fc" stroke-width="3"/>
        <text x="70" y="58" fill="#ffffff" font-size="20" font-weight="900" text-anchor="middle">12pt</text>
        <text x="230" y="45" fill="#c084fc" font-size="13" font-weight="800" text-anchor="middle">12 Demerit Points in 1 Year</text>
        <text x="230" y="65" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">= 2-Month Driver License Suspension</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'cpr_protocol') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="30" width="90" height="40" rx="8" fill="#0284c7"/>
        <text x="75" y="55" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">30 : 2</text>
        <text x="230" y="40" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">CPR Protocol (30 Compressions : 2 Breaths)</text>
        <text x="230" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Depth: 5-6 cm | Rate: 100-120/min</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'cargo_rear') {
    const extText = isCar ? "Max 30 cm Past Bumper" : "Max 50 cm Past Rear Axle";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="40" y="45" width="130" height="25" rx="4" fill="#3b82f6"/>
        <circle cx="65" cy="73" r="10" fill="#64748b"/>
        <circle cx="145" cy="73" r="10" fill="#64748b"/>
        <rect x="170" y="40" width="30" height="30" fill="#f59e0b" rx="3"/>
        <line x1="145" y1="80" x2="200" y2="80" stroke="#ef4444" stroke-width="2" stroke-dasharray="3"/>
        <text x="260" y="45" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">Cargo Extension Limit</text>
        <text x="260" y="65" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">${extText}</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'right_of_way') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <line x1="30" y1="50" x2="150" y2="50" stroke="#10b981" stroke-width="4"/>
        <polygon points="150,45 160,50 150,55" fill="#10b981"/>
        <text x="240" y="45" fill="#10b981" font-size="12" font-weight="800" text-anchor="middle">Intersection Right-of-Way</text>
        <text x="240" y="65" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Straight-Going Vehicle (Priority #1)</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'alcohol_limit') {
    const fineText = isCar ? "Fine: NT$30k–120k" : "Fine: NT$15k–90k";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="40" width="120" height="20" rx="4" fill="#334155"/>
        <rect x="30" y="40" width="40" height="20" rx="4" fill="#10b981"/>
        <line x1="70" y1="25" x2="70" y2="75" stroke="#ef4444" stroke-width="3"/>
        <text x="70" y="20" fill="#ef4444" font-size="10" font-weight="800" text-anchor="middle">BAC 0.15 mg/L</text>
        <text x="230" y="45" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Legal BAC Limit: 0.15 mg/L</text>
        <text x="230" y="65" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">${fineText} / Refusal: NT$180k</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'tire_tread') {
    const depthText = isCar ? "Min Tread: 1.6 mm (Car)" : "Min Tread: 1.0 mm (Moto)";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="30" width="100" height="40" fill="#334155" rx="6"/>
        <line x1="60" y1="30" x2="60" y2="70" stroke="#f59e0b" stroke-width="4"/>
        <line x1="90" y1="30" x2="90" y2="70" stroke="#f59e0b" stroke-width="4"/>
        <text x="230" y="45" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Tire Inspection Standard</text>
        <text x="230" y="65" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">${depthText}</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'freeway_distance') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="40" width="45" height="20" rx="3" fill="#3b82f6"/>
        <rect x="120" y="40" width="45" height="20" rx="3" fill="#3b82f6"/>
        <line x1="75" y1="50" x2="120" y2="50" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
        <text x="250" y="45" fill="#10b981" font-size="12" font-weight="800" text-anchor="middle">Safe Distance = Speed ÷ 2</text>
        <text x="250" y="65" fill="#38bdf8" font-size="11" text-anchor="middle">50m @ 100km/h (Double in rain)</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'child_seat') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="25" width="100" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="80" cy="50" r="14" fill="#f59e0b"/>
        <text x="240" y="45" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Child Safety Seat Law</text>
        <text x="240" y="65" fill="#94a3b8" font-size="11" text-anchor="middle">Under 4 yrs / 18kg → Mandatory Rear Seat</text>
      </svg>
    </div>`;
  }
  return `<div class="rule-diagram-box"><svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;"><circle cx="170" cy="50" r="30" fill="#ffffff" stroke="#ef4444" stroke-width="5"/><text x="170" y="60" fill="#0f172a" font-size="24" font-weight="900" text-anchor="middle">50</text></svg></div>`;
}

// RENDER MASTER RULES (MODE 0: TOPIC DEEP DIVES)
function renderMasterRules() {
  const container = document.getElementById('masterRulesContainer');
  if (!container) return;
  container.innerHTML = '';

  if (!masterRulesData || masterRulesData.length === 0) {
    container.innerHTML = '<div class="empty-state">No master rules available for this vehicle category.</div>';
    return;
  }

  masterRulesData.forEach(rule => {
    const card = document.createElement('div');
    card.className = 'master-rule-card';

    // 1. Header
    const qCount = rule.related_questions ? rule.related_questions.length : (rule.matched_question_count || 0);
    const headerHTML = `
      <div class="master-header">
        <div class="master-title">${rule.title}</div>
        <div class="master-badges">
          <span class="cheat-badge" style="background:rgba(99,102,241,0.2); color:#a5b4fc; border-color:rgba(99,102,241,0.4);">${rule.category || 'Topic Cluster'}</span>
          <span class="cheat-badge" style="background:rgba(168,85,247,0.2); color:#c084fc; border-color:rgba(168,85,247,0.4);">${qCount} Questions Mapped</span>
        </div>
      </div>
    `;

    // 2. Summary
    const summaryHTML = `
      <div class="master-summary">${rule.summary || ''}</div>
    `;

    // 3. Key Numbers / Formulas Pills
    let pillsHTML = '';
    if (rule.key_numbers && rule.key_numbers.length > 0) {
      const pills = rule.key_numbers.map(numStr => `<span class="master-pill">⚡ ${numStr}</span>`).join('');
      pillsHTML = `
        <div>
          <div style="font-size:0.75rem; font-weight:800; text-transform:uppercase; color:var(--accent-indigo); margin-bottom:0.4rem;">🔑 Key Metrics, Distances & Numbers</div>
          <div class="master-pills-container">${pills}</div>
        </div>
      `;
    }

    // 4. Fines & Penalties Table
    let finesHTML = '';
    if (rule.fines_table && rule.fines_table.length > 0) {
      const rows = rule.fines_table.map(f => `
        <tr>
          <td style="font-weight:700;">${f.violation}</td>
          <td style="color:#f59e0b; font-weight:800; white-space:nowrap;">${f.amount}</td>
          <td style="color:#ef4444; font-weight:700;">${f.points_or_penalty}</td>
          <td style="color:var(--text-muted); font-size:0.78rem;">${f.why}</td>
        </tr>
      `).join('');

      finesHTML = `
        <div>
          <div style="font-size:0.75rem; font-weight:800; text-transform:uppercase; color:var(--accent-indigo); margin-bottom:0.4rem;">⚖️ Fine Amounts & Legal Penalties Matrix</div>
          <div class="master-fines-table-wrapper">
            <table class="master-fines-table">
              <thead>
                <tr>
                  <th>Traffic Violation</th>
                  <th>Statutory Fine</th>
                  <th>Points / Penalty</th>
                  <th>Legal Rationale & Safety Logic</th>
                </tr>
              </thead>
              <tbody>${rows}</tbody>
            </table>
          </div>
        </div>
      `;
    }

    // 5. Tricky Bookmarks Callouts
    let trapsHTML = '';
    if (rule.tricky_bookmarks && rule.tricky_bookmarks.length > 0) {
      const trapCards = rule.tricky_bookmarks.map(tb => `
        <div class="master-trap-card">
          <div class="master-trap-header">
            <span>⚠️ TRAP ALERT</span>
            <span class="cheat-badge" style="background:rgba(245,158,11,0.2); color:#fbbf24;">[${tb.question_id}]</span>
          </div>
          <div class="master-trap-q">${tb.question_text}</div>
          <div class="master-trap-ans">✅ Correct Answer: ${tb.correct_answer}</div>
          <div class="master-trap-exp">💡 Why it tricks students: ${tb.trap_explanation}</div>
        </div>
      `).join('');

      trapsHTML = `
        <div>
          <div style="font-size:0.75rem; font-weight:800; text-transform:uppercase; color:#f59e0b; margin-bottom:0.4rem;">🎯 Bookmarked Questions & Tricky Traps Explored</div>
          <div class="master-traps-container">${trapCards}</div>
        </div>
      `;
    }

    // 6. Practice Action Button
    let practiceBtnHTML = '';
    if (rule.related_questions && rule.related_questions.length > 0) {
      practiceBtnHTML = `
        <button class="master-practice-btn" onclick="practiceRuleQuestions('${rule.id}')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
          Practice this Topic (${rule.related_questions.length} Questions)
        </button>
      `;
    }

    card.innerHTML = `
      ${headerHTML}
      ${summaryHTML}
      ${pillsHTML}
      ${finesHTML}
      ${trapsHTML}
      ${practiceBtnHTML}
    `;

    container.appendChild(card);
  });
}

function practiceRuleQuestions(ruleId) {
  const rule = masterRulesData.find(r => r.id === ruleId);
  if (!rule || !rule.related_questions || rule.related_questions.length === 0) return;

  const qIds = new Set(rule.related_questions);
  filteredQuestions = allQuestions.filter(q => qIds.has(q.id));
  if (filteredQuestions.length === 0) {
    alert('No questions found for this topic.');
    return;
  }

  currentQuestionIndex = 0;
  switchTab('all');
  if (currentMode === 'interactive') {
    // start interactive quiz for this cluster
    interactiveQuestions = [...filteredQuestions];
    interactiveCurrentIndex = 0;
    interactiveScore = 0;
    renderInteractiveQuiz();
  } else {
    renderCurrentQuestion();
  }
}

// DASHBOARD STATS
function updateDashboardStats() {
  const m = getModuleData();

  const bmBadge = document.getElementById('navBookmarkBadge');
  const failBadge = document.getElementById('navFailedBadge');
  if (bmBadge) bmBadge.textContent = m.bookmarks.length;
  if (failBadge) failBadge.textContent = m.failedQuestions.length;

  const statMastered = document.getElementById('statMastered');
  const statFailed = document.getElementById('statFailed');
  if (statMastered) statMastered.textContent = m.studiedQuestions.length;
  if (statFailed) statFailed.textContent = m.failedQuestions.length;

  const total = allQuestions.length || 1;
  const studiedRatio = Math.min(1, m.studiedQuestions.length / total);
  const readiness = Math.round(studiedRatio * 100);

  const scoreEl = document.getElementById('readinessScore');
  const barEl = document.getElementById('readinessBar');
  if (scoreEl) scoreEl.textContent = `${readiness}%`;
  if (barEl) barEl.style.width = `${readiness}%`;
}

function getEmptyMessage() {
  if (currentTab === 'bookmarks') {
    return 'No bookmarked questions in this module yet. Click star (☆) on any question to add it here!';
  } else if (currentTab === 'failed') {
    return 'No failed questions! Try the Interactive Quiz or 50-Q Practice Exam to test your skills.';
  } else {
    return 'No questions match your current search/filter criteria.';
  }
}
