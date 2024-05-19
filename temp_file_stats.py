def main():
    ##establish constants to use for getting min/max temp
    max_temp = None
    min_temp = None
    max_year="Not found"
    min_year="Not found"
    ##aks user to input a filename
    filename = input("Temperature anomaly filename:")
    ##opens the filename on read
    file = open(filename,"r")
    ##we read the header but ignore it
    file.readline()
    ##loop through each line in the file 
    for line in file:
        ##remove whitespace at the end
        line = line.strip("\n")
        ### split the list on the comma and place into 2 values
        year,temp = line.split(",")
        ###turns the temp val into a float
        temp = float(temp)
        ##compares the temp to the next temp and saves the lowest temp and year
        if min_temp == None or temp<min_temp:
            min_temp = temp
            min_year = year
        ## compares the temp to the next temp and saves the highest temp and year
        if max_temp == None or temp>max_temp:
            max_temp = temp
            max_year = year
    ##prints out the min and max temp alongside its years
    print("Min temp:",min_temp,"in",min_year)
    print("Max temp:",max_temp,"in",max_year)
## use the function main
main()
