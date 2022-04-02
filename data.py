import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

# to find the mean of the reading score of the student
readingScore_mean = statistics.mean(data)

#population_mean = statistics.mean(data)
#standard_deviation = statistics.stdev(data)


# to find the median of the reading score of the student 
readingScore_median = statistics.median(data)

# to find the mode of the reading score of the student 
readingScore_mode = statistics.mode(data)

print("Mean, Median, Mode of the data is {}, {}, {} respectively : ".format( readingScore_mean , readingScore_median ,readingScore_mode))

readingScore_std_deviation = statistics.stdev(data)

fig = ff.create_distplot([data],["reading score"],show_hist = False)
#fig.add_trace(go.scatter(x = [mean,mean], y = [0,1], mode = "lines",name = "name: "))
fig.show()

# 1st, 2nd and 3rd standard deviation of the data 

readingScore_first_deviation_start,readingScore_first_deviation_end =  readingScore_mean - readingScore_std_deviation , readingScore_mean  + readingScore_std_deviation
readingScore_second_deviation_start,readingScore_second_deviation_end =  readingScore_mean - readingScore_std_deviation ,  readingScore_mean  +(2*readingScore_std_deviation)
readingScore_third_deviation_start,readingScore_third_deviation_end =  readingScore_mean - readingScore_std_deviation , readingScore_mean +(3*readingScore_std_deviation)

readingScore_list_of_data_within_first_deviation = [result for result in data if result > readingScore_first_deviation_start and result<readingScore_first_deviation_end]
readingScore_list_of_data_within_second_deviation = [result for result in data if result > readingScore_second_deviation_start and result<readingScore_second_deviation_end]
readingScore_list_of_data_within_third_deviation = [result for result in data if result > readingScore_third_deviation_start and result<readingScore_third_deviation_end]


print(" {}% of data for reading score lies in within 1st standard deviation".format(len(readingScore_list_of_data_within_first_deviation)*100.0/len(data)))
print(" {}% of data for reading score lies in within 2nd standard deviation".format(len(readingScore_list_of_data_within_second_deviation)*100.0/len(data)))
print(" {}% of data for reading score lies in within 3rd standard deviation".format(len(readingScore_list_of_data_within_third_deviation)*100.0/len(data)))







