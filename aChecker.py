#Program to run site tests on AChecker

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def check(site):
	details={"Sites":site,"Tested":"N","Known":"-","Likely":"-","Potential":"-"}
	aChecker = 'https://achecker.ca/checker/index.php'

	# Instance of a Chrome tab
	driver = webdriver.Chrome()
	# Navigate to AChecker
	driver.get(aChecker)
	# Toggle Options
	try:
		driver.find_element_by_xpath('//*[@id="center-content"]/table/tbody/tr/td/div/form/div/fieldset/div[5]/h2/a').click()
		sleep(1)
		# Select AAA Level
		driver.find_element_by_id('radio_gid_9').click()

		addressBar=driver.find_element_by_id('checkuri')
		addressBar.clear()
		addressBar.send_keys(site)
		addressBar.send_keys(Keys.RETURN)
		sleep(0.5)
		WebDriverWait(driver,120).until(EC.invisibility_of_element_located((By.ID, "AC_spinner_by_uri")))
		sleep(1)
		details['Known']=driver.find_element_by_id('AC_num_of_errors').text
		details['Likely']=driver.find_element_by_id('AC_num_of_likely').text
		details['Potential']=driver.find_element_by_id('AC_num_of_potential').text
		details['Tested']='Y'
		print("Known: ", details['Known'])
		print("Likely: ", details['Likely'])
		print("Potential: ", details['Potential'])

	except:
		print("Timeout")
		details['Known']=details['Likely']=details['Potential']='-'
		details['Tested']='T'

	finally:
		print(details)
		print("-----------------")
		driver.close()
		return(details)
