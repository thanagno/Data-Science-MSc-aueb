# Data-Science-MSc-aueb

## Repository for the Numerical Optimization and Large Scale Linear Algebra

### Introduction

Randomized Numerical Linear Algebra (RNLA) techniques have emerged as crucial tools in the field of data science, offering innovative approaches for analyzing large-scale, high-dimensional datasets. The increasing availability of big data across various domains, such as finance, healthcare, and social networks, necessitates efficient algorithms that can handle large volumes of information while ensuring computational feasibility. RNLA methods provide solutions by leveraging randomness to simplify computations, reduce dimensionality, and improve the scalability of traditional numerical linear algebra techniques.

This project focuses on applying RNLA techniques to real-world datasets and comparing them with classical methods in terms of accuracy, speed, and resource efficiency. Specifically, two datasets are examined: (1) a financial dataset of stock prices and (2) a healthcare dataset related to heart disease indicators. These datasets are chosen to represent diverse applications and to explore how RNLA methods perform in different contexts, from time series financial data to binary classification in healthcare.

The primary objectives of this analysis are:

1. **Dimensionality Reduction**: Investigating how techniques like Sparse Random Projections can be used to reduce the number of features while maintaining predictive performance.
2. **Efficiency in SVD Computation**: Comparing traditional Singular Value Decomposition (SVD) with randomized SVD to assess differences in computational speed and accuracy.
3. **Performance Evaluation**: Evaluating and comparing the accuracy, precision, and recall of models trained using reduced data obtained through RNLA techniques versus traditional methods.

By integrating theoretical understanding with practical implementation, this study highlights the advantages and trade-offs associated with RNLA methods. The experimental results and comparative analysis provide insights into the balance between computational efficiency and accuracy, which is crucial for large-scale applications in today’s data-driven landscape. The findings underscore the relevance of RNLA techniques in modern data science, particularly in scenarios where processing speed and scalability are paramount.

In more detail the actions performed are:

### 1. **Data Preprocessing:**
   - Handling missing values.
   - Normalization and standardization.
   - Balancing classes using techniques like SMOTE.
   - Selecting relevant features based on correlation analysis.
These steps ensure that the data is ready for linear algebra applications and are a key part of the process described in the instructions.

### 2. **Development and Implementation of Algorithms:**
The analysis covers multiple RNLA techniques, such as:
   - Sparse Random Projection.
   - Traditional SVD vs. Randomized SVD.
The performance of these techniques is evaluated through experimental comparisons in terms of speed, accuracy, and computational resources. Hyperparameter tuning is also performed to optimize the models.

### 3. **Experimental Comparison:**
The project includes a detailed comparison between traditional methods (like SVD) and randomized techniques. It evaluates performance using metrics like accuracy, precision, recall, and F1-score. The analysis also investigates the impact of dimensionality reduction on classification performance.

### 4. **Report and Presentation:**
The entire workflow, results, and insights are presented with visualizations such as:
   - Confusion matrices.
   - Correlation heatmaps.
   - Histograms of feature distributions.
These visualizations make it easy to interpret the results and support a comprehensive final report. The analysis includes detailed discussions of the strengths, weaknesses, and potential applications of RNLA techniques.

### 5. **Concluding Remarks:**
The project highlight the advantages of RNLA techniques over traditional methods. It discusses the trade-offs between speed and accuracy and reflects on the effectiveness of different approaches for dimensionality reduction in real-world datasets.

---
