#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) return console.error(error);

  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters(characters, index) {
  if (index >= characters.length) return;

  request(characters[index], (error, response, body) => {
    if (error) return console.error(error);

    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
