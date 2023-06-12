import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from gologin import getRandomPort


gl = GoLogin({
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NDgzZjYzYjhhZDg2YjY5NzJjZmU1OGQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NDg3Mzc5MGI5NTQxOTczYzIzNGNhZTkifQ.F4Or5FgSUnd8OvuNa9CX-ATk3rCt9VXt3ltX1A86G4E",
	"profile_id": "64873933da5f125a0815a154"
	})

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("https://youtube.com/")
