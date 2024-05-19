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
    ###print(tempature)
    ## asks user for a int input
    k = int(input("Enter window size:"))
    ###opens the file to write in
    outfile = open("MovingAve.csv","w")
    ##writes a colum header and creates new line
    outfile.write("Year,Value\n")
    ## for loop that starts from 0 index and goes till last index of the list
    for index in range(k,len(tempature)-k):
        ## forumula to calculate the moving average
        ave = sum(tempature[index-k:index+k+1]) / (2*k+1)
        year = 1880 + index
        ##prints out the moving result to the 4th decimal place and with a comma
        ##print("{},{:.4f}".format(year,ave))
        ##prints out the moving average formatted with a new line
        outfile.write("{},{:.4f}\n".format(year,ave))
        ##closes file 
    outfile.close()
## use the function main
main()
