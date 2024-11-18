const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config();

const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Routes
app.get('/', (req, res) => {
    res.send('API is running...');
});

// Start the server36
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

// Integrate Authentication Middleware
const passport = require('./config/passport');
app.use(passport.initialize());
app.get('/api/protected', passport.authenticate('jwt', { session: false }), (req, res) => {
    res.json({ message: 'This is a protected route', user: req.user });
});

// Add login route to Generate JWTs for Users

const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

app.post('/api/login', async (req, res) => {
    const { username, password } = req.body;

    // Example user (replace with DB lookup)
    const user = { id: 1, username: 'testuser', password: '$2b$10$abc123' };

    const match = await bcrypt.compare(password, user.password);
    if (!match) return res.status(401).json({ message: 'Invalid credentials' });

    const token = jwt.sign({ id: user.id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token });
});

// Import the routes of Public REST API
const publicRoutes = require('./routes/public');
app.use('/api', publicRoutes);

// Import the route of Internal API for Python Integration
const internalRoutes = require('./routes/internal');
app.use('/internal', internalRoutes);
