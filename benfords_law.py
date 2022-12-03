#
# Author: Blake Herring
# Description: This program is used to find out if a csv file follows what is known as Benford's Law. This is down by
#              prompting the user for a file that they present to the program which then takes the file and places
#              all of the numbers from the file into a list. This list is then sorted through and creates a dictionary
#              filled with the total amount of for what the number begins with starting with 1 and ending with 9. This
#              dictionary is then used to calculate the percentage that that number shows up in the file and compares it
#              to the percentages of Benford's Law and if the line up correctly with the error percentage therefore
#              determining if the file follows the law or not and presenting to the user the Benford's Law chart of the
#              file and telling the user if it follows or does not follow Benford's Law.
#
def main():
    '''
    This is the main function where the program begins by prompting for the user to input a csv file in to the program
    which will be set equal to the csv_file variable. After that a for loop runs through the text and appends all the
    lines into the list population by stripping off the end line if any and creating an item(s) for the list by
    splitting at the comma when there is one found. Next a for loop runs through the list population and while the
    variable places is in range of the length of the list then it will continue to loop. Next is a nested for loop that
    runs while place is in range of the length of what ever is at population[places]. In these for loops there is an if
    statement that checks if the first character in the item at population[places][place][0] is numeric and if it has
    been proven to be true then that item from the population list is added or appended rather into the values list.
    After the for loops have finished looping and the values list has all of the items that need to be in it then main
    runs the plot(values) function which returns the variables values_plot and total. After that the graph(values_plot,
    values, total) function is then run and then the csv file is closed and the program ends.
    :return:
    '''
    csv_file = open(input('Data file name:\n\n'))
    population = []
    values = []
    for line in csv_file:  # While line can be found in csv_file it loops
        population.append(line.strip('\n').split(','))
    for places in range(len(population)):  # While places in range of population it loops
        for place in range(len(population[places])):  # While place in range of population[places] it loops
            if population[places][place][0].isnumeric():  # If this character is a number it passes
                values.append(population[places][place])
    values_plot, total = plot(values)
    graph(values_plot, total)
    csv_file.close()


def plot(values):
    '''
    This is the plot function where values_plot is a dictionary the represents the frequency of the different numbers
    that appear within the file. Total represents the total amount of values in the file that fit the requirements for
    being counted in Benford's Law. It begins with a loop that will continue to loop as long as value is in range of
    the length of the values list. In the for loop there's an if statement that asks if the first character in a item
    in the value is inside of the values_plot dictionary and if it is not then it checks if the first character is also
    not zero but in the string form since the list is in strings for the items inside. If it passes both checks then
    that character is added to the dictionary as a key with a value of one and the Total increases by one. Then there's
    an else if the if statement fails that then checks if it is not a zero in the string form. If it is not a zero then
    the key then has its value increased by one and the total increases by one. Once the for loop has finished then the
    function returns the variables values_plot and total.
    :param values: This is the list of values that was found with in the file that the user inputed into the program.
    :return: values_plot: This is a dictionary that is filled with the number 1 through 9 and the number of times that
                          they appear within the file that was inputted by the user.
             total: This is a count of the total amount of numbers that appear that being the the numbers 1-9 that
                    appeared within the user's file.
    '''
    values_plot = {}
    total = 0
    for value in range(len(values)):  # While value in range of values it loops
        if values[value][0] not in values_plot:  # If values[value][0] in values_plot it doesn't pass
            if values[value][0] != '0':  # If values[value][0] is '0' it doesn't pass
                values_plot[values[value][0]] = 1
                total += 1
        else:  # Values[value][0] in values_plot passes
            if values[value][0] != '0':  # If values[value][0] is not '0' it passes
                values_plot[values[value][0]] += 1
                total += 1
    return values_plot, total


def graph(values_plot, total):
    '''
    This function is used to print out the graph of Benford's Law for the file that the user gave to the program. This
    begins with a while loop where the condition is that if index is in range of the length of values_plot + 1 to
    account for the not being a zero within the dictionary of values_plot. In this loop it prints out the current line
    that the index is at for the graph of Benford's Law for the user file that is being observed. In this graph the #
    represents the percentage of the file is filled with that beginning number. After the graph has been created then
    a loop ends once index is the size of the length of values_plot creating two variables value_percent which represent
    the current value and the percentage of times it appears in the file and benfords_percent which represents the
    percentage that the current value should be about in a range of +10 or -5 which is what the if statement checks for
    if they are not within those ranges than benfords_law is proven to be False however if the statement never passes
    then benfords_law is proven to be True. Once the while loop has finished then if benfords_law is True then
    Follows Benford's Law is printed however if benfords_law is False then Does not follow Benford's Law is printed.
    :param values_plot: This is a dictionary that is filled with the number 1 through 9 and the number of times that
                        they appear within the file that was inputted by the user.
    :param total: This is a count of the total amount of numbers that appear that being the the numbers 1-9 that
                  appeared within the user's file.
    :return:
    '''
    index = 1
    benfords_law = True
    benfords_list = [30, 18, 12, 10, 8, 7, 6, 5, 4]
    while index < len(values_plot) + 1:  # If value index < amount of items in values_plot it loops
        print(index, '|', '#' * int(((values_plot[str(index)]) / total) * 100))
        index += 1
    index = 0
    while index < len(values_plot):  # If value index < amount of items in values_plot it loops
        value_percent = int(((values_plot[str(index + 1)]) / total) * 100)
        benfords_percent = benfords_list[index]
        # when value_percent < (benfords_percent - 5) or value_percent > (benford_percent + 10) it passes
        if value_percent < (benfords_percent - 5) or value_percent > (benfords_percent + 10):
            benfords_law = False
        index += 1
    # when benfords_law == True it passes
    if benfords_law:
        print('\nFollows Benford\'s Law')
    else:  # when benfords_law == False it passes
        print('\nDoes not follow Benford\'s Law')
main()