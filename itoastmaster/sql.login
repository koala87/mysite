BEGIN;
--
-- Create model User
--
CREATE TABLE "login_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "email" varchar(200) NOT NULL, "password" varchar(100) NOT NULL);
--
-- Create model UserInfo
--
CREATE TABLE "login_userinfo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "email" varchar(200) NOT NULL, "name" varchar(100) NOT NULL, "portrait" varchar(100) NULL, "sex" varchar(8) NULL, "status" varchar(16) NULL, "lovebridge" bool NOT NULL, "hometown" text NULL, "school" text NULL, "join_dt" date NULL, "progress" text NULL, "positions" text NULL, "interest" text NULL, "self_introduction" text NULL, "word" text NULL, "club_id" integer NULL REFERENCES "club_club" ("id"));
CREATE INDEX "login_userinfo_7115697a" ON "login_userinfo" ("club_id");

COMMIT;
