```
Map<Key, Value>:

    /*
    A map contains tuples of data - a key and it's respective value.

    A map has the following variants:
        * It cannot contain duplicates of the same key


    Can be seen as a further generalisation of lists.

    */

    // Returns True if there's an association for the key, k.
    boolean contains(Key k)

    // Returns the value associated with key, k.
    Value get(Key k)

    // Associates the key, k, with the value, v.
    void put(Key k, Value v)

    // Removes the value associated with the key, k.
    void remove(Key k)

    // Returns True if the Map is currently empty, False otherwise
    boolean is_empty()

    // Returns the current size (# of key-value pairs) in the map
    int size()

    // Iterates over all keys in the map
    Iterator<Key> keys()
```
