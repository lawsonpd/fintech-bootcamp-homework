DROP TABLE IF EXISTS 
	"card_holder",
	"credit_card",
	"merchant_category",
	"merchant",
	"cc_transaction";

CREATE TABLE "card_holder" (
  "id" int,
  "name" VARCHAR(100),
  PRIMARY KEY ("id")
);

CREATE TABLE "merchant_category" (
  "id" int,
  "name" VARCHAR(50),
  PRIMARY KEY ("id")
);

CREATE TABLE "merchant" (
  "id" int,
  "name" VARCHAR(100),
  "category_id" int,
  PRIMARY KEY ("id"),
  FOREIGN KEY ("category_id") REFERENCES "merchant_category" ("id")
);

CREATE TABLE "credit_card" (
  "number" VARCHAR(20),
  "card_holder_id" int,
  PRIMARY KEY ("number"),
  FOREIGN KEY ("card_holder_id") REFERENCES "card_holder" ("id")
);

CREATE TABLE "cc_transaction" (
  "id" int,
  "time" timestamp,
  "amount" float,
  "cc" VARCHAR(20),
  "merchant_id" int,
  PRIMARY KEY ("id"),
  FOREIGN KEY ("cc") REFERENCES "credit_card" ("number")
);

