#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

// get the film id (arg)
if (isNaN(filmId) || !filmId) {
  console.error('please enter a number');
  process.exit(1);
}

function listOfCharacters(filmId) {
  return new Promise((resolve, reject) => {
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
    request(apiUrl, (error, message, body) => {
      if (error) reject(error);
      else {
        resolve(JSON.parse(body).characters);
      }
    });
  });
}

async function characterNames(listOfCharacters) {
  for (const char of listOfCharacters) {
    const name = await new Promise((resolve, reject) => {
      request(char, (err, message, body) => {
        if (err) reject(err);
        else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    console.log(name);
  }
}

listOfCharacters(filmId)
  .then((charactersList) => {
    characterNames(charactersList);
  })
  .catch((error) => {
    console.error(error);
  });
