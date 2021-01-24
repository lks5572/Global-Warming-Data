import requests, numpy as np, matplotlib.pyplot as plt

link = "https://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts+dSST.txt"
f = requests.get(link)
data = f.text
lines = data.split('\n')

annMean = []
Jan = []
Feb = []
Mar = []
Apr = []
May = []
Jun = []
Jul = []
Aug = []
Sep = []
Oct = []
Nov = []
Dec = []
Year = []
def MakeList(name, start, end):
    for each in lines[8:]:
        if each == '' or not each.isdigit() and len(each) < 4:
            pass
        else:
            if each[39].isdigit() and each[70] != "*":
                name.append(each[start:end])
            else:
                pass
        for i in name:
            for i in range(0, len(name)):
                name[i] = int(name[i])
MakeList(Jan, 6, 10)
MakeList(Feb, 11, 15)
MakeList(Mar, 16, 20)
MakeList(Apr, 21, 25)
MakeList(May, 26, 30)
MakeList(Jun, 31, 35)
MakeList(Jul, 36, 40)
MakeList(Aug, 41, 45)
MakeList(Sep, 46, 50)
MakeList(Oct, 51, 55)
MakeList(Nov, 56, 60)
MakeList(Dec, 61, 66)
MakeList(annMean, 69, 72)

month_dict = {'Jan':Jan, 'Feb':Feb, 'Mar':Mar, 'Apr':Apr, 'May':May, 'Jun':Jun, 'Jul':Jul, 'Aug':Aug, 'Sep':Sep, 'Oct':Oct, 'Nov':Nov, 'Dec':Dec}
month_list = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

#1
print(((sum(annMean) / len(annMean)) / 100) * 1.8)

#2
for each in month_dict:
    sum1 = sum(month_dict[each])
    avg = sum1 / len(month_dict[each])
    min1 = min(month_dict[each])
    max1 = max(month_dict[each])
    minyear = month_dict[each].index(min1) + 1880
    maxyear = month_dict[each].index(max1) + 1880
    print(each, avg, min1, minyear, max1, maxyear)

#3
def month_range(month, year1, year2):
    x = year1 - 1880
    y = year2 - 1879
    return month[x:y]
def year_range(year1, year2):
    years = list(range(1880, 2020))
    x = years.index(year1)
    y = years.index(year2) + 1
    return years[x:y]

#4
for each in month_dict:
    plt.plot(year_range(1880,2018), month_range(month_dict[each], 1880, 2018))
    plt.xlabel("Years")
    plt.ylabel(each+'Temperature')
    plt.figure()
plt.show()

#5
plt.plot(year_range(1880,2018), annMean)
plt.xlabel('Years')
plt.ylabel('Avg. Temp')
plt.show()

#6
for each in month_list:
    plt.plot(year_range(2000, 2017), month_range(each, 2000, 2017))
    plt.xlabel('Years')
    plt.ylabel('Monthly Avg. Temp')
plt.show()

#7
plt.plot(year_range(2000,2017), month_range(annMean, 2000, 2017))
plt.xlabel('Years')
plt.ylabel('Avg. Temp')
plt.show()

#8
for each in month_list:
    plt.plot(year_range(1990, 1999), month_range(each, 1990, 1999))
    plt.xlabel('Years')
    plt.ylabel('Monthly Avg. Temp')
plt.show()

#9
plt.plot(year_range(1990,1999), month_range(annMean, 1990, 1999))
plt.xlabel('Years')
plt.ylabel('Avg. Temp')
plt.show()
print((sum(month_range(annMean, 1990, 1999))) / len(month_range(annMean, 1990, 1999)))

#10
for each in month_list:
    plt.plot(year_range(1890, 1899), month_range(each, 1890, 1899))
    plt.xlabel('Years')
    plt.ylabel('Monthly Avg. Temp')
print((sum(month_range(annMean, 1890, 1899))) / len(month_range(annMean, 1890, 1899)))
plt.show()

#11
plt.figure()
for each in month_list:
    plt.plot(year_range(1880,1925), month_range(each, 1880, 1925))
    plt.xlabel('Years')
    plt.ylabel('Monthly Avg. Temp')
plt.figure()
for each in month_list:
    plt.plot(year_range(1926,1970), month_range(each, 1926, 1970))
    plt.xlabel('Years')
    plt.ylabel('Monthly Avg. Temp')
plt.figure()
for each in month_list:
    plt.plot(year_range(1971, 2018), month_range(each, 1971, 2018))
    plt.xlabel('Years')
    plt.ylabel('Monthly Avg. Temp')
plt.show()
print('1880 - 1925: ',(sum(month_range(annMean, 1880, 1925))) / len(month_range(annMean, 1880, 1925)))
print('1926 - 1970: ',(sum(month_range(annMean, 1926, 1970))) / len(month_range(annMean, 1926, 1970)))
print('1971 - 2018: ',(sum(month_range(annMean, 1971, 2018))) / len(month_range(annMean, 1971, 2018)))