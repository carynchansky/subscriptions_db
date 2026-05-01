# Subscription Tracker

## Description
A MySQL + Python CLI app to track subscriptions, payments, and spending.

## Features
- Add, update, delete subscriptions
- Track transactions
- Filter subscriptions
- Category system

## Setup
1. Install MySQL
2. Run schema.sql
3. Run data.sql
4. pip install -r requirements.txt
5. python main.py

## Tables
- Users: stores user info
- PaymentMethods: cards
- Subscriptions: services
- Transactions: payments history
- Categories: grouping
- SubscriptionCategories: M:N relation

## Reflection
(Write 2–3 paragraphs about what you learned)