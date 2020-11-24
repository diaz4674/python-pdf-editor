from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import os
import sys

AccountInfo = {
    "Type": "Business",
    "Ownership": "CCorp",
    "Benificiary": "",
    "BeneficiaryDetails": "",
    "totalSigners": 3,
    "BusinessName": "Disney",
    "DBA": "",
    "EIN": "12-2344564",
    "Street": "1313 Disneyland Dr",
    "City": "Anaheim, CA 92802",
    "AccountType1": "Business Checking",
    "AccountNumber1": "01-1005345-1"
}

signer1 = {
    "Name": 'Bobby Brown',
    "Relationship": 'Owners',
    "Street": "123 Happy Dr",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"
}

signer2 = {
    "Name": 'James Brown',
    "Relationship": 'Owners',
    "Street": "123 Happy Dr",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "(707) 778-7756",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"
}

signer3 = {
    "Name": 'Jimmy Neutron',
    "Relationship": 'Owners',
    "Street": "123 Happy Dr",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "(707) 778-7756",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"
}
signer4 = {
    "Name": 'Timmy Turner',
    "Relationship": 'Owners',
    "Street": "123 Happy Dr",
    "City": "Petaluma, CA 94952",
    "MailingAddress": "PO Box 123, Petaluma CA 94954",
    "PrimaryIDType": "Drivers License",
    "Number": "D234354 CA",
    "IssueDate1": "10/07/2017",
    "ExpirationDate1": "10/18/2022",
    "OtherID": "Credit Card",
    "OtherDesc": "Visa",
    "Expires": "02/28/2023",
    "Employer": "Poppy Bank",
    "Title": "New Accounts/CSR-Poppy Bank",
    "email": "diaz1234@gmail.com",
    "WorkPhone": "(707) 778-7756",
    "HomePhone": "(707) 778-7756",
    "Cell": "(123) 456-7890",
    "DOB": "10/18/1991",
    "SSN": "123-34-2134"

}
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/app/lib/reportlabs/fonts')
# pdfmetrics.registerFont(TTFont('Copperplate', 'Copperplate-Gothic-Bold.ttf'))


pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))


#  Font mapping
packet = io.BytesIO()
packet2 = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=(612, 792), bottomup=0)
can.setFont('Arial', 7.98)

# Account Titling Box
if AccountInfo["Type"] == "Consumer":
    can.drawString(299, 66.5, signer1["Name"])
    can.drawString(299, 76, signer2["Name"])
    # Checking if signer 3 is filled in to add to title
    if signer3:
        can.drawString(299, 86, signer3["Name"])
        if signer4 == {}:
            # Checking to see if there is another signer, to end with POD/Address
            if AccountInfo["Benificiary"] == "POD":
                can.drawString(299, 96, AccountInfo["Benificiary"])
                can.drawString(299, 106, signer1["Street"])
                can.drawString(299, 116, signer1["City"])
            else:
                can.drawString(299, 96, signer1["Street"])
                can.drawString(299, 106, signer1["City"])
    else:
        # If no signer 3, then we end the boxes
        if AccountInfo["Benificiary"] == "POD":
            can.drawString(299, 86, AccountInfo["Benificiary"])
            can.drawString(299, 96, signer1["Street"])
            can.drawString(299, 106, signer1["City"])
        else:
            can.drawString(299, 86, signer1["Street"])
            can.drawString(299, 96, signer1["City"])
    if signer4:
        can.drawString(299, 96, signer3["Name"])
        if AccountInfo["Benificiary"] == "POD":
            can.drawString(299, 106, AccountInfo["Benificiary"])
            can.drawString(299, 116, signer1["Street"])
            can.drawString(299, 126, signer1["City"])
        else:
            can.drawString(299, 106, signer1["Street"])
            can.drawString(299, 116, signer1["City"])

can.drawString(364, 41, AccountInfo["AccountNumber1"])

# Business Account Titling Box
if AccountInfo["Type"] == "Business":
    can.drawString(299, 66.5, AccountInfo["BusinessName"])
    if AccountInfo["DBA"] != "":
        can.drawString(299, 76, f'DBA {AccountInfo["DBA"]}')
        can.drawString(299, 86, AccountInfo["Street"])
        can.drawString(299, 96, AccountInfo["City"])
    else:
        can.drawString(299, 76.5, AccountInfo["Street"])
        can.drawString(299, 86, AccountInfo["City"])

