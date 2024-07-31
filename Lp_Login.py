import time
from ssl import Options
import requests
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://dev-6o0dtt0tzs4774yn.us.auth0.com/u/login?state=hKFo2SAxRjVUN3B4eldILTAtWnpON0FOSTNYRUVjRm5pYlJ3X6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHBQN09Bc0d5UFNpMm1ETExvby1aY1E3SlZRNGpsZUhIo2NpZNkgS2tHM0F2OWtKMWh4dndod2lyZERROUJVaTlIeXpRWTQ")
driver.maximize_window()
time.sleep(5)
driver.close()