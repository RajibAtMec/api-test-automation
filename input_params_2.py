""" Payload for 2nd JWT of Loan Agreement """

input_params_2 = {
       "payload": {
            "current_signer": 2,
            "model_id": "2",
            "model_type": "property",
            "document_name": "Loan Agreement",
            "template_bucket": "addyinvest-integration-pdf-form-filler-destination",
            "template_key_to_delete": "RajibMarch16 - Loan Agreement.pdf",
            "signers": [
                {
                "signature_field": "addy_Sjagger347_Sign_Authorized_Signatory_1",
                "signer_id": 1
                },
                {
                "signature_field": "addy_Mike_Sign_Authorized_Signatory_2",
                "signer_id": 2
                }
            ],
            "pdf_file_url": "https://addyinvest-integration-pdf-form-filler-destination.s3.amazonaws.com/RajibMarch16%20-%20Loan%20Agreement.pdf?AWSAccessKeyId=ASIAXO72UA432BZXWN5F&Signature=R798vHP4VyO%2FA7OjYvIRF7BPug8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHMzPu0WuPtT1%2FjChfOCON5gdsxDBkU3dPxvQhNwy3%2FmAiBzz04d%2FUsUG6z0Sbv8952Kpb3de5BUcc3a6o%2BfPS3d0yrQAQgcEAAaDDUxMzIzNzMyMTUyNyIMgFF8dz%2BqZyvnWFo9Kq0BopCjrnWStXNGRTMMrpJLy2TLazBnh%2FgoS2QjCXCzxFdgJ6jkZioLUi2wpLiXZpKnHeJDk0WYdIRmIarGIEdvnaCtT0S7rV5QA4abdOfSk%2Fz0%2B5MAjiUUr0ELmN4J%2F7zfZzT5l49JyZ1DqIvunuc7QRa%2BB9Y4IkN1dn%2BKe9LWsM0Kpm%2FunZPAWYYUr1M%2BMcyTLefG6qv%2BeOy7t6tmkKnDlXxtv4wQWq07KY9o4d0wpvLDggY64QEpFM1rkvnhTqBI1XyFCFzgalJAMSD3LuySVow8aI5ZP5ytoC3twTMwrs0mJnU1qqjX7gLvGl3zFC7JiT5cWjccpnzIW7VJHxwzqC4nAPgYXSyU4gXgkkRSdpvfcqCvQVFkSGZh8r4l3%2ByLvweCU86n97ZrTqUXfeuSC9LSnTB35WgU7Vk9Np%2BJO0ZYN79NzVCfGEgT3KtyS57jJcdQKbcq0ikm97dN9VBvxU6pvLM9ItBQISs%2FwkBmI6oJy6WMNnC35BfAk%2FkIvx5fw8ljJk0n9Llw0Typ61bwy8%2B6UvHznGs%3D&Expires=1616005821",
            "document_type": "Loan Agreement"
            },
       "issuer": "addy",
       "audience": "pdf_annotate"
}
