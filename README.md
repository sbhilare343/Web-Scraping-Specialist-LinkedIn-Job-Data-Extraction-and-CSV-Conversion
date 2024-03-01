# Web-Scraping-Specialist-LinkedIn-Job-Data-Extraction-and-CSV-Conversion
# main.py
  This code is a simple GUI application built with Tkinter in Python for job scraping from LinkedIn and sending scraped job data via email. It imports two modules: `jobscrape` for scraping job data and `sendMail` for sending emails. 
  
  The GUI consists of:
  - Two entry fields for user to input their name and email address.
  - Three additional entry fields for job search keywords.
  - Two buttons: "Search" for initiating the job search and "Send Mail" for sending the scraped job data via email.
  - A canvas displaying an image (assumed to be the company logo or related image).
  
  When the user enters their details and job search keywords, they can click the "Search" button to initiate the job search process, which involves scraping job data from LinkedIn based on the entered keywords. Once the search is complete, the user can click the "Send Mail" button to send the scraped job data via email to the provided email address.
  
  Note: The `time.sleep(3)` calls after creating each entry field seem unnecessary and may cause the GUI to freeze for 3 seconds after launching. These lines should be removed or relocated as needed.

# jobscrape.py
  This Python code defines a class named `BackendWork` that performs web scraping of job listings from LinkedIn. Here's a breakdown of its functionality:
  
  1. **Initialization**: 
      - It initializes the `PATH` variable with the path to the ChromeDriver executable, `LINK` with the LinkedIn login page URL, `USERID` with the user's LinkedIn username, and `PASSWORD` with the user's LinkedIn password.
      - It initializes variables `t1`, `t2`, and `t3` to store job search keywords.
  
  2. **Login Method**: 
      - It initiates a Selenium webdriver session using ChromeDriver.
      - It navigates to the LinkedIn login page.
      - It fills in the username and password fields and submits the login form.
      - After successful login, it calls the `perform_search` method.
  
  3. **Perform Search Method**: 
      - It scrapes job listings from LinkedIn based on the provided keywords (`t1`, `t2`, `t3`).
      - It initializes an empty Pandas DataFrame `df` to store job data.
      - It sets the initial page number and counter for pagination.
      - It loops through the specified number of pages (`n`) to scrape job data.
      - For each page:
          - It scrapes job titles, company names, and job links using BeautifulSoup from the current page's HTML source.
          - It appends the scraped data to the DataFrame.
          - It updates the URL to navigate to the next page of job listings.
      - Finally, it exports the DataFrame to a CSV file named "Jobs.csv" and prints the DataFrame.
  
  Note: 
  - The `chromedriver path`, `userid`, and `password` need to be filled with actual values.
  - The code uses implicit waits (`implicitly_wait`) to wait for elements to be present in the DOM before interacting with them.
  - The time delays (`time.sleep`) ensure that the page loads properly before scraping data.
  - The number of pages to scrape (`n`) and other parameters can be adjusted as needed.

# sendMail.py
  This Python code defines a `Mail` class responsible for sending emails with job listings CSV file attached. Here's a breakdown of its functionality:
  
  1. **Initialization**: 
      - It initializes `receiver_email` and `name` attributes, which will be filled with the recipient's email address and name respectively.
  
  2. **send_mail Method**: 
      - It constructs the email body in HTML format, personalized with the recipient's name.
      - It sets the email subject to "Job List CSV".
      - It attaches the job listings CSV file to the email.
      - It establishes a connection to the SMTP server (`smtp.gmail.com`) on port 587 using `smtplib.SMTP`.
      - It starts TLS encryption for secure communication using `server.starttls`.
      - It logs in to the sender's email account using the provided credentials.
      - It sends the email using `server.sendmail`.
  
  Note: 
  - The sender's email address and password need to be filled with actual values.
  - The file path for the CSV attachment should be accurate.
  - The HTML email body can be customized further as needed.
  - Ensure that less secure apps access is enabled in the sender's Gmail settings if Gmail is being used. Alternatively, you can use app passwords or two-factor authentication for secure access.
