Star Wars Characters - 0x06 Star Wars API Project
This project focuses on building a Node.js script that interacts with the Star Wars API to retrieve and display character information for a specified movie.

Project Goal:

Develop a script (0-starwars_characters.js) that:

Takes a movie ID as the first command-line argument.
Uses the request module (or a suitable alternative) to make an HTTP GET request to the Star Wars API's /films/{movie_id} endpoint.
Parses the JSON response containing movie data.
Extracts the character URLs from the movie's characters array.
Iterates through each character URL and makes additional GET requests to retrieve individual character information.
Prints the names of all characters in the specified movie, one per line.

Key Concepts:

HTTP Requests in JavaScript: Learn how to make HTTP requests using the request module or fetch for asynchronous data retrieval.
Working with APIs: Gain familiarity with RESTful APIs and techniques for interaction, including JSON data parsing.
Asynchronous Programming: Master managing asynchronous operations with callbacks, promises, or async/await syntax to handle API response data effectively.
Command-Line Arguments in Node.js: Utilize the process.argv array to access arguments passed to the script from the command line.
Array Manipulation and Iteration: Practice iterating through arrays and manipulating data structures to format and display character names.
Learning Resources:
