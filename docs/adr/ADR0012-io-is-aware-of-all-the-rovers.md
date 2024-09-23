# 12. IO is aware of all the Rovers

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:46:31.6419014Z |

## Context

The User needs to be able to send commands to all rovers via the IO.

## Decision

The IO class will publish commands to a set of Rovers with their respective
commands.

## Consequences

Each Rover will have to subscribe or listen to the IO class for broadcasted
commands.
