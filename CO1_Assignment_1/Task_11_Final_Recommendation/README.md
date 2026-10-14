# Task 11 — Final Recommendation

**Recommend binary search over sorted registration numbers**, with iterative binary search as the in-memory algorithm baseline. It has `Θ(log n)` worst-case time and `Θ(1)` auxiliary space, while recursive binary search has `Θ(log n)` time but `Θ(log n)` stack space.

For a real student-record system with 1,000,000 records and 50,000 searches/hour, prefer a database index on the unique registration-number column (for example, a B-tree index) rather than loading and searching all records in application memory for every request. An index is designed for lookup and persistence; daily additions can be handled by normal indexed inserts. If the assignment restricts the recommendation to the three implemented algorithms, choose iterative binary search, provided the data is sorted and the cost of maintaining that ordering is accounted for.
