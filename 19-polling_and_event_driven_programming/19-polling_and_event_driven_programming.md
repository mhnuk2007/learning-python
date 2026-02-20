# Chapter 19 – Polling and Event-Driven Programming

## Learning Goals

- Understand the difference between polling and event-driven programming.
- Learn how to design programs that respond to external inputs efficiently.
- Explore examples using Python for both polling and event-based approaches.

## Key Definitions

- **Polling**: Continuously checking the state of a resource or input to detect changes.
  - Example: Checking a folder for new files every 5 seconds.

- **Event**: An occurrence or signal that triggers a specific action.
  - Example: A button click or network message arrival.

- **Event-Driven Programming**: Designing software to react to events rather than continuously checking for changes.

- **Callback Function**: A function passed as an argument to handle an event when it occurs.

- **Observer Pattern**: A design pattern where objects (observers) are notified automatically of state changes in another object (subject).

## Core Concepts

### 1. Polling

Simplest form of event checking: repeatedly query the state.

**Workflow:**
1. Check input/state.
2. Perform action if condition met.
3. Sleep for a while.
4. Repeat.

**Pros:** Simple to implement.
**Cons:** Wastes CPU if events are rare, slower response time.

### 2. Event-Driven Programming

Programs wait for events rather than checking repeatedly.

**Pros:** Efficient, scalable, responsive.
**Cons:** Slightly more complex logic, requires understanding event loops and callbacks.

### 3. Event Loops

A loop that waits for events and dispatches them to the appropriate handler.

Used extensively in:
- GUI frameworks (Tkinter, PyQt)
- Async frameworks (asyncio)

### 4. Typical Workflow

1. Initialize program state.
2. Register event handlers.
3. Start the event loop.
4. When an event occurs:
   - Invoke the appropriate handler.
   - Update state or trigger other actions.

## Common Mistakes

- Polling too frequently can waste CPU cycles.
- Not unregistering event handlers can lead to memory leaks.
- Blocking operations in event-driven programs can freeze the system.
- Confusing polling with true event-driven callbacks.

## Quick Recap

- **Polling**: Repeatedly check state, simple but inefficient.
- **Event-Driven**: Respond to events as they occur, efficient and scalable.
- Use GUI frameworks or async libraries for real-world event-driven programming.
- Always design event handlers to be non-blocking to maintain responsiveness.