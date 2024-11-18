const express = require('express');
const router = express.Router();

// Example endpoints
router.get('/jobs', (req, res) => {
    res.json({ jobs: ['Job1', 'Job2'] });
});

router.get('/recommendations', (req, res) => {
    res.json({ recommendations: ['Rec1', 'Rec2'] });
});

module.exports = router;
