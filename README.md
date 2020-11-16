# classifying-job-links

<b>Motivation:</b> <br>
<br>
I want to scrape job postings from any given website with a generic algorithm, so I will be able to monitor new job openings directly from the source, i.e. employeers websites.
Since every website will have a different HTML "style" and job titles varies a lot, I decided to build a ML model to classify the scraped links that are job postings.<br>
<br>
<b>Files:</b><br>
<br>
<b>Input:</b><br>
<br>
'inputCompanies - js rendered.csv' -> list of companies and URLs to scrape.<br>
<br>
<b>Scraping:</b><br>
<br>
1 - 'html_scrape.py' -> scrapes HTML rendered websites (requests, beautifulsoup, pandas, numpy).<br>
2 - 'js_scrape.py' -> scrapes JavaScript rendered websites (selenium, beautifulsoup, pandas, numpy).<br>
3 - 'FJGH EDA.ipynb' -> Data cleaning, Exploratory Data Analysis and Feature Engineering (seaborn, sklearb, pandas, numpy, matpyplot).<br>
4 - 'ML_Link_Classifier .ipynb' -> Machine learning model. (sklearn, pandas, numpy)<br>
<br>
<b>Connection between files:</b><br>
<br>
All those files are "conected" by their output, i.e. the out put of 1 and 2 will be the input for 3, and the output of 3 will be the input for 4.<br>
<br>
<b>Next steps</b><br>
<br>
Get more data:<br>
- Create a generic as possible function to iterate pages of JS rendered websites.<br>
<br>
Tolkenize:<br>
- Adjust the model to use the tolkenized dataset as input<br>
<br>
<b>Acknowledgements:</b>
Pedro Monteiro for helping me with statistical concepts and ideas to improve the model. (https://www.linkedin.com/in/pedro-monteiro-05206722/) <br>
Lorena Cunha for helping me reviewing my work. (https://www.linkedin.com/in/lorenapcunha/) <br>
Ken Jee for your free content that helped me structure this project. (https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg) <br>
Tim for your tutorials on Selenium. (https://www.youtube.com/c/TechWithTim) <br>
All the community. I would not pull this out without the infit detailed explanations on stackoverflow and other sources. 
