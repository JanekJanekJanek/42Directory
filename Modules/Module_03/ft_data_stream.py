import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["Bob", "Dylan", "Alice", "Charlie"]
    actions = ["eat", "code", "sleep", "debug"]
    event = (random.choice(players), random.choice(actions))
    yield event


def consume_event(events: list[tuple[str, str]]) -> \
        typing.Generator[list[tuple[str, str]], None, None]:
    rnd = random.randint(0, len(events) - 1)
    print(f"Got event from list: {events[rnd]}")
    events.pop(rnd)
    yield events


def main() -> None:
    for i in range(1, 1000 + 1):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    actions_log = []
    for i in range(10):
        actions_log.append((next(gen_event())))
    print(f"\nBuilt list of 10 events:\n{actions_log}\n")
    while len(actions_log) > 0:
        remaining = next(consume_event(actions_log))
        print(f"Remains in list {remaining}")


if __name__ == "__main__":
    main()
