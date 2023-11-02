# Software Design

This file contains all the documentation to CrimeViz's CouchDB. This includes the overall database setup and the document structures for the crime and weather data.

## Table of Contents
1. **[Goal](#goal)**</br>
2. **[Database Setup](#database-setup)**</br>
3. **[Document Structures](#document-structures)**</br>
  3.1 **[Uniform Crime Data Structure](#uniform-crime-data-structure)**</br>
  3.2 **[Uniform Weather Data Structure](#uniform-weather-data-structure)**</br>

# Goal

CouchDB is a document-based NoSQL database that is used to store the crime and weather data for the different cities. Each document is stored in a JSON format which can easily be sent or retrieved via HTTP REST.

# Database Setup

The CouchDB hosts two databases, one for the crime data and one for the weather data. They are called ```crime_data``` and ```weather_data```, respectively.

# Document Structures

CouchDB documents come with their own metadata fields like for the document id and version. Therefore each data object will be placed in a field called "payload". 

## Uniform Crime Data Structure

Each document will represent one crime, with the following data. It should be noted that because multiple APIs and because these define their own data output, some fields will not be filled for some cities.

```json
{
    ...
    "payload": {
        "metaData": {
            "city": "Los Angeles",
            "reportDate": "MM/DD/YYYY",
            "occurrenceDate": "MM/DD/YYYY",
            "occurrenceTime": "13:00",
            "status": "Arrest"
        },
        "crime": {
            "type": "Battery",
            "premise": "Alley",
            "weapon": "Strong-arm"
        },
        "victim": {
            "age": 35,
            "sex": "Male",
            "ethnicity": "Unknown"
        },
        "location": {
            "area": "Downtown",
            "address": "Street name", 
            "latitude": 0.0000,
            "longitude": 0.0000
        }
    }
}
```

## Uniform Weather Data Structure

Each document will represent exactly one day, with the following data.

```json
{
    ...
    "payload": {
        "metaData": {
            "city": "Los Angeles",
            "timezone": "GMT",
            "elevation": 0.0,
            "latitude": 0.0000,
            "longitude": 0.0000,
            "date": "MM/DD/YYYY"
        },
        "hourlyData": [
            {
                "hour": "13:00",
                "temperatureActual": "0.0 °C",
                "temperatureApparent": "0.0 °C",
                "humidity": "0.0 %",
                "rainfall": "0.0 mm",
                "snowfall": "0.0 cm",
                "windSpeed": "0.0 km/h",
                "windDirection": "°"
            },
            ...
        ]
    }
}
```