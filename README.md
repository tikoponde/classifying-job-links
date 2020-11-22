# classifying-job-links

<h1>Data Science Job Link Classifier: Project Overview</h1><br>
<ul>
  <li>Created a tool that classifys scrapped website links into Job Postings (96% accurracy) to enable a bot scrape job postings from any give website.</li>
  <li>Scraped over 6000 job postings from the website of 30 employers in Canada.</li>
  <li>Engineered features using the information present in the 'a' element tag, such as keys, attributes and text.</li>
  <li>Optimized Random Forest, Logistic Regression, K-Nearest Neighbors and SVM using GridsearchCV.</li>
  <li>Built a Stack model.</li>
 </ul>

<h2>Code and Resources Used</h2><br>
<b>Python Version: </b>3.8<br>
<b>Packages: </b>pandas, numpy, sklearn, requests, re, matplotlib, seaborn, selenium, beautifulsoup, pickle, datetime, time<br>
<b>Stacking walk-through: </b> <a href:"https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/">https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/</a><br>
<b>Documentation: </b> <a href:"https://github.com/PlayingNumbers/ds_salary_proj">https://github.com/PlayingNumbers/ds_salary_proj</a><br>

<h2>Web Scraping</h2><br>.
Built two web scrapers, one using requests and another one using selenium (to scrape js rendered websites). From each /careers website all 'a' tag elements were scraped.<br>
<ul>
  <li>Scraped the entire 'a' element tag.</li>
  <li>Scraped all keys from each 'a' element tag.</li>
  <li>Scraped all attributes from each 'a' element tag.</li>
  <li>Scraped the text from each 'a' element tag</li>
 </ul>

<h2>Data Cleaning and Feature Engineering</h2><br>
<ul>
  <li>Handled rows with null values.</li>
  <li>Made columns for length of text and href and grouped them.</li>
  <li>Made columns for the number of keys.</li>
  <li>Made columns for rows that contained job keywords on keys and attributes.</li>
  <li>Normalized feature values, when necessary, using QuantileTransformer to deal with outliers.</li>
  <li>Cleaned special characters and extracted any duplicated info present in different columns.</li>
 </ul>

<h2>Exploratory Data Analysis</h2><br>
Checked the distribution of the data, evaluated correlation and did a feature selection using "feature imporance" from Random Forest Classifier.
<div>
<img src="https://github.com/tikoponde/classifying-job-links/blob/master/boxplot_len_atagcontent.JPG" alt="BoxPlot" width="300" height="300">
<img src="https://github.com/tikoponde/classifying-job-links/blob/master/heatmap_corr.JPG" alt="Heatmap" width="300" height="300">
</div>
<img src="https://github.com/tikoponde/classifying-job-links/blob/master/random_feature.JPG" alt="Importance" width="300" height="300">
  
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
