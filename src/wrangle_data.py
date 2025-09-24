import pandas as pd
from datetime import datetime


def clean_stadium_data(stadium_data):

    """
    Wrangles the stadium_data that was scraped from wikipedia

    Returns:
        pd.DataFrame: A DataFrame containing the Stadium name, capacity, team that it hosts, when it opened,
        the age, the city, and the state
    """

    #Removing unnecessary columns such as Image, Surface, Distance to center field, Type, Roof type
    stadium_data = stadium_data.drop(['Image', 'Surface', 'Distance to center field', 'Type', 'Roof type'], axis=1)
    
    #Remove the hyperlinks, remove the comma, and make it numeric - Capacity
    stadium_data['Capacity'] = stadium_data['Capacity'].str.replace(r'\[\d+\]', '', regex=True)
    stadium_data['Capacity'] = stadium_data['Capacity'].str.replace(',', '')
    stadium_data['Capacity'] = pd.to_numeric(stadium_data['Capacity'])

    #Remove the hyperlinks and make it numeric - Year it opened
    stadium_data['Opened'] = stadium_data['Opened'].str.replace(r'\[.*?\]', '', regex=True)
    stadium_data['Opened'] = pd.to_numeric(stadium_data['Opened'])

    #Age of stadium is dependent on the current year subtracted by when it was opened
    current_year = datetime.now().year
    stadium_data['Age'] = current_year - stadium_data['Opened'] 
    
    #Team name
    stadium_data['Team'] = stadium_data['Team'].str.replace(r'\[.*?\]', '', regex=True)

    #Want to get city and state by their seperate columns 
    stadium_data[['City', 'State']] = stadium_data['Location'].str.split(', ', expand=True)

    #Then remove redundant location column
    stadium_data = stadium_data.drop(['Location'], axis = 1)


    return(stadium_data)

