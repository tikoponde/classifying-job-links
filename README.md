# classifying-job-links

<h1>Data Science Job Link Classifier: Project Overview</h1><br>
<ul>
  <li>Created a tool that classifies if a website link is a Job Posting (97% accurracy) to enable a bot to scrape job postings from any given website.</li>
  <li>Scraped over 6000 job postings from the website of 68 employers in Canada.</li>
  <li>Engineered features using the information present in the 'a' element tag, such as keys, attributes and text.</li>
  <li>Optimized Random Forest, Logistic Regression, K-Nearest Neighbors and SVM using GridsearchCV.</li>
  <li>Built a Stack model.</li>
 </ul>

<h2>Code and Resources Used</h2><br>
<b>Python Version: </b>3.8<br>
<b>Packages: </b>pandas, numpy, sklearn, requests, re, matplotlib, seaborn, selenium, beautifulsoup, pickle, datetime, time<br>
<b>Stacking: </b> (https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/)<br>
<b>Documentation: </b> https://github.com/PlayingNumbers/ds_salary_proj<br>

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
  <li>Created clusters usining tolkens from the 'a' tag by applying the k-means model.</li>
  <li>Transformed the categorical variables into dummy variables.</li>
 </ul>

<h2>Exploratory Data Analysis</h2><br>
Checked the distribution of the data, evaluated correlation and did a feature selection using "feature imporance" from Random Forest Classifier.<br>
<div>
<img src="https://github.com/tikoponde/classifying-job-links/blob/master/images/boxplot_len_atagcontent.JPG" alt="BoxPlot" width="300" height="300">
<img src="https://github.com/tikoponde/classifying-job-links/blob/master/images/heatmap_corr.JPG" alt="Heatmap" width="400" height="400">
</div>
<img src="https://github.com/tikoponde/classifying-job-links/blob/master/images/random_feature.JPG" alt="Importance" width="200" height="300">

<h2>Model Building</h2>
Splited the train and test dataset with a test size of 30%.<br>
<br>
Tried 4 different models as estimators and built a stacking:
<ol>
  <li><b>Random Forest Classifier: </b>limited maxdepth to keep it from overfitting.</li>
  <li><b>SVC: </b>accepted higher missclassifications for processing time reasons.</li>
  <li><b>Logistic Regression: </b>well known model for classification.</li>
  <li><b>KNN: </b>one of the simplest models for classification, still really effective.</li>
  <li><b>Stacking: </b>used a logistic regression to combine the proba of the 4 estimators.</li>
</ol>

<h2>Model Performance</h2>
Random Forest had the best performance reaching a accurracy of 96,2% vs 96% from Stacking. Anyway, the latter has a better generalization, as we can see in the second image.
<img src="https://github.com/tikoponde/classifying-job-links/blob/master/images/model_performance.PNG" alt="performance" width="400" height="270">

<img src="https://github.com/tikoponde/classifying-job-links/blob/master/images/acc_by_comp.PNG" alt="performance" width="400" height="270"><br>
<br>
<h3>Contributors and acknowledgments</h3>
<br>
<b>Contributor: </b>Pedro Monteiro (https://www.linkedin.com/in/pedro-monteiro-05206722/)<br>
Special thanks to Ken Jee for all the content provided on your youtube channel (https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg)<br>
Also thanks to Tim for the Selenium tutorial (https://www.youtube.com/c/TechWithTim)<br>

  

