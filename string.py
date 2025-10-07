CREATE TABLE IF NOT EXISTS hacker_news (
    name TEXT,
    category TEXT,
    score REAL,
    comments REAL
);

INSERT INTO hacker_news VALUES
('AI breakthrough', 'technology', 250, 120),
('Security update', 'cyber', 180, 90),
('Quantum computing', 'science', 300, 200),
('Tech layoffs', 'business', 90, 40),
('Open source milestone', 'technology', 220, 130),
('Big data trends', 'data', 270, 160);

SELECT 
    AVG(score) AS avg_score,
    MAX(score) AS max_score,
    MIN(score) AS min_score,

