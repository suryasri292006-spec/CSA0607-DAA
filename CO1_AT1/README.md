# ShopSphere Scalability Audit

## Course Details

* **Course Code:** CSA06
* **Course Name:** Design and Analysis of Algorithms
* **Assessment:** CO1 – Assessment Tool 1

## Project Overview

This project analyses the scalability of ShopSphere, an online shopping platform. It evaluates five backend modules and a nightly report generator using algorithm analysis techniques.

## Objectives

* Analyse time and space complexity.
* Derive operation counts for iterative algorithms.
* Solve recurrence relations using backward substitution.
* Apply the Master Theorem and recursion-tree analysis.
* Compare best, average, and worst cases of searching algorithms.
* Estimate execution times for one million products.
* Recommend improvements for inefficient algorithms.

## Modules Analysed

1. Duplicate-Listing Detector
2. API Rate Limiter
3. Product Search – Sequential Search and Binary Search
4. Recommendation Engine – Current and Proposed Designs
5. Sales Analytics Engine
6. Nightly Report Generator

## Technologies Used

* Python 3
* GitHub
* Design and Analysis of Algorithms concepts

## Repository Structure

```text
CO1_AT1/
├── Question_1/
│   ├── Source_Code/
│   │   └── daa_analysis.py
│   └── Report/
│       └── ShopSphere_Scalability_Audit_Report.pdf
└── README.md
```

## Conclusion

The analysis identifies quadratic-time algorithms that require redesign and demonstrates how more efficient algorithms can improve scalability as the product catalogue grows.
