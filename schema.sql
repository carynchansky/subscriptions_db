CREATE DATABASE subscription_tracker;
USE subscription_tracker;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE PaymentMethods (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    card_last4 CHAR(4) NOT NULL,
    card_type VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_id INT,
    name VARCHAR(100) NOT NULL,
    cost DECIMAL(6,2) NOT NULL CHECK (cost >= 0),
    billing_cycle ENUM('Monthly', 'Yearly') DEFAULT 'Monthly',
    FOREIGN KEY (payment_id) REFERENCES PaymentMethods(payment_id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    subscription_id INT,
    amount DECIMAL(6,2),
    transaction_date DATE,
    FOREIGN KEY (subscription_id) REFERENCES Subscriptions(subscription_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

-- M:N Junction Table
CREATE TABLE SubscriptionCategories (
    subscription_id INT,
    category_id INT,
    PRIMARY KEY (subscription_id, category_id),
    FOREIGN KEY (subscription_id) REFERENCES Subscriptions(subscription_id)
        ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
        ON DELETE CASCADE
);