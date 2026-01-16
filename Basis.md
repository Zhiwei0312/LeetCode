# Algorithms & Data Structures

> **“The difference between a bad programmer and a good one is whether the programmer considers _code_ or _data structures_ more important.  
> Bad programmers worry about the code.  
> Good programmers worry about _data structures and their relationships_.”**  
> — Linus Torvalds (creator of Linux)

> **Algorithms + Data Structures = Programs**  
> — Niklaus Wirth (Turing Award winner, Switzerland)

---

## What Is an Algorithm?

> **Informal definition:**  
> An algorithm is any **well-defined computational procedure** that:
>
> - takes some value or set of values as **input**
> - produces some value or set of values as **output**
> - consists of a finite sequence of **computational steps**
> - transforms the input into the output

---

## Running Time Analysis

### Computational Model: RAM (Random Access Machine)

**Assumptions:**

1. Instructions are executed **sequentially**
2. **Basic instructions take constant time** `O(1)`
   - **Arithmetic:** add, subtract, multiply, divide, remainder, floor, ceiling
   - **Data movement:** load, store, copy
   - **Control:** conditional / unconditional branch, subroutine call and return
3. **Precision does not matter**

---

### What Does Running Time Depend On?

1. **Input size**
2. **Input quality** (for the same size)
   - good input
   - bad input

➡️ Usually, we focus on the **worst-case running time**.

---

### Simplification Rules

When analyzing asymptotic running time, focus on the important features:

1. **Drop lower-order terms**
2. **Ignore constant coefficients**

---

## Asymptotic Notation

- **O(·)**: upper bound (≥ worst case)
- **Ω(·)**: lower bound (≤ best case)
- **Θ(·)**: tight bound (O = Ω)
- **o(·)**: strictly smaller growth  
  - example: `n = o(n log n)`
- **ω(·)**: strictly larger growth  
  - example: `n log n = ω(n)`

---

## Sorting Algorithms

### 1. Insertion Sort

- **Time complexity:** `Θ(n²)`
- **Space:** in-place

**Intuition (playing cards analogy):**

1. Start with an empty left hand
2. Cards are face down on the table
3. Remove one card at a time
4. Insert it into the correct position in the left hand
5. Compare cards from **right to left**

![Insertion sort](./Day1_0116/figures/insertion_sort.png)

---

### Loop Invariant

**Statement:**

At the start of each iteration of the outer `for` loop (indexed by `j`),  
the subarray `A[1 … j−1]` consists of the elements originally in  
`A[1 … j−1]`, but in **sorted order**.

---

**Verification by induction:**

1. **Initialization**  
   True prior to the first iteration

2. **Maintenance**  
   If true before an iteration, it remains true afterward

3. **Termination**  
   When the loop terminates, the invariant guarantees that the algorithm
   is correct

---

## 2. Merge Sort

- **Paradigm:** Divide and Conquer
- **Time complexity:** `Θ(n log n)`
- **Space:** not in-place

---

### Divide and Conquer Strategy

1. **Divide**  
   Divide the problem into subproblems of the same type  
   Cost: `Θ(1)`

2. **Conquer**  
   Solve the subproblems recursively  
   Cost: `T(n / 2)`

3. **Combine**  
   Combine the subproblem solutions into the final solution  
   Cost: `Θ(n)`

![Divide and Conquer](./Day1_0116/figures/divide_conquer.png)  
![Merge](./Day1_0116/figures/merge.png)  
![Merge Sort](./Day1_0116/figures/mergeSort.png)

---

## Solving Recurrences

### 1. Substitution Method

- Guess the form of the solution
- Use **mathematical induction**
- Find constants to verify correctness

---

### 2. Recursion Tree Method

- Draw the recursion tree
- Analyze:
  - tree depth
  - work per level
- Generate a guess
- Verify using substitution

---

### 3. Master Theorem

![Master Theorem](./Day1_0116/figures/masterTheorem.png)

---

##### Note
$n - 1 \le \lfloor n \rfloor \le n$,  
$n \le \lceil n \rceil \le n + 1$


---

## Maximum Subarray Problem

### Brute-Force Solution

- **Time complexity:** `Θ(n²)`

---

### Divide and Conquer Solution

1. **Divide**  
   Split the array into two subarrays of (approximately) equal size

2. **Conquer**  
   Find the maximum subarray in:
   - `A[low … mid]`
   - `A[mid+1 … high]`

3. **Combine**  
   Find the maximum subarray **crossing the midpoint**

4. **Result**  
   Return the maximum of the three candidates

![Maximum Subarray](./Day1_0116/figures/maxArray.png)  
![Crossing Subarray](./Day1_0116/figures/crossArray.png)
