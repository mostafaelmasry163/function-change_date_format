#function change_date_format which accepts a list of strings, representing dates, and returns a new list with each date in the format YYYYMMDD. all incoming dates will be valid dates, but only those in one of the following formates: YYYY/MM/DD, DD/MM/YYYY, and MM-DD-YYYY should be included in the returned list, where YYYY,MM,DD are numbers representing year, month, and day

# for example, change_date_format(["2010/03/30","15/12/2016"."11-15-2012","20130720"]) should return the list ["20100330","20161215","20121115"].

import datetime

def change_date_format(lst):
    result = []
    for dates in lst:
        try:
            if (datetime.datetime.strptime(dates,  "%m-%d-%Y")):
                result.append(datetime.datetime.strptime(
                    dates,  "%m-%d-%Y").date().strftime("%Y%m%d"))
        except:
            try:
                if (datetime.datetime.strptime(dates,  "%Y/%m/%d")):
                    result.append(datetime.datetime.strptime(
                        dates,  "%Y/%m/%d").date().strftime("%Y%m%d"))
            except:
                try:
                    if (datetime.datetime.strptime(dates,  "%d/%m/%Y")):
                        result.append(datetime.datetime.strptime(
                            dates,  "%d/%m/%Y").date().strftime("%Y%m%d"))
                except:
                    continue

    print(result)

    
change_date_format(["2010/03/30", "15/12/2016","11-15-2012", "20130720"])

