#!/usr/bin/node
//  Imports a dictionary of occurrences by user id
//  and computes a dictionary of user ids by occurrence.

const dict = require('./101-data.js').dict;

const userOccurrences = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!userOccurrences[occurrences]) {
    userOccurrences[occurrences] = [];
  }

  userOccurrences[occurrences].push(userId);
}

console.log(userOccurrences);
