"""
We must read in a text file.
Display the number of total grades in the text file
Add all the grades into a listA. 
Sum all the grades in the text file and divide by the total number of grades
Close the the file
Check to see if the grade in the listA is greater than the average, if so, add 
to listB
Divide sum of ListB by total number of grades.
Print to user total number of grades, average grade, and percentage of grades 
above the average.
"""
"""
main():
    grades = studentgrades("final.txt")

studentgrades():
    read in final.txt
    create list of all grades in file
    close file
    sum of total grades
    print total number of grades
    print average (sum of grades / number of grades)
percentaboveaverage():
    if index is above average:
        add to list
    print total of list / number of grade
main()
"""
def main():
    grades = studentgrades("final.txt")

def studentgrades(txt_file):
    infile = open(txt_file, "r")
    ListA = [numbers() for numbers in infile]
    infile.close()
    return len(ListA)
    Total = sum(ListA)
    Average = Total / len(ListA)
    return Average

def StudentAboveAverage():
    for i in ListA > Average:
        AboveAverage = []
        percentage = AboveAverage / len(ListA)
    return percentage

main()
