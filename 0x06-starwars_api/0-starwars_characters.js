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
        let data = JSON.parse(body);
        let listOfCharacters = data.characters;
        resolve(listOfCharacters);
      }
    });
  });
}

async function characterNames(listOfCharacters) {
  for (char of listOfCharacters) {
    let name = await new Promise((resolve, reject) => {
      request(char, (err, message, body) => {
        if (err) reject(err);
        else {
          let charData = JSON.parse(body);
          let charName = charData.name;
          resolve(charName);
        }
      });
    });
    console.log(name);
  }
}

listOfCharacters(filmId)
  .then((characters) => {
    characterNames(characters);
  })
  .catch((error) => {
    console.error(error);
  });
