import json

raw = [
  {
    "Age group": "12 to 17",
    "Total": "711",
    "Male": "415",
    "Female": "331",
    "Other": 4,
    "Unknown": 10,
    "Number of doses administered by age group": "4,164,954",
    "Number of doses administered to males": "2,110,887",
    "Number of doses administered to females": "2,049,879",
    "Total number of doses administered1": "4,160,766",
    "Reporting rate by age group": 17.07,
    "Male reporting rate2": 19.66,
    "Female reporting rate2": 16.15,
    "Total reporting rate (males and females)1,2": 17.93
  },
  {
    "Age group": "18 to 29",
    "Total": "3,014",
    "Male": "1,006",
    "Female": "1,949",
    "Other": 14,
    "Unknown": 45,
    "Number of doses administered by age group": "9,657,300",
    "Number of doses administered to males": "4,860,474",
    "Number of doses administered to females": "4,770,111",
    "Total number of doses administered1": "9,630,585",
    "Reporting rate by age group": 31.21,
    "Male reporting rate2": 20.7,
    "Female reporting rate2": 40.86,
    "Total reporting rate (males and females)1,2": 30.68
  },
  {
    "Age group": "30 to 39",
    "Total": "3,927",
    "Male": "857",
    "Female": "2,991",
    "Other": 10,
    "Unknown": 69,
    "Number of doses administered by age group": "8,824,741",
    "Number of doses administered to males": "4,355,550",
    "Number of doses administered to females": "4,458,487",
    "Total number of doses administered1": "8,814,037",
    "Reporting rate by age group": 44.5,
    "Male reporting rate2": 19.68,
    "Female reporting rate2": 67.09,
    "Total reporting rate (males and females)1,2": 43.66
  },
  {
    "Age group": "40 to 49",
    "Total": "4,691",
    "Male": "893",
    "Female": "3,699",
    "Other": 15,
    "Unknown": 84,
    "Number of doses administered by age group": "8,450,753",
    "Number of doses administered to males": "4,121,630",
    "Number of doses administered to females": "4,321,814",
    "Total number of doses administered1": "8,443,444",
    "Reporting rate by age group": 55.51,
    "Male reporting rate2": 21.67,
    "Female reporting rate2": 85.59,
    "Total reporting rate (males and females)1,2": 54.39
  },
  {
    "Age group": "50 to 59",
    "Total": "4,665",
    "Male": "992",
    "Female": "3,576",
    "Other": 9,
    "Unknown": 88,
    "Number of doses administered by age group": "9,153,025",
    "Number of doses administered to males": "4,482,649",
    "Number of doses administered to females": "4,663,634",
    "Total number of doses administered1": "9,146,283",
    "Reporting rate by age group": 50.97,
    "Male reporting rate2": 22.13,
    "Female reporting rate2": 76.68,
    "Total reporting rate (males and females)1,2": 49.94
  },
  {
    "Age group": "60 to 69",
    "Total": "3,779",
    "Male": "976",
    "Female": "2,698",
    "Other": 7,
    "Unknown": 98,
    "Number of doses administered by age group": "8,887,061",
    "Number of doses administered to males": "4,311,978",
    "Number of doses administered to females": "4,570,116",
    "Total number of doses administered1": "8,882,094",
    "Reporting rate by age group": 42.52,
    "Male reporting rate2": 22.63,
    "Female reporting rate2": 59.04,
    "Total reporting rate (males and females)1,2": 41.36
  },
  {
    "Age group": "70 to 79",
    "Total": "2,239",
    "Male": "644",
    "Female": "1,537",
    "Other": 2,
    "Unknown": 56,
    "Number of doses administered by age group": "6,110,390",
    "Number of doses administered to males": "2,897,980",
    "Number of doses administered to females": "3,209,119",
    "Total number of doses administered1": "6,107,099",
    "Reporting rate by age group": 36.64,
    "Male reporting rate2": 22.22,
    "Female reporting rate2": 47.89,
    "Total reporting rate (males and females)1,2": 35.71
  },
  {
    "Age group": "80+",
    "Total": "1,326",
    "Male": "321",
    "Female": "975",
    "Other": 1,
    "Unknown": 29,
    "Number of doses administered by age group": "3,410,164",
    "Number of doses administered to males": "1,366,228",
    "Number of doses administered to females": "2,037,354",
    "Total number of doses administered1": "3,403,582",
    "Reporting rate by age group": 38.88,
    "Male reporting rate2": 23.5,
    "Female reporting rate2": 47.86,
    "Total reporting rate (males and females)1,2": 38.08
  },
  {
    "Age group": "Unknown",
    "Total": "766",
    "Male": "147",
    "Female": "362",
    "Other": 1,
    "Unknown": 256,
    "Number of doses administered by age group": "N/A",
    "Number of doses administered to males": "N/A",
    "Number of doses administered to females": "N/A",
    "Total number of doses administered1": "N/A",
    "Reporting rate by age group": "N/A",
    "Male reporting rate2": "N/A",
    "Female reporting rate2": "N/A",
    "Total reporting rate (males and females)1,2": "N/A"
  }
]


## For age group and total reports
# agTotal = {"key": "data", "values": []}
# for row in raw:
#     temp = row["Total"].replace(',', '')
#     total = int(temp)
#     agTotal["values"].append({"key": row["Age group"], "value":total})

# print(json.dumps(agTotal))


## For age group and rate
# agRate = {"key": "data", "values": []}
# for row in raw:
#     agRate["values"].append({"key": row["Age group"], "value":row["Reporting rate by age group"]})

# print(json.dumps(agRate))

# agMF=[{"key": "Male", "values": []},{"key": "Female", "values": []}]
# for row in raw:
#   temp = row["Male"].replace(',', '')
#   total = int(temp)
#   temp1 = row["Female"].replace(',', '')
#   total1= int(temp1)
#   agMF[0]["values"].append({"key":row["Age group"], "value":total})
#   agMF[1]["values"].append({"key":row["Age group"], "value":total1})


# print(json.dumps(agMF))

agMF=[{"key": "Male", "values": []},{"key": "Female", "values": []}]
for row in raw:
  agMF[0]["values"].append({"key":row["Age group"], "value":row["Male reporting rate2"]})
  agMF[1]["values"].append({"key":row["Age group"], "value":row["Female reporting rate2"]})


print(json.dumps(agMF))