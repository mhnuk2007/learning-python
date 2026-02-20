# Chapter 19: Polling and Event-Driven Programming

Understanding the difference between polling and event-driven approaches.

## Status

- Completed

## Prerequisites

- Python 3.x
- Understanding of loops (Chapter 13)
- Understanding of async basics (helpful)

## How to run

```powershell
cd 19-polling_and_event_driven_programming
python .\polling.py
python .\event_driven.py
```

## Files and topics

### Polling Examples

| File | Focus |
| --- | --- |
| `polling.py` | Pizza delivery: checking door with pathlib |
| `polling-folder-monitor.py` | Continuously check for new files |
| `polling-sensor.py` | Simulated sensor check in a loop |

### Event-Driven Examples

| File | Focus |
| --- | --- |
| `event_driven.py` | Pizza delivery: scheduled life events (asyncio) |
| `event-driven-button.py` | Tkinter GUI button click handler |
| `event-driven-keyboard.py` | Async keyboard input monitoring |
| `event-driven-timer.py` | Tkinter timer using `after()` scheduling |
| `event-driven-async-sensor.py` | Async sensor monitoring without blocking |

### Data Files

| File | Focus |
| --- | --- |
| `front_door.txt` | Data file for polling.py example |

## Key concepts

### Polling

Continuously checking state in a loop:

```python
while hungry:
    check_door()
    time.sleep(1)
```

**Pros:** Simple to implement
**Cons:** Wastes CPU if events are rare, slower response time

### Event-Driven

Reacting to scheduled events:

```python
loop.call_later(1, alarm)
loop.call_later(4, doorbell)
loop.run_forever()
```

**Pros:** Efficient, scalable, responsive
**Cons:** Slightly more complex logic

### Event Loops

A loop that waits for events and dispatches them to handlers:

```python
# Tkinter
root.mainloop()

# Asyncio
asyncio.run(main())
```

## Comparison

| Approach | Pros | Cons | Use Case |
| --- | --- | --- | --- |
| Polling | Simple | Wastes CPU | Simple scripts, rare checks |
| Event-Driven | Efficient | More complex | GUI apps, network servers |

## Common Mistakes

- Polling too frequently wastes CPU cycles
- Blocking operations in event-driven programs freeze the system
- Confusing polling with true event-driven callbacks

## Notes

- Polling is simple but inefficient for large-scale systems
- Event-driven is ideal for GUI apps and async workflows
- Use Tkinter/PyQt for GUI apps, asyncio for network/sensors
- Always design event handlers to be non-blocking

## Theory Notes

- [`19-polling_and_event_driven_programming.md`](19-polling_and_event_driven_programming.md)