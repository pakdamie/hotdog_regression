import pandas as pd


def clean_stadium_data(stadium_data):

    #Removing unnecessary columns such as Image, Surface, Distance to center field, Type, Roof type
    stadium_data = stadium_data.drop(['Image', 'Surface', "Distance to center field", "Type", "Roof type"], axis=1)
    
    #Remove the hyperlinks, remove the comma, and make it numeric
    stadium_data['Capacity'] = stadium_data['Capacity'].str.replace(r'\[\d+\]', '', regex=True)
    stadium_data["Capacity"] = stadium_data["Capacity"].str.replace(",", "")
    stadium_data["Capacity"] = pd.to_numeric(stadium_data["Capacity"])

    #Want to get city and state by their seperate columns 
    stadium_data[["City", "State"]] = stadium_data["Location"].str.split(", ", expand=True)

    #Then remove redundant location column
    stadium_data = stadium_data.drop(['Location'], axis = 1)

    return(stadium_data)

clean_stadium_data(a)
