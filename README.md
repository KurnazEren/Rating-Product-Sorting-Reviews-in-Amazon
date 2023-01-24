# Rating-Product-Sorting-Reviews-in-Amazon

**Business Problem:**
One of the most important problems in e-commerce is to see the points given to the products after sales correctly. The solution to this problem means providing more customer satisfaction for the e-commerce site, prominence of the product for the sellers and a complex shopping experience for the buyers. Another problem is scrutiny as the correct ordering of reviews given to products. Since misleading comments will directly affect the sale of the product, it will cause both financial loss and customer information. In the solution of these 2 basic problems, the e-commerce site and the sellers will complete the purchasing journey as complex while they are browsing their sales.

**Dataset Story**

*This dataset, which includes Amazon product data, includes product categories and various metadata. The product with the most reviews in the electronics category has user ratings and reviews.


**Variables:**
* reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B
* asin - ID of the product, e.g. 0000013714
* reviewerName - name of the reviewer
* helpful - helpfulness rating of the review, e.g. 2/3
* reviewText - text of the review
* overall - rating of the product
* summary - summary of the review
* unixReviewTime - time of the review (unix time)
* reviewTime - time of the review (raw)
* day_diff - Number of days since evaluation
* helpful_yes - The number of times the review was found helpful
* total_vote - Number of votes given to the review

**The Tasks**

Calculate Average Rating Based on Current Comments and compare it with existing Average Rating.
In the shared data set, users gave points and comments to a product.
Our aim in this task is to evaluate the scores given by weighting them by date.
It is necessary to compare the first average score with the weighted score according to the date to be obtained.
Calculate the weighted average score by date.
Specify 20 Reviews for the product to be displayed on the product detail page.
