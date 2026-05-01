INSERT INTO Users (name, email) VALUES
('David', 'david@email.com'),
('John', 'john@email.com');

INSERT INTO PaymentMethods (user_id, card_last4, card_type) VALUES
(1, '1234', 'Visa'),
(1, '5678', 'MasterCard');

INSERT INTO Subscriptions (payment_id, name, cost, billing_cycle) VALUES
(1, 'Netflix', 15.99, 'Monthly'),
(1, 'Spotify', 9.99, 'Monthly'),
(2, 'Amazon Prime', 139.00, 'Yearly');

INSERT INTO Transactions (subscription_id, amount, transaction_date) VALUES
(1, 15.99, '2025-01-01'),
(1, 15.99, '2025-02-01'),
(2, 9.99, '2025-01-01'),
(3, 139.00, '2025-01-01');

INSERT INTO Categories (name) VALUES
('Entertainment'),
('Music'),
('Shopping');

INSERT INTO SubscriptionCategories VALUES
(1,1),
(2,2),
(3,3);