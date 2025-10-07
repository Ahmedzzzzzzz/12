CREATE TABLE hacker_news (
    id INT,
    title VARCHAR(100),
    author VARCHAR(50),
    score INT,
    comments INT
);

INSERT INTO hacker_news VALUES
(1, 'AI breakthrough in robotics', 'karan', 250, 120),
(2, 'New security update released', 'john', 180, 95),
(3, 'Quantum computing progress', 'rita', 300, 200),
(4, 'Tech layoffs continue', 'alex', 90, 40),
(5, 'Open source project hits milestone', 'karan', 220, 150),
(6, 'Big data trends in 2025', 'sara', 270, 180);

SELECT 
    AVG(score) AS avg_score,
    MAX(score) AS top_score,
    MIN(score) AS lowest_score,
    COUNT(*) AS total_news
FROM hacker_news
WHERE score > 150;
