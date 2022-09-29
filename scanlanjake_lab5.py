"""Program to read from CSV files to get data from a specific column.
Produce the count(number of data), mean, min,max, and standard
deviation values. As well create a graph of that data."""

# Imports of different functions into program
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sets selection to zero
SELECTION = 0
# Enters while loop, selection does not equal 3 continue looping
while SELECTION != 3:
    # Try these statements to ensure correctness
    try:
        # Ask user what file they would like to obtain data from
        SELECTION = int(input("Hey there, which file would you like to experiment with"
                              " (Enter with number)?\n"
                              "1. Population Data\n"
                              "2. Housing Data\n"
                              "3. Exit the program and go home for a sick brunch\n"))
        # If selection is 1
        if SELECTION == 1:
            # Thanks user for selection population data
            print("Thank you for choosing population data:\n")
            # Sets popselect to 0
            POPSELECT = 0
            # Nested while loop, while popselect doesn't equal 4
            while POPSELECT != 4:
                # Tries these statements to ensure correctness
                try:
                    # Asks user which column they would like to get data for
                    POPSELECT = int(input("Which column would you like to analyze:\n"
                                          "1. Population Apr 1\n"
                                          "2. Population Jul 1\n"
                                          "3. Change Population\n"
                                          "4. Exit\n"))
                    # If popselect equals 1
                    if POPSELECT == 1:
                        # df(Dataframe) = pandas csv file reader
                        # reads the file location of PopChange.csv
                        # and specifies to use the column with
                        # usecols to read the "Pop Apr 1" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/lab5tools/PopChange.csv",
                                         usecols=["Pop Apr 1"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column Pop Apr 1:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins
                        # that start from 13519 and end at 3726157
                        # with the amount of 24 bins
                        # based on the square root
                        # of the number of values in the column
                        plt.hist(df["Pop Apr 1"], bins=np.linspace(13519, 3726157, num=24))
                        # Labels the x-axis
                        plt.xlabel("Number of Row")
                        # Labels the y-axis
                        plt.ylabel("Amount of population in April")
                        # Shows the plot
                        plt.show()

                    # If popselect is 2
                    elif POPSELECT == 2:
                        # df(Dataframe) = pandas csv file reader,
                        # reads the file location of PopChange.csv
                        # and specifies to use
                        # the column with usecols
                        # to read the "Pop Jul 1" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/lab5tools"
                                         "/PopChange.csv", usecols=["Pop Jul 1"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column Pop Jul 1:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins
                        # that start from 12619 and end at 3195153
                        # with the amount of 24 bins based on the square root
                        # of the number of values in the column
                        plt.hist(df["Pop Jul 1"], bins=np.linspace(12619, 3195153, num=24))
                        # Labels the x-axis
                        plt.xlabel("Number of Row")
                        # Labels the y-axis
                        plt.ylabel("Amount of population in July")
                        # Shows the plot
                        plt.show()

                    # If popselect is 3
                    elif POPSELECT == 3:
                        # df(Dataframe) = pandas csv file reader,
                        # reads the file location of PopChange.csv
                        # and specifies to use the column with
                        # usecols to read the
                        # "Change Pop" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/lab5tools"
                                         "/PopChange.csv", usecols=["Change Pop"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column Change Pop:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and
                        # formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins
                        # that start from -531004 and end at 22363
                        # with the amount of 24 bins based on the square root
                        # of the number of values in the column
                        plt.hist(df["Change Pop"], bins=np.linspace(-531004, 22363, num=24))
                        # Labels the x-axis
                        plt.xlabel("Number of Row")
                        # Labels the y-axis
                        plt.ylabel("Amount of population Change")
                        # Shows the plot
                        plt.show()

                    # If popselect is 4, exits loop and prints following statement
                    elif POPSELECT == 4:
                        print("Thank you for messing with the"
                              " populations of the world, it means alot!\n")
                # Checks if input is not of an int
                except ValueError:
                    # Prints error message and goes
                    # back to the
                    # top of the loop
                    print("Look we've been through this for "
                          "the past 5 weeks, we use NUMBERS here!\n")

        # If selection equals 2
        elif SELECTION == 2:
            # Thanks user for choosing housing data
            print("Thank you for choosing housing data.\n")
            # Sets houseselect to 0
            HOUSESELECT = 0
            # While houseselect does not equal 8 continue looping
            while HOUSESELECT != 8:
                # Try statements to detect errors
                try:
                    # Asks user which column of the file they would like to obtain info for
                    HOUSESELECT = int(input("Which column would you like to check:\n"
                                            "1. Age\n"
                                            "2. Bedrooms\n"
                                            "3. Built\n"
                                            "4. Nunits\n"
                                            "5. Rooms\n"
                                            "6. Weight\n"
                                            "7. Utility\n"
                                            "8. Exit\n"))
                    # If houseselect is 1
                    if HOUSESELECT == 1:
                        # df(Dataframe) = pandas csv file reader,
                        # reads the file location of Housing.csv
                        # and specifies to
                        # use the column with
                        # usecols to read
                        # the "AGE" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/"
                                         "lab5tools/Housing.csv", usecols=["AGE"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column AGE:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins
                        # that start from -9 and end at 93
                        # with the amount of 101 bins based on the square root
                        # of the number of values in the column
                        plt.hist(df["AGE"], bins=np.linspace(-9, 93, num=101))
                        # Labels the x-axis
                        plt.xlabel("Age of person")
                        # Labels the y-axis
                        plt.ylabel("Amount of people per age")
                        # Shows the plot
                        plt.show()

                    # If houseselect is 2
                    elif HOUSESELECT == 2:
                        # df(Dataframe) = pandas csv file reader,
                        # reads the file
                        # location of Housing.csv
                        # and specifies to
                        # use the column with
                        # usecols to read
                        # the "BEDRMS" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/"
                                         "lab5tools/Housing.csv", usecols=["BEDRMS"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column BEDRMS:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins that start from 0 and end at 7
                        # with the amount of 101 bins based on the square root
                        # of the number of values in the column
                        plt.hist(df["BEDRMS"], bins=np.linspace(0, 7, num=101))
                        # Labels the x-axis
                        plt.xlabel("Number of Row")
                        # Labels the y-axis
                        plt.ylabel("Amount of Bedrooms")
                        # Shows the plot
                        plt.show()
                    # If houseselect is 3
                    elif HOUSESELECT == 3:
                        # df(Dataframe) = pandas
                        # csv file reader,
                        # reads the file location of Housing.csv
                        # and specifies to
                        # use the column with
                        # usecols to read
                        # the "BUILT" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/"
                                         "lab5tools/Housing.csv", usecols=["BUILT"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column BUILT:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:",
                              f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f""
                                      f"{float(df.min()):.2f}\n")
                        # Prints the max value
                        # and formats 2 decimal places
                        print("Max:", f""
                                      f"{float(df.max()):.2f}\n")
                        # Plots the specified column,
                        # creates bins that start
                        # from 1919 and end at 2012
                        # with the amount of 101
                        # bins based on the square root
                        # of the number of values in the column
                        plt.hist(df["BUILT"], bins=np.linspace(1919, 2012, num=101))
                        # Labels the x-axis
                        plt.xlabel("Year built")
                        # Labels the y-axis
                        plt.ylabel("Number Built")
                        # Shows the plot
                        plt.show()
                    # If houseselect
                    # is 4
                    elif HOUSESELECT == 4:
                        # df(Dataframe) = pandas csv file reader,
                        # reads the file
                        # location of Housing.csv
                        # and specifies to
                        # use the column with
                        # usecols to read the "NUNITS" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/"
                                         "lab5tools/Housing.csv", usecols=["NUNITS"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column NUNITS:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins that start from 1 and end at 799
                        # with the amount of 101 bins based on the square root
                        # of the number of values in the column
                        plt.hist(df["NUNITS"], bins=np.linspace(1, 799, num=101))
                        # Labels the x-axis
                        plt.xlabel("Built per family size")
                        # Labels the y-axis
                        plt.ylabel("Number of Units")
                        # Shows the plot
                        plt.show()
                    # If houseselect is 5
                    elif HOUSESELECT == 5:
                        # df(Dataframe) =
                        # pandas csv file reader,
                        # reads the file
                        # location
                        # of Housing.csv
                        # and specifies to use the column with
                        # usecols to read
                        # the "ROOMS" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/"
                                         "lab5tools/Housing.csv", usecols=["ROOMS"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column ROOMS:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins
                        # that start from 1 and end at 14
                        # with the amount of 101 bins
                        # based on the square root
                        # of the number of values in the column
                        plt.hist(df["ROOMS"], bins=np.linspace(1, 14, num=101))
                        # Labels the x-axis
                        plt.xlabel("Family size")
                        # Labels the y-axis
                        plt.ylabel("Rooms built")
                        # Shows the plot
                        plt.show()

                    # If houseselect is 6
                    elif HOUSESELECT == 6:
                        # df(Dataframe) =
                        # pandas csv file reader,
                        # reads the file location of Housing.csv
                        # and specifies to
                        # use the column with
                        # usecols to read
                        # the "WEIGHT" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/"
                                         "lab5tools/Housing.csv", usecols=["WEIGHT"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column WEIGHT:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins
                        # that start from 0 and end at 19077
                        # with the amount of 101 bins
                        # based on the square root
                        # of the number of values in the column
                        plt.hist(df["WEIGHT"], bins=np.linspace(0, 19077, num=101))
                        # Labels the x-axis
                        plt.xlabel("Weight of house")
                        # Labels the y-axis
                        plt.ylabel("Number of houses built")
                        # Shows the plot
                        plt.show()

                    # If houseselect is 7
                    elif HOUSESELECT == 7:
                        # df(Dataframe) = pandas csv file reader,
                        # reads the file
                        # location of Housing.csv
                        # and specifies to
                        # use the column with
                        # usecols to read
                        # the "UTILITY" column
                        df = pd.read_csv("C:/Users/Jakes/Desktop/"
                                         "lab5tools/Housing.csv", usecols=["UTILITY"])
                        # Tells user which data they are obtaining
                        print("Here is the data for the column UTILITY:\n")
                        # Prints the length of the column(the amount of values inside)
                        print("Count:", len(df), "\n")
                        # Prints the mean of the values and formats 2 decimal places
                        print("Mean:", f"{float(df.mean()):.2f}\n")
                        # Prints the standard deviation of the values and formats 2 decimal places
                        print("Standard deviation:", f"{float(df.std()):.2f}\n")
                        # Prints the minimum value and formats 2 decimal places
                        print("Min:", f"{float(df.min()):.2f}\n")
                        # Prints the max value and formats 2 decimal places
                        print("Max:", f"{float(df.max()):.2f}\n")
                        # Plots the specified column, creates bins
                        # that start from 0 and end at 1107
                        # with the amount of 101 bins
                        # based on the square root
                        # of the number of values in the column
                        plt.hist(df["UTILITY"], bins=np.linspace(0, 1107, num=101))
                        # Labels the x-axis
                        plt.xlabel("Price of Utilities")
                        # Labels the y-axis
                        plt.ylabel("Amount of Utility use")
                        # Shows the plot
                        plt.show()
                    # If houseselect is 8
                    elif HOUSESELECT == 8:
                        # Exits loop, and thanks user for checking housing data
                        print("Thank you for checking out all "
                              "of our housing data and have a great day!\n")
                # Checks if user
                # input is not a number
                except ValueError:
                    # If user did not enter
                    # a number, prints error message
                    # and goes back
                    # to top of loop
                    print("Ok listen, the options are "
                          "specified by numbers. It might help to use those.\n")

        # If selection is 3
        elif SELECTION == 3:
            # Thanks user for using the program and exits
            print("We're sorry to see you go,"
                  " thank you so much for using our program"
                  " and have a great day")
    # Checks if user input is not a number
    except ValueError:
        # If number is not entered, prints error message
        # and goes back to top of loop
        print("Please use some numbers to make your choice!\n")
