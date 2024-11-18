const passport = require('passport');
const { Strategy, ExtractJwt } = require('passport-jwt');
const dotenv = require('dotenv');

dotenv.config();

const options = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: process.env.JWT_SECRET
};

passport.use(
    new Strategy(options, (payload, done) => {
        // Replace with DB user lookup
        if (payload.id === 1) {
            return done(null, { id: 1, username: 'testuser' });
        }
        return done(null, false);
    })
);

module.exports = passport;
