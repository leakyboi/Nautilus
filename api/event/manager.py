from typing import (
    Callable,
    Awaitable,
    Any,
    Optional,
)
import asyncio

CORO_FUNC = Callable[[Any], Awaitable]

async def execute_all(l: list[CORO_FUNC], args: tuple[Any]) -> None:
    """Sequentially executes all coroutines within `l` with `args`."""
    for func in l:
        await func(*args)

class EventManager:
    """A replication of the JavaScript event manager in Python."""
    
    __slots__ = (
        "_events",
    )
    
    def __init__(self) -> None:
        """Initialises an empty event manager."""
        
        self._events: dict[str, list[CORO_FUNC]] = {}
        
    def register(self, event: str, callback: CORO_FUNC) -> None:
        """Adds a callback to the event manager."""
        
        event_list = self._events.get(event)
        
        if event_list is None:
            self._events[event] = event_list = []
        
        event_list.append(callback)
    
    def on(self, event: str) -> Callable:
        """Decorator that ads a callback to the event manager."""
        
        def decorator(func: CORO_FUNC) -> CORO_FUNC:
            self.register(event, func)
            return func
        
        return decorator
    
    async def emit(self, event: str, *args: Any) -> Optional[Awaitable]:
        """Emits an event to the event manager."""
        
        event_list = self._events.get(event)
        
        if event_list is None:
            return
        
        loop = asyncio.get_event_loop()
        return loop.create_task(
            execute_all(event_list, args)
        )
        