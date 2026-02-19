# 09-lists_and_tuples

## Learning goals

- Understand list and tuple behavior in Python.
- Use indexing, slicing, and unpacking effectively.
- Decide when to use mutable vs immutable sequence types.

## Key definitions

- `List`: ordered, mutable sequence.
- `Tuple`: ordered, immutable sequence.
- `Index`: position of an element in a sequence.
- `Slice`: subset of a sequence using `start:stop:step`.

## Core concepts

- Lists are ideal when data must change over time.
- Tuples are better for fixed records and safe constants.
- Slicing helps extract subranges without manual loops.
- Unpacking improves readability when handling structured values.

## Common mistakes

- Expecting tuple values to be editable.
- Confusing `append` (single item) and `extend` (iterable items).
- Off-by-one errors in slice boundaries.

## Quick recap

- Use lists for mutable collections.
- Use tuples for fixed, stable groupings.
