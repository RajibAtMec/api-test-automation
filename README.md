At first you have to setup the virtual env. If you have not already done so you can use the following link for guidelines
https://www.notion.so/addyinvest/Set-up-Python-Development-Environment-de0fe4fcdb224ac5b9e587e45e57ccd6 

Then use pipenv to install requests, boto3, pytest and pylint 

Then you can run positive test cases in integration with a command like following :

aws-vault exec integration -- /Users/rajib/.local/share/virtualenvs/api-test-automation-MlUn4hDE/bin/python /Users/rajib/Desktop/api-test-automation/test_pdf_validate_endpoint.py 

Replace /Users/rajib/.local/share/virtualenvs/api-test-automation-MlUn4hDE/bin/python with the location of your python interpreter in your virtual environment.
Replace /Users/rajib/Desktop/api-test-automation/test_pdf_validate_endpoint.py with location of your python script that you want to run


