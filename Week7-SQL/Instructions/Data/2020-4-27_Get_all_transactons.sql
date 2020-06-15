SELECT ch.name, t.time, t.amount
FROM cc_transaction t
JOIN credit_card cc
	ON t.cc = cc.number
JOIN card_holder ch
	ON cc.card_holder_id = ch.id
WHERE ch.id = 2
AND EXTRACT (HOUR FROM t.time) BETWEEN 7 AND 9;