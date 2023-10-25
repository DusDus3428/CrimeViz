# Software Design

This file contains the general documentation to CrimeViz. This includes functional requirements, non-functional requirements, and architectural diagrams and descriptions.

## Table of Contents
1. **[Goal](#goal)**</br>
2. **[Rough Overview](#rough-overview)**</br>
3. **[Requirements](#requirements)**</br>
  3.1 **[Functional Requirements](#functional-requirements)**</br>
  3.2 **[Non-Functional Requirements](#non-functional-requirements)**</br>
4. **[Use Cases](#use-cases)**</br>
  4.1 **[Use Case Diagram](#use-case-diagram)**</br>
  4.2 **[Use Case Description](#use-case-description)**</br>

# Goal

CrimeViz is a a visualization application. It's purpose is to visualize crime data from different cities in the US. It consists of multiple separate projects, each written in a programming language.

# Rough Overview

![CrimeViz Rough Overview](./01_images/01_RoughOverview.png "CrimeViz Rough Overview")

The CouchDB contains all the crime data for the application.</br>
The Flask Gatherer component is a Python project based on the Flask framework. It receives requests from the Angular Frontend signalling which city's API should be targeted for data. It then sends a request to the target API to get the crime data, after which it stores said data in the CouchDB.</br>
The Restbed Backend is a C++ project based on the Restbed framework. It receives requests from the Angular Frontend to fetch the crime data from the CouchDB and send it in the response.</br>
The Angular Frontend is a TypeScript project based on the Angular framework. It interacts with the Flask Gatherer to tell it which API to target and with the Restbed Backend to retrieve the crime data. It then utilizes the D3.js library to visualize the data.</br>

Here are the documentation files to each component:

- **[CouchDB Database](./02_couchdb_database/README.md)**</br>
- **[Flask Gatherer](./03_flask_gatherer/README.md)**</br>
- **[Restbed Backend](./04_restbed_backend/README.md)**</br>
- **[Angular Frontend](./05_angular_frontend/README.md)**</br>

# Requirements

There are general functional and non-functional requirements for CrimeViz's. The project-specific requirements can be found in their individual documentation files linked above.

## Functional Requirements

| ID        	| Title                          | Description/Use Case (where possible)  														  |
| ------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CrimeViz_General_FR_1 | Fetch Crime Data 		 | Flask Gatherer should fetch crime data from open data APIs on a daily basis to guarantee up-to-date data. 	  |

## Non-Functional Requirements

| ID        	 | Title                          | Description																		   |
| -------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CrimeViz_General_NFR_1 | Containerized Projects 	  | Each project belonging to the CrimeViz application should be containerized using Docker to guarantee cross-platform portability. A docker-compose file should tie all the individual containers together.  |

## Use Case Diagram

![CrimeViz Use Case Diagram](./01_images/01_CrimeViz_UseCase.png "CrimeViz Use Case Diagram")



## Use Case Description