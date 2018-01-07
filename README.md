# Sqlalchemy Analysis - Climate Analysis and Flask API


The following outlines are completed:

## Data Engineering

The climate data for Hawaii is provided through two CSV files. Python and Pandas are used to inspect the content of these files and clean the data.

* Created a Jupyter Notebook file called `data_engineering.ipynb` and use this to complete all of the Data Engineering tasks.

* Used Pandas to read in the measurement and station CSV files as DataFrames.

* Inspected the data for NaNs and missing values. 

* Saved the cleaned CSV files with the prefix `clean_`.


##  Database Engineering

Used SQLAlchemy to model the table schemas and create a sqlite database for the tables. One table for easurements and one for stations.

* Created a Jupyter Notebook called `database_engineering.ipynb` and used this to complete all of the Database Engineering work.

* Used Pandas to red the cleaned measurements and stations CSV data. 

* Used the `engine` and connection string to be created a database called `hawaii.sqlite`.

* Used `declarative_base` and created ORM classes for each table.

  * A class for `Measurement` and for `Station`.

  * Defined the primary keys.

* Once ORM classes defined, created the tables in the database using `create_all`.



##  Climate Analysis and Exploration

Used Python and SQLAlchemy to do basic climate analysis and data exploration on the new weather station tables. All of the following analysis done by using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Created a Jupyter Notebook file called `climate_analysis.ipynb` and use it to complete the climate analysis and data exporation.

* Choose a start date and end date for a trip. Made sure that the vacation range is approximately 3-15 days total.

* Used SQLAlchemy `create_engine` to connect to the sqlite database.

* Used SQLAlchemy `automap_base()` to reflect the tables into classes and saved a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Ploted the results using the DataFrame `plot` method.

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * Listed the stations and observation counts in descending order

  * Highest number of observations found.

* Designed a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filtered by the station with the highest number of observations.

  * Ploted the results as a histogram with `bins=12`.



### Temperature Analysis

* Wrote a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d` and return the minimum, average, and maximum temperatures for that range of dates.

* Used the `calc_temps` function to calculate the min, avg, and max temperatures for the trip using the matching dates from the previous year (i.e. use "2017-01-01" if the trip start date was "2018-01-01")

* Ploted the min, avg, and max temperature from the previous query as a bar chart.

  * Used the average temperature as the bar height.

  * Used the peak-to-peak (tmax-tmin) value as the y error bar (yerr).


##  Climate App

Designed a Flask API based on the queries that were developed. 

* Used FLASK to create the routes.

### Routes

* `/api/v1.0/precipitation`

  * Queried for the dates and temperature observations from the last year.

  * Converted the query results to a Dictionary using `date` as the key and `tobs` as the value.

  * Returned the json representation of the dictionary.

* `/api/v1.0/stations`

  * Returned a json list of stations from the dataset.

* `/api/v1.0/tobs`

  * Returned a json list of Temperature Observations (tobs) for the previous year

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returned a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculated `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculated the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

