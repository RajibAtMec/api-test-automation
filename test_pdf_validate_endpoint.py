""" Tests the pdf-validate endpoint using different states of the Loan Agreement.
    TC stands for Test Case
"""
import requests
import get_header

# Endpoint for Integration Environment
URL = "https://utilities.addyinvest-integration.com/pdf-validate"
# Endpoint for Staging Environment
#URL = "https://utilities.addyinvest-staging.com/pdf-validate"
# Endpoint for Production Environment
#URL = "https://utilities.addyinvest.com/pdf-validate"

## TC-1: Passing the pdf with just first signature to the endpoint using jwt for step1
payload={}
files=[
  ('file',('LoanAgreementWithJustFirstSignature.pdf', open('./files/LoanAgreementWithJustFirstSignature.pdf','rb'),'application/pdf'))
]

# Call the endpoint for step 1
resp = requests.request("POST", URL, headers=get_header.get_header(1), data=payload, files=files)

assert resp.status_code == 200
assert resp.text == '{}'
print(resp.status_code)

## TC-2: Passing the pdf with all the signatures to the endpoint using jwt for step2. TODO
