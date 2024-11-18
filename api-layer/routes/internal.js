const express = require('express');
const axios = require('axios');
const router = express.Router();

router.post('/recommendations', async (req, res) => {
    try {
        const response = await axios.post('http://localhost:8000/recommend', req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Error fetching recommendations' });
    }
});

module.exports = router;
