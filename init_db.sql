CREATE TABLE IF NOT EXISTS campaigns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Active', 'Paused')),
    clicks INTEGER NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    impressions INTEGER NOT NULL
);
INSERT INTO campaigns (name, status, clicks, cost, impressions) VALUES
('Summer Sale', 'Active', 150, 45.99, 1000),
('Black Friday', 'Paused', 320, 89.50, 2500),
('New Year Sale', 'Active', 200, 60.00, 1500),
('Spring Sale', 'Paused', 180, 50.00, 1200),
('Summer Clearance', 'Active', 220, 70.00, 1300),
('Fall Sale', 'Paused', 300, 80.00, 2000),
('Cyber Monday', 'Active', 400, 100.00, 3000),
('Halloween Sale', 'Paused', 250, 75.00, 1800),
('Thanksgiving Sale', 'Active', 350, 90.00, 2200),
('Winter Sale', 'Paused', 280, 65.00, 1600);  