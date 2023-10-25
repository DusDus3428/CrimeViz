# Software Design

This file contains all the documentation to CrimeViz's Flask Gatherer project. This includes functional requirements, non-functional requirements, and architectural diagrams and descriptions.

## Table of Contents
1. **[Goal](#goal)**</br>
2. **[Requirements](#requirements)**</br>
  2.1 **[Functional Requirements](#functional-requirements)**</br>
  2.2 **[Non-Functional Requirements](#non-functional-requirements)**</br>
3. **[Sequence Diagrams](#sequence-diagrams)**</br>
4. **[Activity Diagrams](#activity-diagrams)**</br>

# Goal

The Flask Gatherer component is a Python project based on the Flask framework. It receives requests from the Angular Frontend signalling which city's API should be targeted for data. It then sends a request to the target API to get the crime data, after which it stores said data in the CouchDB. 

# Requirements

## Functional Requirements

| ID        	| Title                          | Description/Use Case (where possible)  														  |
| ------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CrimeViz_FlaskGatherer_FR_1 | Fetch Crime Data 		 | Flask Gatherer should fetch crime data from open data APIs on a daily basis to guarantee up-to-date data. 	  |
| CrimeViz_FlaskGatherer_FR_2 | Set Target API Upon Request 		 | Flask Gatherer should be able to change the target API for the crime data upon request from Angular Frontend. 	  |
| CrimeViz_FlaskGatherer_FR_3 | Store Crime Data 		 | Flask Gatherer should store the fetched crime data in a CouchDB database. 	  |
| CrimeViz_FlaskGatherer_FR_4 | Store Crime Data In Uniform Format 	  | The crime data retrieved from different APIs should be stored in a uniform JSON format to ensure. Identical handling of all crime data in Angular Frontend |

## Non-Functional Requirements

| ID        	 | Title                          | Description																		   |
| -------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CrimeViz_FlaskGatherer_NFR_1 | Retry Failed REST Requests 	  | If the data retrieval requests specified in CrimeViz_FlaskGatherer_FR_1 return with a code that warrants a retry, they should be retried three more times in intervals of three seconds.  |