const bcrypt = require('bcrypt');
const saltRounds = 10;
const password = 'password123';

bcrypt.hash(password, saltRounds, (err, hash) => {
  if (err) throw err;
  console.log('Hashed password:', hash);  // Copy the result
});
