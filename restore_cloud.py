import urllib.request
import json

url = 'https://jsonblob.com/api/jsonBlob/019fec96-40e6-7aae-b2ba-dc7e687d7c92'
recovery_data = {
  "diego": {
    "name": "Diego (Pilot Mode)",
    "motorcycle": {
      "bookmarks": [],
      "failedQuestions": [],
      "studiedQuestions": [],
      "examHistory": []
    },
    "car": {
      "bookmarks": [
        "CAR_0058", "CAR_0071", "CAR_0087", "CAR_0090", "CAR_0111", "CAR_0116", "CAR_0128", "CAR_0133", "CAR_0148", "CAR_0158", "CAR_0164", "CAR_0166"
      ],
      "failedQuestions": [],
      "studiedQuestions": [
        "CAR_0952", "CAR_0052", "CAR_0482", "CAR_0514", "CAR_0013", "CAR_0093", "CAR_0526", "CAR_0906", "CAR_0233", "CAR_0103", "CAR_0104", "CAR_0105", "CAR_0106", "CAR_0107", "CAR_0108", "CAR_0109", "CAR_0110", "CAR_0111", "CAR_0112", "CAR_0001", "CAR_0002", "CAR_0003", "CAR_0004", "CAR_0005", "CAR_0006", "CAR_0007", "CAR_0008", "CAR_0009", "CAR_0010", "CAR_0011", "CAR_0012", "CAR_0014", "CAR_0015", "CAR_0016", "CAR_0017", "CAR_0018", "CAR_0019", "CAR_0020", "CAR_0021", "CAR_0022", "CAR_0023", "CAR_0024", "CAR_0025", "CAR_0026", "CAR_0027", "CAR_0028", "CAR_0029", "CAR_0030", "CAR_0031", "CAR_0032", "CAR_0033", "CAR_0034", "CAR_0035", "CAR_0036", "CAR_0037", "CAR_0038", "CAR_0040", "CAR_0041", "CAR_0042", "CAR_0043", "CAR_0044", "CAR_0045", "CAR_0046", "CAR_0047", "CAR_0048", "CAR_0049", "CAR_0050", "CAR_0051", "CAR_0053", "CAR_0054", "CAR_0055", "CAR_0056", "CAR_0057", "CAR_0058", "CAR_0059", "CAR_0061", "CAR_0062", "CAR_0063", "CAR_0064", "CAR_0066", "CAR_0067", "CAR_0068", "CAR_0069", "CAR_0070", "CAR_0071", "CAR_0072", "CAR_0074", "CAR_0075", "CAR_0076", "CAR_0077", "CAR_0078", "CAR_0079", "CAR_0080", "CAR_0081", "CAR_0082", "CAR_0083", "CAR_0084", "CAR_0085", "CAR_0086", "CAR_0087", "CAR_0088", "CAR_0089", "CAR_0090", "CAR_0091", "CAR_0092", "CAR_0094", "CAR_0095", "CAR_0096", "CAR_0097", "CAR_0098", "CAR_0099", "CAR_0100", "CAR_0101", "CAR_0102", "CAR_0113", "CAR_0114", "CAR_0115", "CAR_0116", "CAR_0117", "CAR_0118", "CAR_0119", "CAR_0120", "CAR_0121", "CAR_0122", "CAR_0123", "CAR_0124", "CAR_0125", "CAR_0126", "CAR_0127", "CAR_0128", "CAR_0129", "CAR_0130", "CAR_0131", "CAR_0132", "CAR_0133", "CAR_0141", "CAR_0142", "CAR_0143", "CAR_0144", "CAR_0145", "CAR_0146", "CAR_0147", "CAR_0148", "CAR_0149", "CAR_0150", "CAR_0151", "CAR_0152", "CAR_0153", "CAR_0154", "CAR_0155", "CAR_0156", "CAR_0157", "CAR_0158", "CAR_0159", "CAR_0160", "CAR_0161", "CAR_0162", "CAR_0164", "CAR_0165", "CAR_0166", "CAR_0167", "CAR_0168"
      ],
      "examHistory": [],
      "lastIndices": {"sheppard1": 153}
    }
  },
  "johana": {
    "name": "Johana (Study Profile)",
    "motorcycle": {"bookmarks": [], "failedQuestions": [], "studiedQuestions": [], "examHistory": []},
    "car": {"bookmarks": [], "failedQuestions": [], "studiedQuestions": [], "examHistory": []}
  },
  "last_updated": 9999999999999
}

req_put = urllib.request.Request(url, data=json.dumps(recovery_data).encode('utf-8'), headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, method='PUT')
with urllib.request.urlopen(req_put) as resp:
    print('Restored Cloud Backup Status:', resp.status)
