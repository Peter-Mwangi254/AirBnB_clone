# AirBnB Clone - The Console

![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Project Overview

Welcome to the AirBnB-clone project, the AirBnB Clone! This project focuses on creating a backend system for an AirBnB-like application, complete with a command-line interface for managing objects, data serialization, and a file-based storage system. The primary goals include building a Python package, creating a command interpreter, implementing unit testing, and mastering serialization and deserialization techniques.

## Project Structure

The project consists of the following key components:

### 1. BaseModel Class

- A base class for object management.
- Initializes instance attributes and handles data serialization and deserialization.

### 2. Serialization Flow

- Defines a serialization flow to set up data serialization and deserialization.
- Uses a file-based storage system to persistently store data in JSON format.

### 3. Storage Engine

- Implements a storage engine for efficient handling of instances.
- Utilizes a JSON file for storing and retrieving object data.

### 4. Unit Testing

- Ensures code quality through comprehensive unit testing.
- Verifies the functionality of various components and classes.

### 5. Command Interpreter

- Acts as a custom command-line tool for handling objects.
- Supports commands for creating, retrieving, updating, and deleting objects.
- Enables various operations on objects through a user-friendly interface.

## Learning Objectives

Throughout this project, you will:

- Build a Python package and create a command interpreter.
- Understand the importance of unit testing in ensuring code reliability.
- Master serialization and deserialization techniques using JSON data.
- Work with dates, UUIDs, and function arguments effectively.

## Getting Started

To set up the project on your local machine for development and testing purposes, follow these steps:

### Installation

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/Perpet98Sofia/AirBnB_clone.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd AirBnB_clone
    ```

### Usage

#### Interactive Mode

Run the console in interactive mode, allowing you to input commands directly:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Available commands and what they do

**quit or EOF**: Exits the program.
**Usage**: By itself.

**help**: Provides information on how to use a command.
**Usage**: By itself or help <command>.

**create**: Creates a new instance of a valid class, saves it to the JSON file, and prints the ID.
**Usage**: create <class name>.

**show**: Prints the string representation of an instance based on the class name and ID.
**Usage**: show <class name> <id> or <class name>.show(<id>).

**destroy**: Deletes an instance based on the class name and ID, saving the change to the JSON file.
**Usage**: destroy <class name> <id> or <class name>.destroy(<id>).

**all**: Prints all string representations of instances based on the class name.
**Usage**: By itself or all <class name> or <class name>.all().

**update**: Updates an instance based on the class name and ID by adding or updating attributes, saving the changes to the JSON file.
**Usage**: update <class name> <id> <attribute name> "<attribute value>" or <class name>.update(<id>, <attribute name>, <attribute value>) or <class name>.update(<id>, <dictionary representation>).

**count**: Retrieves the number of instances of a class.
**Usage**: <class name>.count().

## Authors

Perpetua Akwiri Otieno | Email: [perpetualakwiri](mailto:perpetualakwiri@gmail.com)

Peter Brian Mwangi | Email: [wahomebrian](mailto:wahomebrian98@gmail.com)