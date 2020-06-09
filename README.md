# HackerRank Sparse Arrays solver (Test MdM)
> This  project solves the sparse arrays problem presented by HackerRank ([link](https://www.hackerrank.com/challenges/sparse-arrays/problem)) 

This python program finds the occurrences of a user specified string queries into a predifined list of strings.

You can either run this app locally or run it on a docker container (see the installation and how to use procedures below).

## Installation
The project requires a python 3.x interpreter.
First clone the repo.
```sh
git clone https://github.com/loicbausor/sparse_arrays_solver.git
```


## How to use this app locally

First you need to specify an environement variable with strings list you want to investigate. The name of this variable should be `SPARSE_ARRAY_STRINGS` and the format of this one has to be a quoted list. For example we may define (in a linux shell):

```sh
export SPARSE_ARRAY_STRINGS='["my","strings","abc","acb"]'
```
Then run the main.py in the app folder, specifying the queries you want to count. For example :
```sh
python3 -m main  query1,query2,query3
```
The program will retrun a dictionnary with, as key the query and as value the number of occurrences of this query. For example : 
```sh
{'query1' : 3,
'query2': 6,
'query3' : 0}
```
## How to use this app on Docker

At the location of the repo, you can build the docker image like this.

```sh
docker build . -t name_of_image
```
The Dockerfile will run the app installation. You can change the ENV variable directly into it to specify the strings of your choice (change the buildtime_variable value). 
You can then run the container using this command (you can change the ports arguments if needed and add some arguments).

```sh 
docker run -t name_of_image qurey1,query2,query3
```
The container will return the dictionnary.


## Repo composition
This project is composed of several files :

#### 1) The sparse_arrays.py module (in the app folder)
This module contains the class `QueryBuilder`. This class groups a query list and a strings list to do the occurrences research.
**Arguments :**
1. `query` : A list (or tuple) containing all the string queries specified by the user. Those queries have to respect the constraintsof the Sparse Arrays problem (specified on the paragraph below)
2. `strings` : A list (or tuple) containing all the strings the user wants to search into. Those strings have also to respect the constraints of the Sparse Arrays problem (specified on the paragraph below)

The class constructor will raise a **ValueError** or a **TypeError** if the constraints are not respected. 

**Methods :**
- `QueryBuilder.search()`
Searches the occurrences of strings of `query` into the `strings` list. It returns a dictionnary mapping the string queries with their occurrences in the list.

#### 2) The main.py module (in the app folder)
This module collects the different variables (arguments and environement) variable and constructs a QueryBuilder to print the query result (a dictionnary mapping strings queries and their occurrences in the list).

#### 3) The requirements.txt file
It groups all the package requirements for this project. 


## Sparse Arrays constraints

The arguments given to the program  have to respect the following constraints.


![](constraints.PNG)

Where n is the  length and q the strings length.
The two variable have to be lists or tuples  

## Meta

Loïc Bausor –– loic.bausor@gmail.com
