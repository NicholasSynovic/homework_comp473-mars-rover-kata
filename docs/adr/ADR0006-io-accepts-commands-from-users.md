# 6. IO accepts commands from users

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:41:54.9319213Z |

## Context

Users have to be able to send commands to the Rovers and get updated of the
current positon of each Rover after their command is processed.

## Decision

IO will collect all Rover commands sequentially and then apply the commands to
each Rover in the order that they were handled.

## Consequences

Commands can interfere with one another and introduce "race" condtions. To
handle this, if Rover A moves to a location that Rover B was supposed to move
to, Rover B should not move into that location and end command execution to
avoid interference with other Rovers or moving to an unexpected location.
