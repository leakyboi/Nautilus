from typing import (
    Any,
    TypeVar,
    Generic,
    Union,
    Optional,
)

T = TypeVar("T")
KEY_TYPE = Union[str, int, tuple[Any, ...]]

class LRUCache(Generic[T]):
    """A simple LRU key-value cache implementation."""
    
    __slots__ = (
        "_cache",
        "capacity",
    )
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._cache: dict[KEY_TYPE, T] = {}
        
    def __len__(self) -> int:
        return len(self._cache)
    
    def __add_to_front(self, key: KEY_TYPE, value: T) -> None:
        """Adds a value of `value` to the front of the cache with the key `key`."""
        
        self._cache = {
            key: value
        } | self._cache
    
    def __clear_to_capacity(self) -> None:
        """Removes items from the end of the cache until it is at capacity."""
        
        cache_keys = tuple(self._cache.keys())
        rem_keys = cache_keys[self.capacity:]
        
        for key in rem_keys:
            self.remove(key)
        
    def remove(self, key: KEY_TYPE) -> None:
        """Remove a value from the cache with `key` key. Has no effect if value
        did not exist."""
        
        try:
            del self._cache[key]
        except KeyError:
            pass
    
    def get(self, key: KEY_TYPE) -> Optional[T]:
        """Attempts to fetch a value from the cache with the key `key`."""
        
        res = self._cache.get(key)
        
        # Move to front if found
        if res is not None:
            self.remove(key)
            self.__add_to_front(key, res)
        
        return res

    def insert(self, key: KEY_TYPE, value: T) -> None:
        """Inserts a value with key `key` to the front of the LRU cache."""
        
        self.__add_to_front(key, value)
        
        if len(self) > self.capacity:
            self.__clear_to_capacity()
