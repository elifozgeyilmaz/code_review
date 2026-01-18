# AI Code Review Assignment (Python)

## Candidate
- Name: Elif Özge Yılmaz
- Approximate time spent: 1 hours

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- it excludes the cancelled orders while suming the order amount, however the number of the orders for finding the average is done by dividing the sum of noncancelled orders by number of all orders, which leads to mathematical error.

### Edge cases & risks
- If the input is not an iterable of order-like mappings (dicts), the function may fail or 
amount is non-numeric data types (e.g., strings that cannot be converted to numbers) or,
order amount is negative.
-If an order is missing "status" or "amount", the function can raise KeyError.



### Code quality / design issues
- The variable count is misleading, as it represents the total number of orders rather than the number of non-cancelled orders.

The function assumes a strict input schema without validation.

Behavior for empty input or all-cancelled input is not documented.
## 2) Proposed Fixes / Improvements
### Summary of changes
-  instead of dividing the sum of non-cancelled order amounts by number of all orders, I divide it by the number of noncancelled orders and,
I check if the amount is integral type and larger than 0.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would check by inputting negative amount of order and give a data typefor order amount which is not convertible to any integral data type.
- I also send non dictionary data type as a parameter.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation is incorrect because it claims the function divides by the number of non-cancelled orders, while the actual code divides by the total number of orders.

### Rewritten explanation
- This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of non-cancelled orders. It correctly excludes cancelled orders from the calculation.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

- It does not consider an important issue which leads to mathematically wrong result. However it is not necessary to design whole code from scratch.
It does not specify what to do about negative amounts. I assume that it is an error input.
Decision: Request Changes

Justification: The denominator is incorrect (divides by total orders instead of non-cancelled orders) and the function can raise errors for empty input or missing keys.

Confidence & unknowns: High confidence in the bug. Unknown: whether negative amounts (refunds) should be included; behavior for empty/all-cancelled input should be specified.


# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- It is not enough to check if whether input includes at least one '@' character, because email address conventions usually requires more things.

### Edge cases & risks
- if the given argument is not even a string, it would lead an error to check whether if '@' char in the variable.

### Code quality / design issues
-  necessary email address conventions are not addressed, therefore misleading design and result.

## 2) Proposed Fixes / Improvements
### Summary of changes
- check whether given input is list , and its elements are strings
if it is a string we need to get rid of starting and ending spaces,
also using a simplified, pragmatic email format validation, string should contains exactly one '@' character, not more or less, and
we check the email address by comparing with a valid address regex.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would give some errorness inputs like non-string data types, 
and give rare but acceptable email addresses like

Empty input: [] should return 0.

Non-string values: [None, 123, {}, []] should not crash and should count as 0.

Basic valid cases: ["a@b.com", "user.name+tag@sub.domain.com"].

Invalid format cases:

missing @: "abc.com"

multiple @: "a@@b.com"

empty local/domain: "@b.com", "a@"

spaces: "a b@c.com", "a@b .com"

domain dot edge cases: "a@.com", "a@com.", "a@com"

Whitespace handling: " a@b.com " should be treated as valid after trimming.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
-  it does not give any details about how it checks whether a given input is invalid or not, therefore it is not possible to understand it eliminates email addresses by conventions.

### Rewritten explanation
- This function counts the number of valid email addresses in the input list. It safely ignores non-string inputs, require exactly one "@", require non-empty local/domain parts, and require a dot in the domain (not at the start/end).

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

--- The issues are correctable with additional validation and do not require a complete redesign, it lacks of important detail to check whether the string is suitable for the email conventions or not.
Decision: Request Changes

Justification: The original function is overly permissive and can raise TypeError for non-string inputs; adding minimal validation fixes correctness and safety without redesign.

Confidence & unknowns: High confidence. Full RFC-compliant validation is intentionally out of scope; simplified rules are acceptable.

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- it does not include none data types while suming the result, however it divides the sum by number of all values which also may include none data types.

### Edge cases & risks
- if given parameter is not iterable, and includes non integral data types which cannot be sum.

### Code quality / design issues
- The variable name count is misleading because it represents total input length, not the number of valid measurements.

The function has no documented behavior for “no valid measurements” after filtering.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track valid_count separately and divide by the number of valid (non-None, numeric) measurements.
Skip values that are None or not convertible to float to avoid exceptions.
Optionally ignore non-finite values (NaN, +/-inf) to keep the output meaningful for real-world measurements.

Return None when there are no valid measurements to average (avoids division by zero and communicates “no data”).

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
Empty input: [] → should return None (or the defined fallback) without crashing.
Only missing values: [None, None] → should return None.
Mixed valid/None: [1, None, 3] → average should be (1+3)/2 = 2.0.
Convertible strings: ["1.5", "2"] → should return 1.75.
Non-convertible values: ["abc", {}, 5] → should ignore invalids and return 5.0.
Non-finite values if filtered: [1, float("nan"), 2] → should return 1.5 (if ignoring NaN), or document behavior.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The code does not actually “average the remaining values” correctly because it divides by the total length including None.

### Rewritten explanation
- This function computes the average of valid measurements by iterating through the input values and converting each non-None entry to float. Values that are missing (None) or not convertible to a numeric type are ignored. The function averages only the successfully parsed numeric measurements; if no valid measurements exist, it returns None to avoid division by zero.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

-Decision: Request Changes
-since it needs to divide the sum by number of data which is not none.
Justification: The function divides by the total length including None, producing incorrect averages, and may raise exceptions for non-numeric inputs.

Confidence & unknowns: High confidence in the bug. Unknown: desired policy for NaN/inf and expected return value when no valid measurements exist (None vs 0.0).


