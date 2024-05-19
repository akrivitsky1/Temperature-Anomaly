def main():
    ##empty list for temp values
    tempature = []
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
        ### split the list on the comma
        year,temp = line.split(",")
        ### turn the 2nd number of each list into a float
        temp = float(temp)
        ##we print out the first and 2nd index of the list
        ###print(line[0],line[1])
        ##adds temp values to the list
        tempature.append(temp)
    ##prints the list tempature
    print(tempature)
## use the function main
main()
