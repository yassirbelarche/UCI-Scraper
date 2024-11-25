const passport = require('passport');
const { Strategy: JwtStrategy, ExtractJwt } = require('passport-jwt');
const dotenv = require('dotenv');

dotenv.config();

const options = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: process.env.JWT_SECRET
};

// passport.use(
//     new Strategy(options, (payload, done) => {
//         // Replace with DB user lookup
//         if (payload.id === 1) {
//             return done(null, { id: 1, username: 'testuser' });
//         }
//         return done(null, false);
//     })
// );

passport.use(
    new JwtStrategy(options, async (jwtPayload, done) => {
      try {
        // Mock user lookup or replace with database query
        const user = { id: jwtPayload.sub, username: jwtPayload.username };
  
        if (user) {
          return done(null, user); // Pass user to req.user
        } else {
            console.log('User not found');
          return done(null, false); // User not found
        }
      } catch (err) {
        console.error('Error in strategy:', err);
        return done(err, false);
      }
    })
  );

module.exports = passport;
