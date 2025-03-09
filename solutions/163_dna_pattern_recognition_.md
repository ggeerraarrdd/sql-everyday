# SQL Everyday \#163

## DNA Pattern Recognition

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Biologists are studying basic patterns in DNA sequences. Write a solution to identify `sample_id` with the following patterns:

* Sequences that start with ATG (a common start codon)
* Sequences that end with either TAA, TAG, or TGA (stop codons)
* Sequences containing the motif ATAT (a simple repeated pattern)
* Sequences that have at least 3 consecutive G (like GGG or GGGG)

Return the result table ordered by sample_id in ascending order. [[Full Description](https://leetcode.com/problems/dna-pattern-recognition/description/)]

## Submitted Solution

```sql
-- Submitted Solution
-- PostgreSQL
SELECT 
    sample_id
    ,dna_sequence
    ,species
    ,CASE WHEN dna_sequence LIKE 'ATG%' 
        THEN 1 ELSE 0 END AS has_start
    ,CASE WHEN dna_sequence LIKE '%TAA' 
        OR dna_sequence LIKE '%TAG' 
        OR dna_sequence LIKE '%TGA'
        THEN 1 ELSE 0 END AS has_stop
    ,CASE WHEN dna_sequence LIKE 'ATAT%' 
        OR dna_sequence LIKE '%ATAT%' 
        OR dna_sequence LIKE '%ATAT'
        THEN 1 ELSE 0 END AS has_atat
    ,CASE WHEN dna_sequence LIKE 'GGG%' 
        OR dna_sequence LIKE '%GGG%' 
        OR dna_sequence LIKE '%GGG'
        THEN 1 ELSE 0 END AS has_ggg
FROM Samples
ORDER BY sample_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
TBD
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
