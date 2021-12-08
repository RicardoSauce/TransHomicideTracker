# PPHA 30536: Data and Programming for Public Policy II
# Submission by: Ricardo Saucedo

## Final Project: Reproducible Research
## Autumn 2020


## Due: Sunday, December 6th by midnight on GitHub

### Project Introduction:

Transgender folx in the US have uncomfortably large homocide rates. The purpose of this project is not only to represent the visualizations of these homicides, but to promote more academic research on the LGBTQ+ community. 


A major disparity in research involving the queer community is that there is a small amount of accessible and publicy available data sets. For this reason, I created my own data set, a collection of csv files for each year containing three important variables for each instance of homicide: name, state and city, and year. What I am also hoping to illuminate with my research is a inherent connection between states and who they voted for in the US presidential election.

The steps needed to do this are:

1) Build the collection of CSVs on public transgender homicide.
2) Build two choropleth maps: one for homicide rates, and one for states and their elected official.
3) Conduct a linear regression to predict outcomes on states that either do not contain data or do not have death cases.

Hypothetically speaking, this project aims to reveal that there is a positive correlation between states that vote Republican and also have higher counts of homicides, or to contain some underlying inherent connection between the state's voting history and their homicide rates for Transgender folx.

### Methodology:
Publicly available on the LGBTQ is very limited. That being the case, I formed my data set from The Human Rights Campaign's blog posts. As this is an unofficial list, it is bound to grow; at the time of the construction of this project, there was no living collection or recording (available to the public) of transgender homicide rates in the US. This is not uncommon, as transgender homicides, amongst other critical public health metadata pertinent to the LGBTQ community. With data living on multiple sites, it was easier for me to construct the first one manually.

Gathering together all 2020 transgender homicides thus far into one csv, I defined a function to load in and parse this data. Once loaded in, I reformat the csv dataframe and its columns to be compatible with geospatial data. This included grouping states in the trans_homicide dataframe to create counts of cases in each state which we use to populate the choropleth map.

Next, we use and load the GeoPandas library and its preloaded spatial datasets to obtain geometry data coordinates to use in our plotting. Once loaded, I collect a GeoJSON file via url request which then provides geometry on each US state. This data set is bountiful in the way that it includes more states affiliated with the US, like Puerto Rico. From the states where homicide cases occured in 2020, we subset that collection of states and their respective geometric coordinates and sort them alphabetically.

After completing the transgender homicide dataset, another pull request is made to the Cook political website, where they provide predicted calls for the 2020 winner of each state (either Democrat or Republican). Loaded and cleaned by a function, we use the same states GeoJSON information from before and merge the election results into that data set to preserve GeoDataFrame type. To ensure clean visuals, slight adjustments to column and values were made after the merge.

Lastly, we produce choropleth visuals. Two visualization libraries were used to do so: Plotly and Matplotlib. Each came with their pros and cons: Matplotlib allowed for Puerto Rico to be plotted, while Plotly did not include it in their installed datasets; however, Plotly figures are more interactive and sophisticated than Matplotlib's.

### Results and Discussion:
The results show a majority of homicide cases occuring in the south. In the choropleth of the states and who they voted for (popular vote), we see a majority of red states. Due to Puerto Rico not being accounted for in Presidential elections, we do not see what PR votes. However, Puerto Rico in the Matplotlib choropleth contained the highest counts of Transgender homicide in 2020. If we prop both figures side by side, it is observable that there is a high concentration of homicides in the southern half of the US, which historically votes more red. 


With steps one and two completed, conducting a linear regression to make predictions on states was not completed for two reasons: there was a time constraint on building this myself, and there is also limited data points to train and test on. However, this could be reapproached if more data was collected via webscraping methods, or simply if more data was publicly available to download. 

### Conclusion:
Overall, the finding of this project revealed probable inference in relation to  the proposed hypothesis, despite any statistical finding. Major limitations to more robust findings can be attributed to the lack of publicy available biometrics/meta-data on LGBTQ folx. The goal of this project was to produce more publicly available data on Transgender homicides in the ingestible form of csv files so it could be widely replicated and improved by way of other data scientists. 

In the future, I would look to see how I could connect this to my previous research ofincorporating Twitter API to run sentiment analysis on Tweets from 'Gay Twitter'. Considering how heavily biased Machine Learning and NLP models are against queer users online, and with my newly gained skills in visually representing data, next steps in furthering Data Justice for the LGBTQ community would be to create network maps to reveal potential cases where biases in NLP models are found in publicly available data such as Tweets. Despite working solo, I am happy with my findings and being able to create geospatial mappings from scratch, and most importantly, building to improve and bring awareness to the public health disparities in the LGBTQ communities. 

