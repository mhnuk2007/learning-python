# 10-stacks_and_queues

## Learning goals

- Understand stack and queue data-structure behavior.
- Implement basic operations in Python.
- Choose suitable standard library tools for each structure.

## Key definitions

- `Stack`: Last-In, First-Out (LIFO) structure.
- `Queue`: First-In, First-Out (FIFO) structure.
- `Push/Pop`: add/remove for stacks.
- `Enqueue/Dequeue`: add/remove for queues.

## Core concepts

- Python `list` can model a simple stack (`append`, `pop`).
- `collections.deque` is efficient for queue operations.
- `queue.Queue` is useful for thread-safe producer/consumer workflows.

## Common mistakes

- Using `list.pop(0)` repeatedly for queue behavior (slow for large lists).
- Mixing stack and queue semantics in the same structure.

## Quick recap

- Stack: latest item handled first.
- Queue: earliest item handled first.