#  Signer 1 Information Box
can.drawString(83.5, 159, signer1["Name"])
can.drawString(83.5, 171, signer1["Relationship"])
can.drawString(83.5, 189, f'{signer1["Street"]}, {signer1["City"]}')
can.drawString(83.5, 213, signer1["MailingAddress"])
can.drawString(83.5, 232, signer1["PrimaryIDType"])
can.drawString(188, 231, "Issued:")
can.drawString(228, 231, signer1["IssueDate1"])
can.drawString(83.5, 242, signer1["Number"])
can.drawString(188, 242, "Expires:")
can.drawString(228, 242, signer1["ExpirationDate1"])
can.drawString(83.5, 255, signer1["OtherID"])
can.drawString(83.5, 266, signer1["OtherDesc"])
can.drawString(188, 266, "Expires:")
can.drawString(228, 266, signer1["Expires"])
can.drawString(83.5, 278, f'{signer1["Employer"]}, {signer1["Title"]}')
can.drawString(83.5, 301, signer1["email"])
can.drawString(83.5, 313, signer1["WorkPhone"])
can.drawString(63, 324.5, signer1["HomePhone"])
can.drawString(202, 324.5, signer1["Cell"])
can.drawString(55, 336, signer1["DOB"])
can.drawString(188, 336, signer1["SSN"])

#  Signature Field Details
can.drawString(348, 451, signer1["Name"])
can.drawString(348, 461, signer1["SSN"])
can.drawString(476, 461, signer1["DOB"])

# Checking to see if more signers need to sign
if signer2:
    can.drawString(342, 510, signer2["Name"])
    can.drawString(342, 520, signer2["SSN"])
    can.drawString(476, 520, signer2["DOB"])

