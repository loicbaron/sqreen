import os
APP_NAME = os.environ.get("APP_NAME")
if not APP_NAME:
  APP_NAME = "My Porject"

APP_DB = os.environ.get("APP_DB")
if not APP_DB:
  APP_DB = "/database.db"

environment = {
  "app": APP_NAME,
  "db": APP_DB
}