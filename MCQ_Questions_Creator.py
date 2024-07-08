from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)  # Reduced font size by 2 units
        self.cell(0, 10, 'Lab On Wheels', 0, 1, 'C')
        self.set_font('Arial', 'B', 12)  # Reduced font size by 2 units
        self.cell(0, 10, 'Basic Computer Course', 0, 1, 'C')
        self.cell(0, 10, 'MULTIPLE CHOICE QUESTIONS', 0, 1, 'C')
        self.set_font('Arial', '', 10)  # Reduced font size by 2 units
        self.cell(0, 10, 'Time Allowed: 20 minutes             Maximum Marks: 10', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, question, num):
        self.set_font('Arial', 'B', 10)  # Reduced font size by 2 units
        self.multi_cell(0, 6, f'{num}. {question}', 0, 1)
        self.ln(2)

    def chapter_body(self, options):
        self.set_font('Arial', '', 10)  # Reduced font size by 2 units
        page_width = self.w - 2 * self.l_margin  # calculate effective page width
        col_width = page_width / 2  # calculate column width
        for i in range(0, len(options), 2):
            left_option = options[i]
            right_option = options[i+1] if i+1 < len(options) else ""
            self.cell(col_width, 6, left_option, 0, 0)
            self.cell(col_width, 6, right_option, 0, 1)
        self.ln(2)

def create_mcq_pdf(mcq_list, filename):
    pdf = PDF()
    pdf.add_page()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    
    for idx, mcq in enumerate(mcq_list):
        question, options = mcq
        pdf.chapter_title(question, idx + 1)
        pdf.chapter_body(options)
    
    pdf.output(filename)

# List of MCQs (question and options)
mcq_list = [
    ("What is the Internet?", [
        "a) One computer network",
        "b) A big group of connected networks",
        "c) A kind of web browser",
        "d) A software program"
    ]),
    ("What does IP address mean?", [
        "a) Internet Protocol address",
        "b) Internet Provider address",
        "c) Internet Processor address",
        "d) Internal Protocol address"
    ]),
    ("Which one looks like an IP address?", [
        "a) 300..168.1.1",
        "b) www.google.com",
        "c) 192.168.1.1",
        "d) 2001:0db8:85a3:::8a2e:0370:7334"
    ]),
    ("Which of the following is NOT an example of a search engine?", [
        "a) Google",
        "b) Bing",
        "c) Yahoo",
        "d) None of the above"
    ]),
    ("Which technology is used to secure websites and protect data transmission over the Internet?", [
        "a) HTTPS",
        "b) FTP",
        "c) HTTP",
        "d) TCP/IP"
    ]),
    ("What do we call a network inside an organization?", [
        "a) WAN",
        "b) LAN",
        "c) MAN",
        "d) PAN"
    ]),
    ("What does ISP mean?", [
        "a) Internet Service Provider",
        "b) Internet Security Protocol",
        "c) Internet Server Provider",
        "d) Internet Search Protocol"
    ]),
    ("Which device is typically used to connect to the Internet at home?", [
        "a) Router",
        "b) Printer",
        "c) Scanner",
        "d) Ethernet cable"
    ]),
    ("What is Excel primarily used for?", [
        "a) Tracking expenses",
        "b) Creating presentations",
        "c) Analyzing data",
        "d) Editing videos"
    ]),
    ("Which security feature is typically part of LinkedIn's account verification process?", [
        "a) Uploading a profile photo",
        "b) Confirming email address",
        "c) Adding work experience",
        "d) Linking social media accounts"
    ])
]


# Create PDF
create_mcq_pdf(mcq_list, 'mcq_test.pdf')
