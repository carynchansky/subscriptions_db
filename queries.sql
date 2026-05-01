-- 1. View all subscriptions
SELECT * FROM Subscriptions;

-- 2. Subscriptions with payment method
SELECT s.name, p.card_last4
FROM Subscriptions s
JOIN PaymentMethods p ON s.payment_id = p.payment_id;

-- 3. Monthly subscriptions only
SELECT * FROM Subscriptions WHERE billing_cycle = 'Monthly';

-- 4. Total spent per subscription
SELECT subscription_id, SUM(amount)
FROM Transactions
GROUP BY subscription_id;

-- 5. Users with subscriptions
SELECT u.name, s.name
FROM Users u
JOIN PaymentMethods p ON u.user_id = p.user_id
JOIN Subscriptions s ON p.payment_id = s.payment_id;

-- 6. Subscriptions by category
SELECT s.name, c.name
FROM Subscriptions s
JOIN SubscriptionCategories sc ON s.subscription_id = sc.subscription_id
JOIN Categories c ON sc.category_id = c.category_id;

-- 7. Most expensive subscription
SELECT * FROM Subscriptions ORDER BY cost DESC LIMIT 1;

-- 8. Count subscriptions per user
SELECT u.name, COUNT(s.subscription_id)
FROM Users u
JOIN PaymentMethods p ON u.user_id = p.user_id
JOIN Subscriptions s ON p.payment_id = s.payment_id
GROUP BY u.name;