""" Tests Negative cases for the pdf-validate endpoint.
    TC stands for Test Case.
 """
import requests
import get_header

# Endpoint for Integration Environment
URL = "https://utilities.addyinvest-integration.com/pdf-validate"
# Endpoint for Staging Environment
#URL = "https://utilities.addyinvest-staging.com/pdf-validate"
# Endpoint for Production Environment
#URL = "https://utilities.addyinvest.com/pdf-validate"


## TC-1: Using the jwt_1 passing a text file to test to the endpoint
payload={}
files=[
  ('file',('test.txt', open('./files/test.txt','rb'),'application/txt'))
]

resp = requests.request("POST", URL, headers=get_header.get_header(1), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "Unsupported file included"}'
print(resp.text)

## TC-2: Using the jwt_2 passing a doc file to test to the endpoint
payload={}
files=[
  ('file',('test.doc', open('./files/test.doc','rb'),'application/txt'))
]

resp = requests.request("POST", URL, headers=get_header.get_header(2), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "Unsupported file included"}'
print(resp.text)

## TC-3: Using the jwt_2 passing a completely signed file to test to the endpoint
payload={}
files=[
  ('file',('LoanAgreementWithAllSignatures.pdf', open('./files/LoanAgreementWithAllSignatures.pdf','rb'),'application/pdf'))
]

resp = requests.request("POST", URL, headers=get_header.get_header(2), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "PDF already has been signed by the authority"}'
print(resp.text)


## TC-4: Passing the pdf with just first signature to the endpoint using jwt for step2
payload={}
files=[
  ('file',('LoanAgreementWithJustFirstSignature.pdf', open('./files/LoanAgreementWithJustFirstSignature.pdf','rb'),'application/pdf'))
]

# Calling the endpoint for step 2
resp = requests.request("POST", URL, headers=get_header.get_header(2), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "Please sign the field"}'
print(resp.text)


## TC-5: Passing a completely signed pdf using JWT of step1
payload={}
files=[
  ('file',('LoanAgreementWithAllSignatures.pdf', open('./files/LoanAgreementWithAllSignatures.pdf','rb'),'application/pdf'))
]

# Calling the endpoint for step 1
resp = requests.request("POST", URL, headers=get_header.get_header(1), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "Please do not sign in other signer\'s place"}'
print(resp.text)


## TC-6: Passing the pdf with no signature to the endpoint using jwt for step1
payload={}
files=[
  ('file',('LoanAgreementWithoutAnySignature.pdf', open('./files/LoanAgreementWithoutAnySignature.pdf','rb'),'application/pdf'))
]

# Call the endpoint for step 1
resp = requests.request("POST", URL, headers=get_header.get_header(1), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "Please sign the field"}'
print(resp.text)


## TC-7: Passing the pdf with just 2nd signature deleting the 1st signature for step2
payload={}
files=[
  ('file',('LoanAgreementWithJust2ndSignature.pdf', open('./files/LoanAgreementWithJust2ndSignature.pdf','rb'),'application/pdf'))
]

# Call the endpoint for step 2
resp = requests.request("POST", URL, headers=get_header.get_header(2), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "Please do not delete the other signer\'s place"}'
print(resp.text)

## TC-8: Passing the pdf with no signature to the endpoint using jwt for step2
payload={}
files=[
  ('file',('LoanAgreementWithoutAnySignature.pdf', open('./files/LoanAgreementWithoutAnySignature.pdf','rb'),'application/pdf'))
]

# Call the endpoint for step 2
resp = requests.request("POST", URL, headers=get_header.get_header(2), data=payload, files=files)

assert resp.status_code == 400
assert resp.text == '{"message": "Please do not delete the other signer\'s place"}'
print(resp.text)
.DS_Store
.vscode/
__pycache__