if signer3 == {}:
    can.drawString(334, 550, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
else:
    can.drawString(342, 569, signer3["Name"])
    can.drawString(342, 579, signer3["SSN"])
    can.drawString(476, 579, signer3["DOB"])

if signer4 == {}:
    can.drawString(334, 619, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
else:
    can.drawString(342, 638, signer4["Name"])
    can.drawString(342, 648, signer4["SSN"])
    can.drawString(476, 648, signer4["DOB"])

# Checking Ownership Type
if AccountInfo["Ownership"] == "Joint":
    can.drawString(17, 382.5, "X")
if AccountInfo["Ownership"] == "LLC":
    can.drawString(17, 448, "X")
if AccountInfo["Ownership"] == "CCorp":
    can.drawString(17, 459, "X")
if AccountInfo["Ownership"] == "SCorp":
    can.drawString(91.5, 459, "X")

#  Beneficiary Info
if AccountInfo["Benificiary"] == "POD":
    can.drawString(138.5, 518.5, "X")
    can.drawString(26, 576, AccountInfo["BeneficiaryDetails"])

can.save()

page2 = canvas.Canvas(packet2, pagesize=(612, 792), bottomup=0)
page2.setFont('Arial', 7.98)

#  Signer 2 Information Box
if signer2 != {}:
    page2.drawString(83.5, 35, signer2["Name"])
    page2.drawString(83.5, 46.5, signer2["Relationship"])
    page2.drawString(83.5, 64.6, f'{signer2["Street"]}, {signer2["City"]}')
    page2.drawString(83.5, 87.6, signer2["MailingAddress"])
    page2.drawString(83.5, 107, signer2["PrimaryIDType"])
    page2.drawString(188, 107, "Issued:")
    page2.drawString(228, 107, signer2["IssueDate1"])
    page2.drawString(83.5, 117, signer2["Number"])
    page2.drawString(188, 117, "Expires:")
    page2.drawString(228, 117, signer2["ExpirationDate1"])
    page2.drawString(83.5, 131, signer2["OtherID"])
    page2.drawString(83.5, 141, signer2["OtherDesc"])
    page2.drawString(188, 141, "Expires:")
    page2.drawString(228, 141, signer2["Expires"])
    page2.drawString(
        83.5, 152.5, f'{signer2["Employer"]}, {signer2["Title"]}')
    page2.drawString(83.5, 176.5, signer2["email"])
    page2.drawString(83.5, 188, signer2["WorkPhone"])
    page2.drawString(63, 200.5, signer2["HomePhone"])
    page2.drawString(202, 200.5, signer2["Cell"])
    page2.drawString(55, 212, signer2["DOB"])
    page2.drawString(188, 212, signer2["SSN"])

#  Signer 3 Information Box
if signer3 != {}:
    page2.drawString(83.5, 236, signer3["Name"])
    page2.drawString(83.5, 248, signer3["Relationship"])
    page2.drawString(83.5, 266, f'{signer3["Street"]}, {signer3["City"]}')
    page2.drawString(83.5, 290, signer3["MailingAddress"])
    page2.drawString(83.5, 307.5, signer3["PrimaryIDType"])
    page2.drawString(188, 307.5, "Issued:")
    page2.drawString(228, 307.5, signer3["IssueDate1"])
    page2.drawString(83.5, 318, signer3["Number"])
    page2.drawString(188, 318, "Expires:")
    page2.drawString(228, 318, signer3["ExpirationDate1"])
    page2.drawString(83.5, 332, signer3["OtherID"])
    page2.drawString(83.5, 342, signer3["OtherDesc"])
    page2.drawString(188, 342, "Expires:")
    page2.drawString(228, 342, signer3["Expires"])
    page2.drawString(
        83.5, 354, f'{signer3["Employer"]}, {signer3["Title"]}')
    page2.drawString(83.5, 377.5, signer3["email"])
    page2.drawString(83.5, 389.5, signer3["WorkPhone"])
    page2.drawString(63, 401.5, signer3["HomePhone"])
    page2.drawString(202, 401.5, signer3["Cell"])
    page2.drawString(55, 413, signer3["DOB"])
    page2.drawString(188, 413, signer3["SSN"])

#  Signer 4 Information Box
if signer4 != {}:
    page2.drawString(83.5, 437.5, signer4["Name"])
    page2.drawString(83.5, 449, signer4["Relationship"])
    page2.drawString(83.5, 467, f'{signer4["Street"]}, {signer4["City"]}')
    page2.drawString(83.5, 491, signer4["MailingAddress"])
    page2.drawString(83.5, 509, signer4["PrimaryIDType"])
    page2.drawString(188, 509, "Issued:")
    page2.drawString(228, 509, signer4["IssueDate1"])
    page2.drawString(83.5, 520, signer4["Number"])
    page2.drawString(188, 520, "Expires:")
    page2.drawString(228, 520, signer4["ExpirationDate1"])
    page2.drawString(83.5, 533, signer4["OtherID"])
    page2.drawString(83.5, 543, signer4["OtherDesc"])
    page2.drawString(188, 543, "Expires:")
    page2.drawString(228, 543, signer4["Expires"])
    page2.drawString(
        83.5, 555, f'{signer4["Employer"]}, {signer4["Title"]}')
    page2.drawString(83.5, 579, signer4["email"])
    page2.drawString(83.5, 590.5, signer4["WorkPhone"])
    page2.drawString(63, 602.5, signer4["HomePhone"])
    page2.drawString(202, 602.5, signer4["Cell"])
    page2.drawString(55, 614, signer4["DOB"])
    page2.drawString(188, 614, signer4["SSN"])

page2.drawString(423, 442.5, AccountInfo["EIN"])
page2.drawString(299, 227, AccountInfo["AccountType1"])
page2.drawString(393, 227, AccountInfo["AccountNumber1"])

page2.save()
# move to the beginning of the StringIO buffer
packet.seek(0)
packet2.seek(0)

new_pdf = PdfFileReader(packet)
new_pdf2 = PdfFileReader(packet2)
# read your existing PDF
existing_pdf = PdfFileReader('sigCard.pdf', "rb+")
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
page2 = existing_pdf.getPage(1)
page2.mergePage(new_pdf2.getPage(0))

output.addPage(page)
output.addPage(page2)

# finally, write "output" to a real file
outputStream = open("newSigCard.pdf", "wb")
output.write(outputStream)
outputStream.close()
